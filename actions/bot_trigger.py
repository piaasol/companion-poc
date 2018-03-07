from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
import logging

from rasa_core import utils
from rasa_core.agent import Agent
from rasa_core.event import BotUttered
from rasa_core.channels.console import ConsoleInputChannel
from rasa_core.interpreter import RegexInterpreter
from rasa_core.channels import HttpInputChannel
from channels.slack import SlackInput
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.actions import Action

logger = logging.getLogger(__name__)

class ActionCheckRestaurants(Action):
    def bot_trigger():
        dispatcher.utter_template("utter_greet")
        BotUttered(parameters.get("text"),
                   parameters.get("data"),
                   parameters.get("timestamp"))
        BotUttered(text: "trigger greet start", data: null)
        BotUttered(text: utter_check_context: health over view, Enviornmental info, checking feeling included in the action, data: {
                   "buttons": {
                   "actions": [
                               {
                               "name": "great",
                               "text": "Great",
                               "type": "button",
                               "value": "great"
                               },
                               {
                               "name": "bad",
                               "text": "Bad",
                               "type": "button",
                               "value": "hate eating"
                               }
                               ]
                   }
                   })

def run_mood(serve_forever=True):
    agent = Agent.load("models/dialogue",
                       interpreter = RasaNLUInterpreter("models/nlu/default/current"))
    input_channel = SlackInput(slack_token="xoxb-313317646164-lJx89zZa02JztX9Bcc40vAvn",  # this is the `bot_user_o_auth_access_token`
                               slack_channel="general"  # the name of your channel to which the bot posts
                               )
                                                  
    if serve_forever:
                     agent.handle_channel(HttpInputChannel(5004, "/app", input_channel))
                     agent.handle_channel(ConsoleInputChannel())
                     return agent


if __name__ == '__main__':
    utils.configure_colored_logging(loglevel="DEBUG")
    run_mood()

