from errbot import BotPlugin, webhook
import requests
import json
import os

TEKTON_URL = "http://el-tbcd:8080"


class Gitlab(BotPlugin):
    @webhook("/ci/ping")
    def trigger(self, request):
        return "pong"

    @webhook("/ci/<action>/", raw=True)
    def trigger(self, request, action):
        body = json.loads(request.data)

        if action == "trigger":
            body["transformer"] = {}
            self.trim_checkout_sha(body)
            self.lower_repository_name(body)
            resp = self.post_tekton(body)

            return {"code": 0, "msg": "success", "data": resp}

        if action == "notify":
            params = body["taskRun"]["spec"]["params"]

            for param in params:
                if param["name"] == "targetURL":
                    targetURL = param["value"]

                if param["name"] == "repositoryURL":
                    repositoryURL = param["value"]

                if param["name"] == "project":
                    project = param["value"]

                if param["name"] == "username":
                    username = param["value"]

                if param["name"] == "message":
                    message = param["value"]

            return {
                "code":
                0,
                "msg":
                "success",
                "data":
                self.post_dingtalk(targetURL, repositoryURL, project, username,
                                   message)
            }

        return {"code": -1, "msg": "error action"}

    def lower_repository_name(self, body):
        body['transformer']['project_name'] = body['project']['name'].lower()

    def trim_checkout_sha(self, body):
        body['transformer']['checkout_sha'] = body['checkout_sha'][0:7]

    def post_tekton(self, body):
        headers = {
            "Content-Type": "application/json",
            "X-Gitlab-Event": "Push Hook",
        }
        r = requests.post(TEKTON_URL, headers=headers, data=json.dumps(body))
        return r.text

    def post_dingtalk(self, targetURL, repositoryURL, project, username,
                      message):
        headers = {
            "Content-Type": "application/json",
        }

        content = "%s build image success @%s.\nRepository: %s.\nCommit message: %s." % (
            project, username, repositoryURL, message)
        payload = {
            "msgtype": "text",
            "text": {
                "content": content,
            }
        }
        r = requests.post(targetURL, headers=headers, data=json.dumps(payload))
        return r.text
