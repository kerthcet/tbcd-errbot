from errbot import BotPlugin, webhook


class Ping(BotPlugin):
    @webhook("/ping")
    def healthCheck(self, request):
        return "pong"
