from errbot import BotPlugin, webhook
import requests
import json

TEKTON_URL = "http://el-tbcd:8080"


class Gitlab(BotPlugin):
    @webhook("/ci/ping")
    def trigger(self, request):
        return "pong"

    @webhook("/ci/<action>/", raw=True)
    def trigger(self, request, action):
        body = json.loads(request.data)

        if action == "trigger":
            self.trim_checkout_sha(body)
            self.lower_repository_name(body)
            resp = self.post_tekton(request.headers, body)

            return {"code": 0, "msg": "success", "data": resp}
        return {"code": -1, "msg": "error action"}

    def lower_repository_name(self, body):
        self.read_project_name(body).lower()

    def read_project_name(self, body):
        try:
            project_name = body['project']['name']
        except:
            project_name = ''
        finally:
            return project_name

    def trim_checkout_sha(self, body):
        try:
            sha = body['checkout_sha']
        except:
            sha = ""
        finally:
            return sha[0:7]

    def post_tekton(self, headers, body):
        r = requests.post(TEKTON_URL,
                          headers=json.dumps(headers),
                          data=json.dumps(body))
        return r.text
