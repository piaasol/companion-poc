from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
import re

from pymongo import MongoClient
from rasa_core.actions import Action
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.events import  ReminderScheduled, SlotSet
from datetime import datetime, timedelta
import requests

class ActionAskDoctorsAppointment(Action):
    def name(self):
        return "ask_doctors_appointment"
    def run(self,dispatcher,tracker,domain):
        client = MongoClient('localhost',27017)
        db = client.user_database
        result = db.user_data.find()
        attachment_buttons = {'actions' :[{
                                            'name' : "make appointment",
                                            'text' : "Yes",
                                            'type' : "button",
                                            'value' : "",
                                            'style': "primary"},{
                                            'name' : "great",
                                            'text' : "No",
                                            'type' : "button",
                                            'value' : "",
                                            'style': "danger"}]}
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
    def name(self):
        return "action_food_recommendation"
    def run(self,dispatcher,tracker,domain):
        print('chect past diet history, weight,doctor\'s recommendation....')
        reponse_text = 'Your weight is okay and you can eat whatever you want unless the doctor advised otherwise. Recommended calories are ***Kcal and try to avoid *** during pregnancy'
        dispatcher.utter_message(reponse_text)
        
        return []

class ActionAskSymptom(Action):
    def name(self):
        return "action_ask_symptom"
    def run(self,dispatcher,tracker,domain):
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
                                                              'value': "the pain is even worse"
                                                              },{
                                                              'text': "Worse",
                                                              'value': "the pain is even worse"
                                                              }]}]}
                dispatcher.utter_button_message(reponse_text,attachment_buttons)
        return []

class ActionSetRemind(Action):
    def name(self):
        return 'action_set_remind'
    def run(self,dispatcher,tracker,domain):
        action = 'action_ask_symptom'
        print("latest_bot_utterance===>",tracker.latest_bot_utterance)
        print("tracker.latest_message===>",tracker.latest_message)
        print("latest_action===>",tracker.latest_action_name)
        ReminderScheduled(action,datetime.now()+ timedelta(minutes=5))
        dispatcher.utter_message("Ok, I will let you know then.")
        return []

class ActionAskSymptomBloom(Action):
    def name(self):
        return 'action_ask_symptom_bloom'
    def run(self,dispatcher,tracker,domain):
        print('KB Data ......')
        reponse_text = 'answer from KB Data..'
        dispatcher.utter_message(reponse_text)
        client = MongoClient('localhost',27017)
        db = client.user_database
        result = db.user_data.find()   
        if result :
            health_info = result[0]['user_info']['health_info']
            reponse_text += '\n You\'re in week'+ str(health_info['weeks']) + '. If they are not painful or regular, they may be Braxton Hicks contractions. You can try using Belli device. '
            reponse_text += 'Do you want more info?' 
            attachment_buttons = {'actions' :[{
                                                'name' : "ask symptom more info",
                                                'text' : "Yes",
                                                'type' : "button",
                                                'value' : "",
                                                'style' : "primary"},{
                                                'name' : "great",
                                                'text' : "No",
                                                'type' : "button",
                                                'value' : "",
                                                'style' : "danger"}]}
            dispatcher.utter_button_message(reponse_text,attachment_buttons)
        return []                                        

class ActionStartGreetTrigger(Action):
    def name(self):
        return 'action_start_greet_trigger'
    def run(self,dispatcher,tracker,domain):
        trigger_time = '14:13'
        current_time = datetime.time(datetime.now()).strftime('%H:%M')
        print("action greet tirgger start......")
        if trigger_time == current_time :
                client = MongoClient('localhost',27017)
                db = client.user_database
                result = db.user_data.find()
                attachment_buttons = {'actions' :[{
                                                'name' : "great",
                                                'text' : "Great",
                                                'type' : "button",
                                                'value' : "",
                                                'style': "primary"},{
                                                'name' : "i feel bad",
                                                'text' : "Bad",
                                                'type' : "button",
                                                'value' : "",
                                                'style': "danger"}]}
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
                    return [ReminderScheduled('action_start_greet_trigger', datetime.now()+ timedelta(days=1),kill_on_user_message=False)]
                          
        else :  
            return [ReminderScheduled('action_start_greet_trigger', datetime.now()+ timedelta(minutes=1),kill_on_user_message=False)]

  
class ActionAskDevicePurchase(Action):
    def name(self):
        return 'action_ask_device_purchase'
    def run(self,dispatcher,tracker,domain):
        client = MongoClient('localhost',27017)
        db = client.user_database
        result = db.user_data.find()
        if result:
            user_info = result[0]['user_info']
            health_info = result[0]['user_info']['health_info']
            remain_patch = 42 - health_info['weeks']
            response_text = 'You need about '+ str(remain_patch) + 'more patches before birth. \n'
            response_text += 'Shall I order '+ str(remain_patch) + 'using the same address ('+ user_info['address']+') and '
            response_text += 'payment method? It\'s $20 including taxes and shipping.'
            attachment_buttons = {'actions' :[{
                                        'name' : "confirm purchase",
                                        'text' : "Yes",
                                        'type' : "button",
                                        'value' : "",
                                        'style' : "primary"},{
                                        'name' : "great",
                                        'text' : "No",
                                        'type' : "button",
                                        'value' : "",
                                        'style' : "danger"
                                        }]}
            dispatcher.utter_button_message(response_text,attachment_buttons)
        return [] 
     
class ActionDeviceTrigger(Action):
    def name(self):
        return 'action_device_trigger'
    def run(self, dispatcher,tracker,domain):
        response_text = 'You have high blood pressure! It is 138/60. High BP could cause pre-eclampsia so you\'d better take extra caution'
        response_text += 'Do you want to know more about pre-eclampsia?'
        attachment_buttons = {'actions' :[{
                                        'name' : "i want to find more about this disease",
                                        'text' : "Yes",
                                        'type' : "button",
                                        'value' : "",
                                        'style' : "primary"},{
                                        'name' : "great",
                                        'text' : "No",
                                        'type' : "button",
                                        'value' : "",
                                        'style' : "danger"
                                        }]}
        tracker.update(SlotSet("disease","pre-eclampsia"))
        dispatcher.utter_button_message(response_text,attachment_buttons)
        return [] 

class ActionAskDisease(Action):
    def name(self):
        return 'action_ask_disease'
    def run(self, dispatcher,tracker,domain): 
        disease = tracker.get_slot('disease')   
        if disease :
            response_text = 'pre-eclampsia is a condition that pregnant women develop. \nIt is marked by high blood pressure in women who have ' 
            response_text += 'previously not experienced high blood pressure before. \nPre-eclamptic women will have a high level of pretein in their urin '
            response_text += 'and often also have swelling in the feet, legs and hands. \nThis condition usually appears late in pregnancy although it can occur earlier.'
            response_text += '\n If you\'s like to find details, please select the taps.'
            attachment_buttons = {'actions' :[{
                                        'name' : "helpful food for this disease",
                                        'text' : "Food Recommendation",
                                        'type' : "button",
                                        'value' : "",
                                        'style' : "primary"},{
                                        'name' : "great",
                                        'text' : "Cause",
                                        'type' : "button",
                                        'value' : ""
                                        },{
                                        'name' : "great",
                                        'text' : "Sign & Symptom",
                                        'type' : "button",
                                        'value' : ""
                                        }]}
            dispatcher.utter_button_message(response_text,attachment_buttons)
        return []  
class ActionAskFood(Action):
    def name(self):
        return 'action_ask_food'  
    def run(self, dispatcher,tracker,domain): 
        disease = tracker.get_slot('disease') 
        if disease :
            response_text = 'I recommend food containing Ca, meneral, Re. They can help your blood circulations as well as High bp controll.'
            response_text += 'Besides, they are good for your baby\'s nutrition.'
            dispatcher.utter_message(response_text)
        return []  
        
class ActionAskSupplements(Action):
    def name(self):
        return 'action_ask_supplements'  
    def run(self, dispatcher,tracker,domain): 
        disease = tracker.get_slot('disease') 
        if disease :
            response_text = 'That is a good idea. However, you\'d beeter talk to your doctor first before purchaseing supplements.'
            response_text += 'Besides, they are good for your baby\'s nutrition.'
            dispatcher.utter_message(response_text)
        return []        
                                        
class ActionProductRecommendationTrigger(Action):
    @classmethod
    def name(cls):
        return 'action_product_recommendation_trigger'
    @classmethod
    def run(cls,dispatcher,tracker,domain): 
        trigger_time = '19:00'
        current_time = datetime.time(datetime.now()).strftime('%H:%M')
        print("action greet tirgger start......")
        if trigger_time == current_time :
            response_text = 'In 6 weeks, you will meet your baby, Silvia. \nThere must be lots of thinks to consider and be prepared.\n Do you want me to show some helpful information?'                  
            attachment_buttons = {'actions' :[{
                                            'name' : "great",
                                            'text' : "Devices-Owlet, TytoCare",
                                            'type' : "button",
                                            'value' : ""},{
                                            'name' : "great",
                                            'text' : "Insurance",
                                            'type' : "button",
                                            'value' : ""
                                            },{
                                            'name' : "great",
                                            'text' : "Postpartum",
                                            'type' : "button",
                                            'value' : ""
                                            },{
                                            'name' : "remind me later",
                                            'text' : "Not now",
                                            'type' : "button",
                                            'value' : ""
                                            }]}
            dispatcher.utter_button_message(response_text,attachment_buttons)
            return [ReminderScheduled('action_product_recommendation_trigger', datetime.now()+ timedelta(days=1),kill_on_user_message=False)]
        return [ReminderScheduled('action_product_recommendation_trigger', datetime.now()+ timedelta(minutes=1),kill_on_user_message=False)]    
            
def call_weather_api(location) :
    if location =='seoul' :
        url = 'https://simple-weather.p.mashape.com/weatherData?lat=37.5&lng=127'
        user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36'
        values = {}
        headers = { 'X-Mashape-Key' : 'oU9MsC6CJemsht3yOzjFDFjH3AgDp15d2mgjsn2ciYL2LBRWna'}
        r= requests.get(url,headers=headers)
        data=r.json()
        return data   

class UsertriggerPolicy(KerasPolicy):
    def _build_model(self, num_features, num_actions, max_history_len):
        """Build a keras model and return a compiled model.
        :param max_history_len: The maximum number of historical turns used to
                                decide on next action"""
        from keras.layers import LSTM, Activation, Masking, Dense
        from keras.models import Sequential

        n_hidden = 32  # size of hidden layer in LSTM
        # Build Model
        batch_shape = (None, max_history_len, num_features)

        model = Sequential()
        model.add(Masking(-1, batch_input_shape=batch_shape))
        model.add(LSTM(n_hidden, batch_input_shape=batch_shape))
        model.add(Dense(input_dim=n_hidden, output_dim=num_actions))
        model.add(Activation('softmax'))

        model.compile(loss='categorical_crossentropy',
                      optimizer='adam',
                      metrics=['accuracy'])

        logger.debug(model.summary())
        return model   
          
#
# class ActionAskRemind(Action):
#     @classmethod
#     def name(cls):
#         return 'action_ask_remind'
#
#     @classmethod
#     def run(cls,dispatcher,tracker,domain):
#         print("tracker.latest_action_name===",tracker.latest_action_name)
#         dispatcher.utter_message("Do you want to confirm your booking at Papi's pizza?")
#         Reminder(tracker.latest_action_name, datetime.now() + timedelta(minutes=5))
#         return []
