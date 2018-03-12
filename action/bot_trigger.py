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
import requests
from datetime import datetime

logger = logging.getLogger(__name__)

class ActionGreetTrigger(Action):
    @classmethod
    def name(cls):
        return 'action_greet_trigger'
    @classmethod
    def run(cls,dispatcher,tracker,domain):
        client = MongoClient('localhost',27017)
        db = client.user_database
        result = db.user_data.find()
        attachment_buttons = {'actions' :[{
                                          'name' : "great",
                                          'text' : "Great",
                                          'type' : "button",
                                          'value' : ""},{
                                          'name' : "bad",
                                          'text' : "Bad",
                                          'type' : "button",
                                          'value' : ""}]}
        if result :
            user_info = result[0]['user_info']
            
            date_format = "%Y-%m-%d"
            a = datetime.strptime(datetime.now().strftime(date_format),date_format)
            b = datetime.strptime(user_info['health_info']['weight_date'], date_format+' %H:%M:%S')
            days_ago = a - b
            weeks =str(user_info['health_info']['weeks'])
            response_text ='Hello, '+user_info['user_name']+'. \n'
            response_text += 'Here\'s a quick summary for you today.\n You\'re in week' + weeks +' '
            response_text += 'and your weight was '+str(user_info['health_info']['weight'])+'kg, '+str(days_ago.days)+'days ago. \n'
            weather_data = call_weather_api(result[0]['user_info']['address'])
            if weather_data :
                temp = weather_data['query']['results']['channel']['item']['forecast'][0]
                response_text += 'It\'s '+ temp['text'] + ' today. '
                response_text += 'Temperature is between ' + temp['low'] + ' C° and '+ temp['high'] + ' C°.\n '
            response_text += 'How are you feeling?'
            dispatcher.utter_button_message(response_text,attachment_buttons)

        return []

def call_weather_api(location) :
    if location =='seoul' :
        url = 'https://simple-weather.p.mashape.com/weatherData?lat=37.5&lng=127'
        user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36'
        values = {}
        headers = { 'X-Mashape-Key' : 'oU9MsC6CJemsht3yOzjFDFjH3AgDp15d2mgjsn2ciYL2LBRWna'}
        r= requests.get(url,headers=headers)
        data=r.json()
        return data
