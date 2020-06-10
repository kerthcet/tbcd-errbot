from errbot import BotPlugin, webhook
import requests
import json


class Channel(BotPlugin):
    @webhook("/channel/<action>/", raw=True)
    def notify(self, request, action):
        body = json.loads(request.data)

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

    def post_dingtalk(self, targetURL, repositoryURL, project, username,
                      message):
        headers = {
            "Content-Type": "application/json",
        }

        content = "【%s】 Build Image Success @%s\n【Repository】 %s\n【Commit】 %s" % (
            project, username, repositoryURL, message)
        payload = {
            "msgtype": "text",
            "text": {
                "content": content,
            }
        }
        r = requests.post(targetURL, headers=headers, data=json.dumps(payload))
        return r.text
