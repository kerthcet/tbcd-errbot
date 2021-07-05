from errbot import BotPlugin, webhook
import requests
import json

TEKTON_URL = "http://el-tekton-ci:8080"
BUMP_KEY_WORDS = 'Bump version'
TINY_NS = "Tiny"
TINY_IAC_URL = 'git@git.kid17.com:tiny/iac.git'
KID_IAC_URL = 'git@git.kid17.com:ops/iac.git'

DEFAULT_PROJECT_REPO = 'registry.cn-shanghai.aliyuncs.com/kid17_backend'
PROJECT_REPO_MAPS = {
    'Tiny': 'registry.cn-shanghai.aliyuncs.com/tiny-repo',
}


class Gitlab(BotPlugin):
    @webhook("/ci/<action>/", raw=True)
    def trigger(self, request, action):
        body = json.loads(request.data)

        if action == "trigger":
            body["transformer"] = {}
            self.lower_repository_name(body)
            self.get_iac_url(body)

            version, flag = self.get_bumpversion(body)
            if not flag:
                return {
                    "code": 0,
                    "msg": "success",
                    "data": "no need to build"
                }

            body["transformer"]["version"] = version
            body["transformer"]["ns"] = self.get_ns(version)
            body["transformer"]["message"] = self.get_message(body)

            body['transformer']['imageRepoUrl'] = self.get_group_repo(body)
            resp = self.post_tekton(body)

            return {"code": 0, "msg": "success", "data": resp}
        return {"code": -1, "msg": "error action"}

    def lower_repository_name(self, body):
        project_name = body['project']['name']
        body['transformer']['project_name'] = project_name.lower()

    def get_ns(self, version):
        if "dev" in version:
            return "dev"

        if "qa" in version:
            return "qa"

        if "rc" in version:
            return "rc"

        return "prod"

    def get_message(self, body):
        res = ""

        for i in range(len(body['commits']) - 1, 0, -1):
            m = body['commits'][i]
            res += m['message'].strip('\n') + '    \n'

        return res

    def get_iac_url(self, body):
        if self.get_group_namespace(body) == TINY_NS:
            body['transformer']['iacRepoUrl'] = TINY_IAC_URL
            return

        body['transformer']['iacRepoUrl'] = KID_IAC_URL

    def get_group_repo(self, body):
        repo = PROJECT_REPO_MAPS.get(self.get_group_namespace(body))
        if repo:
            return repo
        return DEFAULT_PROJECT_REPO

    def get_group_namespace(self, body):
        return body["project"]["namespace"]

    def get_bumpversion(self, body):
        sha = body['checkout_sha']
        for msg in body['commits']:
            if sha == msg['id']:
                m = msg['message']
                if BUMP_KEY_WORDS in m.strip('\n'):
                    return m.split(" ")[-1], True

        return "", False

    def post_tekton(self, body):
        headers = {
            "Content-Type": "application/json",
            "X-Gitlab-Event": "Push Hook",
        }
        r = requests.post(TEKTON_URL, headers=headers, data=json.dumps(body))
        self.log.info("post tekton response: %s", r.text)
        return r.text
