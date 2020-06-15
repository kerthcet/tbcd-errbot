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

        content = "## Project: %s \n> Repo: %s \n\n> Status: %s \n\n> Committer: %s \n\n> Message: %s" % (
            project, repositoryURL, "success", username, message)
        # TODO @somebody
        payload = {
            "msgtype": "markdown",
            "markdown": {
                "title": "%s👷 ✅" % project,
                "text": content,
            },
        }
        r = requests.post(targetURL, headers=headers, data=json.dumps(payload))
        self.log.info("post dingtalk response: %s", r.text)
        return r.text
