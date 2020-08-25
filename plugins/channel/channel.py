from errbot import BotPlugin, webhook
import requests
import json


class Channel(BotPlugin):
    @webhook("/channel/test", raw=True)
    def test(self, request):
        body = json.loads(request.data)

        params = body["taskRun"]["spec"]["params"]
        for param in params:
            if param["name"] == "targetURL":
                targetURL = param["value"]

            if param["name"] == "project":
                project = param["value"]

            if param["name"] == "username":
                username = param["value"]

            if param["name"] == "message":
                message = param["value"]

        success = body["taskRun"]["status"]["conditions"][0]["type"]
        if success != "Succeeded":
            title = "%s🤖 ❎" % project,
            content = "## Test: %s \n> Status: %s \n\n> Committer: %s \n\n> Message: %s" % (
                project, "failure🚨🚨🚨", username, message)
            return {
                "code": -1,
                "msg": "test failure",
                "data": self.post_dingtalk(targetURL, title, content)
            }

        title = "%s🤖 ✅" % project,
        content = "## Test: %s \n> Status: %s \n\n> Committer: %s \n\n> Message: %s" % (
            project, repositoryURL, "success🎉🎉🎉", username, message)
        return {
            "code": 0,
            "msg": "OK",
            "data": self.post_dingtalk(targetURL, title, content)
        }

    @webhook("/channel/build", raw=True)
    def build(self, request):
        body = json.loads(request.data)

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

        success = body["taskRun"]["status"]["conditions"][0]["type"]
        if success != "Succeeded":
            title = "%s👷 ❎" % project,
            content = "## Build: %s \n> Status: %s \n\n> Committer: %s \n\n> Message: %s" % (
                project, "failure🚨🚨🚨", username, message)
            return {
                "code": -1,
                "msg": "build image error",
                "data": self.post_dingtalk(targetURL, title, content)
            }

        title = "%s👷 ✅" % project,
        content = "## Build: %s \n> Repo: %s \n\n> Status: %s \n\n> Committer: %s \n\n> Message: %s" % (
            project, repositoryURL, "success🎉🎉🎉", username, message)
        return {
            "code": 0,
            "msg": "OK",
            "data": self.post_dingtalk(targetURL, title, content)
        }

    @webhook("/channel/sync", raw=True)
    def sync(self, request):
        body = json.loads(request.data)
        print(body)

    def post_dingtalk(self, targetURL, title, content):
        headers = {
            "Content-Type": "application/json",
        }

        payload = {
            "msgtype": "markdown",
            "markdown": {
                "title": title,
                "text": content,
            },
        }
        r = requests.post(targetURL, headers=headers, data=json.dumps(payload))
        self.log.info("post dingtalk response: %s", r.text)
        return r.text
