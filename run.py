from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
import logging

from rasa_core import utils
from rasa_core.agent import Agent
from rasa_core.channels.console import ConsoleInputChannel
from rasa_core.interpreter import RegexInterpreter
from rasa_core.channels import HttpInputChannel
from channels.slack import SlackInput
from rasa_core.interpreter import RasaNLUInterpreter

logger = logging.getLogger(__name__)

def run_mood(serve_forever=True):
    agent = Agent.load("models/dialogue",
                       interpreter = RasaNLUInterpreter("models/nlu/default/current"))
    input_channel = SlackInput(slack_token="xoxb-313317646164-ZWj0GQGnBt7U4ri2Rdl709qO",  # this is the `bot_user_o_auth_access_token`
                               slack_channel="general"  # the name of your channel to which the bot posts
                               )
                                                  
    if serve_forever:
                     agent.handle_channel(HttpInputChannel(5004, "/app", input_channel))
                     agent.handle_channel(ConsoleInputChannel())
                     return agent


if __name__ == '__main__':
    utils.configure_colored_logging(loglevel="DEBUG")
    run_mood()

