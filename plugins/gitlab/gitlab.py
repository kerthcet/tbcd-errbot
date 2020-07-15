from errbot import BotPlugin, webhook
import requests
import json

TEKTON_URL = "http://el-tbcd:8080"


class Gitlab(BotPlugin):
    @webhook("/ci/<action>/", raw=True)
    def trigger(self, request, action):
        body = json.loads(request.data)

        if action == "trigger":
            body["transformer"] = {}
            self.trim_checkout_sha(body)
            self.lower_repository_name(body)
            resp = self.post_tekton(body)

            return {"code": 0, "msg": "success", "data": resp}
        return {"code": -1, "msg": "error action"}

    def lower_repository_name(self, body):
        project_name = body['project']['name']
        body['transformer']['project_name'] = project_name.replace("-",
                                                                   "").lower()

    def trim_checkout_sha(self, body):
        body['transformer']['checkout_sha'] = body['checkout_sha'][0:10]

    def post_tekton(self, body):
        headers = {
            "Content-Type": "application/json",
            "X-Gitlab-Event": "Push Hook",
        }
        r = requests.post(TEKTON_URL, headers=headers, data=json.dumps(body))
        self.log.info("post tekton response: %s", r.text)
        return r.text
