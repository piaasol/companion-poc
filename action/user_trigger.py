from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
import re

from pymongo import MongoClient
from rasa_core.actions.action import Action
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.events import  SlotSet, AllSlotsReset, Restarted, ActionExecuted

logger = logging.getLogger(__name__)

class ActionAskDoctorsAppointment(Action):
    @classmethod
    def name(cls):
        return 'action_ask_doctors_appointment'
    @classmethod
    def run(cls,dispatcher,tracker,domain):
        client = MongoClient('localhost',27017)
        db = client.user_database
        result = db.user_data.find()
        attachment_buttons = {'actions' :[{
                                            'name' : "great",
                                            'text' : "No",
                                            'type' : "button",
                                            'value' : ""},{
                                            'name' : "make appointment",
                                            'text' : "Yes",
                                            'type' : "button",
                                            'value' : ""}]}
        if result :
            if result[0]['user_info']['schedule']['appointment'] :
                recent_schedule = result[0]['user_info']['schedule']['appointment'][0]
                print('recent_schedule check',recent_schedule)
                dispatcher.utter_button_message('My record show that your next visit to ' + recent_schedule['doctor_name'] + ' is ' + recent_schedule['date'] + '. Do you want to reschedule?',attachment_buttons)
            else :
                dispatcher.utter_button_message('You don\'t have any appointment. Do you like to make an appointment?',attachment_buttons)
        else :
            dispatcher.utter_button_message('You don\'t have any appointment. Do you like to make an appointment?',attachment_buttons)
        return []
class ActionBadMood(Action):
    @classmethod
    def name(cls):
        return 'action_bad_mood'
    @classmethod
    def run(cls,dispatcher,tracker,domain):
        client = MongoClient('localhost',27017)
        db = client.user_database
        result = db.user_data.find()
        attachment_buttons = {'actions' :[{
                                          'name' : "great",
                                          'text' : "No",
                                          'type' : "button",
                                          'value' : "great"},{
                                          'name' : "make appointment",
                                          'text' : "Yes",
                                          'type' : "button",
                                          'value' : "make appointment"}]}
        if result :
            if result[0]['user_info']['schedule']['appointment'] :
                            recent_schedule = result[0]['user_info']['schedule']['appointment'][0]
                            print('recent_schedule check',recent_schedule)
                            dispatcher.utter_button_message('My record show that your next visit to ' + recent_schedule['doctor_name'] + ' is ' + recent_schedule['date'] + '. Do you want to reschedule?',attachment_buttons)
            else :
                            dispatcher.utter_button_message('You don\'t have any appointment. Do you like to make an appointment?',attachment_buttons)
        else :
            dispatcher.utter_button_message('You don\'t have any appointment. Do you like to make an appointment?',attachment_buttons)
        return []
