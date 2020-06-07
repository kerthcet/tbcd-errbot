from errbot import BotPlugin, webhook
import requests
import json

TEKTON_URL = ""


class Gitlab(BotPlugin):
    @webhook("/ci/<action>/")
    def trigger(self, request, action):
        if action == "trigger":
            self.log.debug(action)
            return repr(request)
        return "Error action"

    def read_repository_name(self, body):
        self.read_project_name(body).lower()

    def read_project_name(self, body):
        try:
            project_name = body['project']['name']
        except:
            project_name = ''
        finally:
            return project_name.lower()

    def read_short_commit_sha(self, body):
        try:
            sha = body['checkout_sha']
        except:
            sha = ""
        finally:
            return sha[0:7]

    def read_user_name(self, body):
        return body['user_name']

    def get_git_ssh_url(self, body):
        try:
            url = body['project']['git_ssh_url']
        except:
            url = ""
        finally:
            return url

    def post_tekton(self, body):
        payload = {'key1': 'value1', 'key2': 'value2'}
        r = requests.post(TEKTON_URL, data=json.dumps(payload))
        return r.text
