from errbot import BotPlugin, webhook
import requests
import json

TEKTON_URL = "http://el-tbcd:80"


class Gitlab(BotPlugin):
    @webhook("/ci/ping")
    def trigger(self, request):
        return "pong"

    @webhook("/ci/<action>/", raw=True)
    def trigger(self, request, action):
        body = json.loads(request.data)

        if action == "trigger":
            transformer["short_checkout_sha"] = self.read_short_commit_sha(
                body)
            transformer["project_name"] = self.read_repository_name(body)

            body["transformer"] = transformer
            resp = self.post_tekton(body)

            return {"code": 0, "msg": "success", "data": resp}
        return {"code": -1, "msg": "error action"}

    def read_repository_name(self, body):
        self.read_project_name(body).lower()

    def read_project_name(self, body):
        try:
            project_name = body['project']['name']
        except:
            project_name = ''
        finally:
            return project_name

    def read_short_commit_sha(self, body):
        try:
            sha = body['checkout_sha']
        except:
            sha = ""
        finally:
            return sha[0:7]

    def post_tekton(self, body):
        r = requests.post(TEKTON_URL, data=json.dumps(body))
        return r.text
