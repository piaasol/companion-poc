from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import json
import logging

from flask import Blueprint, request, jsonify, make_response
from slackclient import SlackClient

from rasa_core.channels.channel import UserMessage, OutputChannel
from rasa_core.channels.rest import HttpInputComponent

logger = logging.getLogger(__name__)


class SlackBot(SlackClient, OutputChannel):
    """A Slack communication channel"""

    def __init__(self, token):
        super(SlackBot, self).__init__(token)
        print("SlackBot __init__")

    def send_text_message(self, recipient_id, message):
        super(SlackBot, self).api_call("chat.postMessage",
                                       channel=recipient_id,
                                       as_user=True, text=message)
        print("SlackBot.send_text_message")

    def send_image_url(self, recipient_id, image_url, message=""):
        image_attachment = [{"image_url": image_url,
                             "text": message}]
        super(SlackBot, self).api_call("chat.postMessage",
                                       channel=recipient_id,
                                       as_user=True,
                                       attachments=image_attachment)
        print("SlackBot.send_image_url")

    def _convert_to_slack_buttons(self, buttons):
        return [{"text": b['title'],
                 "name": b['payload'],
                 "type": "button"} for b in buttons]
        print("SlackBot._convert_to_slack_buttons")

    def send_text_with_buttons(self, recipient_id, message, buttons, **kwargs):
        print("SlackBot.send_text_with_buttons")
        if len(buttons) > 5:
            logger.warn("Slack API currently allows only up to 5 buttons. "
                        "If you add more, all will be ignored.")
            print("if len(buttons) > 5")
            return self.send_text_message(recipient_id, message)
               
       
        if "actions" in buttons :
           print("if actions in buttons")
           button_attachment = [{"fallback": message,
                                 "callback_id": message.replace(' ', '_')[:20],
                                 "actions":buttons.get('actions')
                                 }]
           super(SlackBot, self).api_call("chat.postMessage",
                                           channel=recipient_id,
                                           as_user=True,
                                           text=message,
                                           attachments=button_attachment)
        

        else :
            print("else actions in buttons")
            button_attachment = [{"fallback": message,
                                  "callback_id": message.replace(' ', '_')[:20],
                                  "actions": self._convert_to_slack_buttons(
                                      buttons)}]

            super(SlackBot, self).api_call("chat.postMessage",
                                           channel=recipient_id,
                                           as_user=True,
                                           text=message,
                                           attachments=button_attachment)


class SlackInput(HttpInputComponent):
    """Slack input channel implementation. Based on the HTTPInputChannel."""

    def __init__(self, slack_token, slack_channel):
        # type: (Text, Text) -> None
        """Create a Slack input channel.

        Needs a couple of settings to properly authenticate and validate
        messages. Details to setup:

        https://github.com/slackapi/python-slackclient
        :param slack_token: Your Slack Authentication token. You can find or
            generate a test token
             `here <https://api.slack.com/docs/oauth-test-tokens>`_.
        :param slack_channel: the string identifier for a channel to which
            the bot posts, or channel name
            (e.g. 'C1234ABC', 'bot-test' or '#bot-test')
        """
        self.slack_token = slack_token
        self.slack_channel = slack_channel
        print("SlackInput __init__")

    @staticmethod
    def _is_user_message(slack_event):
        print("SlackInput._is_user_message")
        return (slack_event.get('event') and
                slack_event.get('event').get('type') == u'message' and
                slack_event.get('event').get('text') and not
                slack_event.get('event').get('bot_id'))

    @staticmethod
    def _is_button_reply(slack_event):
        print("SlackInput._is_button_reply")
        return (slack_event.get('payload') and
                slack_event['payload'][0] and
                'name' in slack_event['payload'][0])

    @staticmethod
    def _get_button_reply(slack_event):
        print("SlackInput._get_button_reply")
        return json.loads(slack_event['payload'][0])['actions'][0]['name']

    def blueprint(self, on_new_message):
        print("SlackInput.blueprint")
        slack_webhook = Blueprint('slack_webhook', __name__)

        @slack_webhook.route("/", methods=['GET'])
        def health():
            print("SlackInput.health()")
            return jsonify({"status": "ok"})

        @slack_webhook.route("/webhook", methods=['GET', 'POST'])
        def webhook():
            request.get_data()
            print("SlackInput.webhook()")
            if request.json:
                print("if request.json")
                output = request.json
                print("output check==>",output)
                if "challenge" in output:
                    print("if challenge in output")
                    return make_response(output.get("challenge"), 200,
                                         {"content_type": "application/json"})
                elif self._is_user_message(output):
                    print("elif self._is_user_message")
                    text = output['event']['text']
                    sender_id = output.get('event').get('user')
                else:
                    print("else")
                    return make_response()
            elif request.form:
                print("elif request.form")
                output = dict(request.form)
                if self._is_button_reply(output):
                    print("if self._is_button_reply")
                    text = self._get_button_reply(output)
                    sender_id = json.loads(output['payload'][0]).get(
                        'user').get('id')
                else:
                    print("else self._is_button_reply")
                    return make_response()
            else:
                print("else request.json")
                return make_response()

            try:
                print("try webhook")
                out_channel = SlackBot(self.slack_token)
                user_msg = UserMessage(text, out_channel, sender_id)
                on_new_message(user_msg)
            except Exception as e:
                print(" except Exception")
                logger.error("Exception when trying to handle "
                             "message.{0}".format(e))
                logger.error(e, exc_info=True)
                pass

            return make_response()

        return slack_webhook
