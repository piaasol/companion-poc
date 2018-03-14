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
xoxb-313317646164-AA39Mr4cpa5Zn0ezArhFIRDh
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

class ActionFoodRecommendation(Action):
    @classmethod
    def name(cls):
        return 'action_food_recommendation'
    @classmethod
    def run(cls,dispatcher,tracker,domain):
        print('chect past diet history, weight,doctor\'s recommendation....')
        reponse_text = 'Your weight is okay and you can eat whatever you want unless the doctor advised otherwise. Recommended calories are ***Kcal and try to avoid *** during pregnancy'
        dispatcher.utter_message(reponse_text)
        
        return []

class ActionAskSymptom(Action):
    @classmethod
    def name(cls):
        return 'action_ask_symptom'
    @classmethod
    def run(cls,dispatcher,tracker,domain):
        print('KB Data ......')
        reponse_text = 'answer from KB Data..'
        dispatcher.utter_message(reponse_text)
        client = MongoClient('localhost',27017)
        db = client.user_database
        result = db.user_data.find()
        if result :
            symptom_list = result[0]['user_info']['chat_info']['symptoms']
            if symptom_list :
                reponse_text = 'How are you doing with your ' + symptom_list[0]['name'] + '?'
                attachment_buttons = {'actions' :[{
                                                  'name' : "great",
                                                  'text' : "Choose...",
                                                  'type' : "select",
                                                  'options': [
                                                              {
                                                              'text': "Better",
                                                              'value': "great"
                                                              },{
                                                              'text': "Still Bad",
                                                              'value': "still bad"
                                                              },{
                                                              'text': "Worse",
                                                              'value': "getting worse"
                                                              }]}]}
                dispatcher.utter_button_message(reponse_text,attachment_buttons)

