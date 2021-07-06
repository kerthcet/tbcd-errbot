Errbot
======

Errbot is a chatbot. It allows you to start scripts interactively from your chatrooms
for any reason: random humour, chatops, starting a build, monitoring commits, triggering
alerts...

It is written and easily extensible in Python.

Errbot is available as open-source software and released under the GPL v3 license.


Features
--------

Chat servers support
~~~~~~~~~~~~~~~~~~~~

**Built-in**

- IRC support
- `Hipchat support <http://www.hipchat.com/>`_
- `Slack support <https://slack.com/>`_
- `Telegram support <https://www.telegram.org/>`_
- `XMPP support <http://xmpp.org>`_

**With add-ons**

- `CampFire <https://campfirenow.com/>`_ (See `instructions <https://github.com/errbotio/err-backend-campfire>`__)
- `Cisco Spark <https://www.ciscospark.com/>`_ (See `instructions <https://github.com/marksull/err-backend-cisco-spark>`__)
- `Discord <https://www.discordapp.com/>`_ (See `instructions <https://github.com/gbin/err-backend-discord>`__)
- `Gitter support <https://gitter.im/>`_ (See `instructions <https://github.com/errbotio/err-backend-gitter>`__)
- `Mattermost <https://about.mattermost.com/>`_ (See `instructions <https://github.com/Vaelor/errbot-mattermost-backend>`__)
- `RocketChat <https://rocket.chat/>`_ (See `instructions <https://github.com/cardoso/errbot-rocketchat>`__)
- `Skype <https://www.skype.com/>`_ (See `instructions <https://github.com/errbotio/errbot-backend-skype>`__)
- `TOX <https://tox.im/>`_ (See `instructions <https://github.com/errbotio/err-backend-tox>`__)
- `VK <https://vk.com/>`_ (See `instructions <https://github.com/Ax3Effect/errbot-vk>`__)
- `Zulip <https://zulipchat.com/>`_ (See `instructions <https://github.com/zulip/errbot-backend-zulip>`__)


Administration
~~~~~~~~~~~~~~

After the initial installation and security setup, Errbot can be administered by just chatting to the bot (chatops).

- install/uninstall/update/enable/disable private or public plugins hosted on git
- plugins can be configured from chat
- direct the bot to join/leave Multi User Chatrooms (MUC)
- Security: ACL control feature (admin/user rights per command)
- backup: an integrated command !backup creates a full export of persisted data.
- logs: can be inspected from chat or streamed to Sentry.

Developer features
~~~~~~~~~~~~~~~~~~

- Very easy to extend in Python! (see below)
- Presetup storage for every plugin i.e. ``self['foo'] = 'bar'`` persists the value.
- Conversation flows to track conversation states from users.
- Webhook callbacks support
- supports `markdown extras <https://pythonhosted.org/Markdown/extensions/extra.html>`_ formatting with tables, embedded images, links etc.
- configuration helper to allow your plugin to be configured by chat
- Text development/debug consoles
- Self-documenting: your docstrings become help automatically
- subcommands and various arg parsing options are available (re, command line type)
- polling support: your can setup a plugin to periodically do something
- end to end test backend
- card rendering under Slack and Hipchat.

Community and support
---------------------

If you have:

- a quick question feel free to join us on chat at `errbotio/errbot on Gitter <https://gitter.im/errbotio/errbot>`_.
- a plugin development question please use `Stackoverflow <http://stackoverflow.com/questions/tagged/errbot>`_ with the tags `errbot` and `python`.
- a bug to report or a feature request, please use our `GitHub project page <https://github.com/errbotio/errbot/issues>`_.

You can also ping us on Twitter with the hashtag ``#errbot``.


Installation
------------

Prerequisites
~~~~~~~~~~~~~

Errbot runs under Python 3.6+ on Linux, Windows and Mac. For some chatting systems you'll need a key or a login for your bot to access it.

Quickstart
~~~~~~~~~~

docker exec -it <container> sh
errbot

How To Config Webserver
Step1: RUN errbot
Step2: RUN !plugin config Webserver {'HOST': '0.0.0.0', 'PORT': 3141, 'SSL': {'certificate': '', 'enabled': False, 'host': '0.0.0.0', 'key': '', 'port': 3142}}
Step3: RUN !plugin activate Webserver
Step4: RUN !restart
Step5: RUN curl -X POST http://localhost:3141/ping

## How To Use
Step1: RUN docker pull yaphetsglhf/chatops-errbot:tag
Step2: docker run -it -p 3141:3141 chatops-errbot:tag
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
