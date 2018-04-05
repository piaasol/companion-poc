from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import json
import logging

from flask import Blueprint, request, jsonify, make_response, current_app, Flask
from slackclient import SlackClient

from rasa_core.channels.channel import UserMessage, OutputChannel
from rasa_core.channels.rest import HttpInputComponent
from rasa_core.events    import ActionExecuted, BotUttered, SlotSet

from datetime   import datetime
import time
import sched
from threading import Timer

logger = logging.getLogger(__name__)


class SlackBot(SlackClient, OutputChannel):
    """A Slack communication channel"""

    def __init__(self, token):
        super(SlackBot, self).__init__(token)
        #print("SlackBot __init__")

    def send_text_message(self, recipient_id, message):
        super(SlackBot, self).api_call("chat.postMessage",
                                       channel=recipient_id,
                                       as_user=True, text=message)
        #print("SlackBot.send_text_message")

    def send_image_url(self, recipient_id, image_url, message=""):
        image_attachment = [{"image_url": image_url,
                             "text": message}]
        super(SlackBot, self).api_call("chat.postMessage",
                                       channel=recipient_id,
                                       as_user=True,
                                       attachments=image_attachment)

    def _convert_to_slack_buttons(self, buttons):
        return [{"text": b['title'],
                 "name": b['payload'],
                 "type": "button"} for b in buttons]

    def send_text_with_buttons(self, recipient_id, message, buttons, **kwargs):
        
        #print("SlackBot.send_text_with_buttons",recipient_id)
        if len(buttons) > 5:
            logger.warn("Slack API currently allows only up to 5 buttons. "
                        "If you add more, all will be ignored.")
            return self.send_text_message(recipient_id, message)
               
       
        if "actions" in buttons :
           button_attachment = [{"fallback": message,
                                 "callback_id" : message.replace(' ', '_')[:20],
                                 "color" : "#3AA3E3",
                                 "actions":buttons.get('actions')
                                 }]
           super(SlackBot, self).api_call("chat.postMessage",
                                           channel=recipient_id,
                                           as_user=True,
                                           text=message,
                                           attachments=button_attachment)
        

        elif "dialog" in  buttons :
            dialog = buttons.get('dialog',buttons.get('dialog'))
#            dialog['callback_id'] = message.replace(' ', '_')[:20]
            dialog_attachment = [{"fallback": message,
                                 "dialog":buttons.get('dialog')
                                 }]
            super(SlackBot, self).api_call("dialog.open",
                                               channel=recipient_id,
                                               as_user=True,
                                               dialog=buttons.get('dialog')
                                               )
                
        else :
            button_attachment = [{"fallback": message,
                                  "callback_id": message.replace(' ', '_')[:20],
                                   "color" : "#3AA3E3",
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
        

    @classmethod
    def __enter__(cls):
        return cls

    @classmethod
    def __exit__(cls, typ, value, tb):
        print('')

    @staticmethod
    def _is_user_message(slack_event):
        return (slack_event.get('event') and
                slack_event.get('event').get('type') == u'message' and
                slack_event.get('event').get('text') and not
                slack_event.get('event').get('bot_id'))

    @staticmethod
    def _is_button_reply(slack_event):
        return (slack_event.get('payload') and
                slack_event['payload'][0] and
                'name' in slack_event['payload'][0])

    @staticmethod
    def _get_button_reply(slack_event):
        return json.loads(slack_event['payload'][0])['actions'][0]['name']
    
    @staticmethod
    def greet_trigger(self, on_new_message):
        
        user_id = "U98A5D231"
        out_channel = SlackBot(self.slack_token)
        user_msg = UserMessage("greet trigger start now", out_channel, user_id)
        on_new_message(user_msg)
        make_response()
        user_msg = UserMessage("product recommendation start...", out_channel, user_id)
        on_new_message(user_msg)
        make_response()
        user_msg = UserMessage("night trigger", out_channel, user_id)
        on_new_message(user_msg)
        make_response()
        user_msg = UserMessage("excerpt trigger", out_channel, user_id)
        on_new_message(user_msg)
        make_response()
        
        
    def blueprint(self, on_new_message):
        slack_webhook = Blueprint('slack_webhook', __name__)
        app = Flask(__name__)
        # with app.app_context():
        #     self.greet_trigger(self,on_new_message)
         
        @slack_webhook.route("/", methods=['GET'])
        def health():
                return jsonify({"status": "ok"})
        
        @slack_webhook.route("/message_actions", methods=['POST'])
        def message_actions():
                request_form_data = dict(request.form)
                if request_form_data['payload'] :
                    action_data = json.loads(request_form_data['payload'][0]).get('actions')
                    if action_data :
                        action_type = action_data[0]['type']
                        if action_type == 'select' :
                            user_text = action_data[0]['selected_options'][0]['value']
                        elif action_type == 'button' :
                            user_text = action_data[0]['name']
                    sender_id = "U98A5D231"
                    #sender_id = json.loads(request_form_data['payload'][0]).get(
                                                                     #'user').get('id')
                out_channel = SlackBot(self.slack_token)
                user_msg = UserMessage(user_text, out_channel, sender_id)
                on_new_message(user_msg)
                return make_response()
    
        @slack_webhook.route("/webhook", methods=['GET', 'POST'])
        def webhook():
                request.get_data()
                if request.json:
                    output = request.json
                    if "challenge" in output:
                        return make_response(output.get("challenge"), 200,
                                             {"content_type": "application/json"})
                    elif self._is_user_message(output):
                        text = output['event']['text']
                        sender_id = "U98A5D231"
                        #sender_id = output.get('event').get('user')
                    else:
                        return make_response()
                elif request.form:
                    output = dict(request.form)
                    if self._is_button_reply(output):
                        text = self._get_button_reply(output)
                        sender_id = "U98A5D231"
                        # sender_id = json.loads(output['payload'][0]).get(
                        #     'user').get('id')
                    else:
                        return make_response()
                else:
                    return make_response()

                try:
                    out_channel = SlackBot(self.slack_token)
                    user_msg = UserMessage(text, out_channel, sender_id)
                    on_new_message(user_msg)
                except Exception as e:
                    logger.error("Exception when trying to handle "
                                 "message.{0}".format(e))
                    logger.error(e, exc_info=True)
                    pass

                return make_response()

        return slack_webhook


