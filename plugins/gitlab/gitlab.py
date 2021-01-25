from errbot import BotPlugin, webhook
import requests
import json

TEKTON_URL = "http://el-tbcd:8080"
BUMP_KEY_WORDS = 'Bump version'


class Gitlab(BotPlugin):
    @webhook("/ci/<action>/", raw=True)
    def trigger(self, request, action):
        body = json.loads(request.data)

        if action == "trigger":
            body["transformer"] = {}
            self.trim_checkout_sha(body)
            self.lower_repository_name(body)

            version, flag = self.get_bumpversion(body)
            if not flag:
                return {
                    "code": 0,
                    "msg": "success",
                    "data": "no need to build"
                }

            body["transformer"]["version"] = version
            body["transformer"]["ns"] = self.get_ns(version)
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

    def trim_checkout_sha(self, body):
        body['transformer']['checkout_sha'] = body['checkout_sha'][0:10]

    def get_bumpversion(self, body):
        length = len(body['commits'])
        for i in range(length - 1, -1, -1):
            m = body['commits'][i]
            msg = m['message']
            if BUMP_KEY_WORDS in msg:
                version = msg.split(" ")[-1]
                return version.split("\n")[0], True

        return "", False

    def post_tekton(self, body):
        headers = {
            "Content-Type": "application/json",
            "X-Gitlab-Event": "Push Hook",
        }
        r = requests.post(TEKTON_URL, headers=headers, data=json.dumps(body))
        self.log.info("post tekton response: %s", r.text)
        return r.text
