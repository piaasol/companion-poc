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
from channels.slack import SlackInput, SlackBot
from rasa_core.interpreter import RasaNLUInterpreter
import datetime
from rasa_core.events import ActionExecuted
import sched, time
from flask import Blueprint, request, jsonify, make_response
from slackclient import SlackClient

logger = logging.getLogger(__name__)


def run_mood(serve_forever=True):
    print("run_mood()")
    agent = Agent.load("models/dialogue",
                       interpreter=RasaNLUInterpreter("models/nlu/default/current"))
    
    input_channel = SlackInput(slack_token="",  # this is the `bot_user_o_auth_access_token`
                               slack_channel="bloomchatbot"  # the name of your channel to which the bot posts
                               )                                      
    if serve_forever:
         print("input channel check==>", input_channel)
         agent.handle_channel(HttpInputChannel(5004, "/app", input_channel))
         agent.handle_channel(ConsoleInputChannel())
         return agent

if __name__ == '__main__':
    utils.configure_colored_logging(loglevel="DEBUG")
    run_mood()


