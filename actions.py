from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
import re

from pymongo import MongoClient
from rasa_core.actions import Action
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.events import  ReminderScheduled, SlotSet, ActionExecuted
from datetime import datetime, timedelta
import requests

class ActionHappy(Action):
    def name(self):
        return "action_happy"
    def run(self,dispatcher,tracker,domain):
        intent_result = intent_classification_check(self, dispatcher, tracker, domain)
        if intent_result == 1 :
            response_text = "Great! I'm happy to hear that you are feeling good. Please let me know if you need any help."
            attachment_buttons = {'actions' :[{
                                                    'name' : "ask advice",
                                                    'text' : "Advice",
                                                    'type' : "button",
                                                    'value' : "",
                                                    'style': "primary"},{
                                                    'name' : "play music",
                                                    'text' : "Music",
                                                    'type' : "button",
                                                    'value' : "",
                                                    'style': "primary"},{
                                                    'name' : "great",
                                                    'text' : "Book",
                                                    'type' : "button",
                                                    'value' : ""},{
                                                    'name' : "great",
                                                    'text' : "Pregnancy Q",
                                                    'type' : "button",
                                                    'value' : ""},{
                                                    'name' : "no thanks",
                                                    'text' : "Nothing",
                                                    'type' : "button",
                                                    'value' : ""}]}
            dispatcher.utter_button_message(response_text,attachment_buttons)
            return []
        else:
            action_default(self,dispatcher,tracker,domain)
            return[] 

class ActionNotBad(Action):
    def name(self):
        return "action_not_bad"
    def run(self,dispatcher,tracker,domain):
        intent_result = intent_classification_check(self, dispatcher, tracker, domain)
        if intent_result == 1 :
            response_text = "I hope you feel bettter. Please let me know if you need any help."
            attachment_buttons = {'actions' :[{
                                                    'name' : "ask advice",
                                                    'text' : "Advice",
                                                    'type' : "button",
                                                    'value' : "",
                                                    'style': "primary"},{
                                                    'name' : "play music",
                                                    'text' : "Music",
                                                    'type' : "button",
                                                    'value' : "",
                                                    'style': "primary"},{
                                                    'name' : "great",
                                                    'text' : "Book",
                                                    'type' : "button",
                                                    'value' : ""},{
                                                    'name' : "great",
                                                    'text' : "Pregnancy Q",
                                                    'type' : "button",
                                                    'value' : ""},{
                                                    'name' : "no thanks",
                                                    'text' : "Nothing",
                                                    'type' : "button",
                                                    'value' : ""}]}
            dispatcher.utter_button_message(response_text,attachment_buttons)
            return []
        else:
            action_default(self,dispatcher,tracker,domain)
            return[] 
class ActionAskForwardDoctor(Action):
    def name(self):
        return "action_ask_forward_doctor"
    def run(self,dispatcher,tracker,domain):
        intent_result = intent_classification_check(self, dispatcher, tracker, domain)
        if intent_result == 1 :
            response_text = "Okay. Your question about hip pain is posted.\n I'll let you know when i get an answer or chat request from a doctor."
            dispatcher.utter_message(response_text)
            return []
        else:
            action_default(self,dispatcher,tracker,domain)
            return[]             
class ActionGoodbye(Action):
    def name(self):
        return "action_goodbye"
    def run(self,dispatcher,tracker,domain):
        intent_result = intent_classification_check(self, dispatcher, tracker, domain)
        if intent_result == 1 :
            response_text = "Bye"
            dispatcher.utter_message(response_text)
            return []
        else:
            action_default(self,dispatcher,tracker,domain)
            return[]             
class ActionPlayMusic(Action):
    def name(self):
        return "action_play_music"
    def run(self,dispatcher,tracker,domain):
        intent_result = intent_classification_check(self, dispatcher, tracker, domain)
        if intent_result == 1 :
            response_text = "Play music [April in Paris by Eddie Higgins Trio ]"
            dispatcher.utter_message(response_text)
            return []
        else:
            action_default(self,dispatcher,tracker,domain)
            return[] 

class ActionAskGeneralInfo(Action):
    def name(self):
        return "action_ask_general_info"
    def run(self,dispatcher,tracker,domain):
        intent_result = intent_classification_check(self, dispatcher, tracker, domain)
        if intent_result == 1 :
            response_text = "When nothing else works, have a warm water bath or apply a hot water bottle on your hip." 
            response_text += "\nWith advice and consultation from your doctor, you can also get a massage with warm oil to get relief from hip pain."
            response_text += "\nThe massage should be very gentle, and your bath water should be warm (not hot)."
            response_text += "\nIn addition, I would like you to schedule a prenatal massage eases the pains and aches of pregnancy."
            response_text += "\nA prenatal massage not only relaxes your muscles and de-stresses you but also makes you feel better. \nGo to a trained therapist so that they know where the exact sore spots lie."
            dispatcher.utter_message(response_text)
            return []
        else:
            action_default(self,dispatcher,tracker,domain)
            return[] 
class ActionAskDevice(Action):
    def name(self):
        return "action_ask_device"
    def run(self,dispatcher,tracker,domain):
        intent_result = intent_classification_check(self, dispatcher, tracker, domain)
        if intent_result == 1 :
            response_text = "You can use a patch up to about a week"
            dispatcher.utter_message(response_text)
            return []
        else:
            action_default(self,dispatcher,tracker,domain)
            return[] 

class ActionConfirmPurchase(Action):
    def name(self):
        return "action_confirm_purchase"
    def run(self,dispatcher,tracker,domain):
        intent_result = intent_classification_check(self, dispatcher, tracker, domain)
        if intent_result == 1 :
            response_text = "Order places. It'll arrive within 5days."
            dispatcher.utter_message(response_text)
            return []
        else:
            action_default(self,dispatcher,tracker,domain)
            return[] 
class ActionGreet(Action):
    def name(self):
        return "action_greet"
    def run(self,dispatcher,tracker,domain):
        intent_result = intent_classification_check(self, dispatcher, tracker, domain)
        if intent_result == 1 :
            response_text = "Hi, there"
            dispatcher.utter_message(response_text)
            return []
        else:
            action_default(self,dispatcher,tracker,domain)
            return[]            

class ActionAskRemedy(Action):
    def name(self):
        return "action_ask_remedy"
    def run(self,dispatcher,tracker,domain):
        intent_result = intent_classification_check(self, dispatcher, tracker, domain)
        if intent_result == 1 :
            response_text = "Practicing exercises that strengthen both the back muscles, as well as, your abdominal muscles will likely reduce hip pain. \nOne exercise that may provide relief is elevating your hips above chest level while lying on your back for a couple of minutes. \nTaking a warm bath or applying warm compresses to the sore area can reduce pain. In addition, a massage may ease soreness.\n As you get closer to your delivery date, make sure to sleep on your side and keep your legs and knees bent.\n Using pillows to support your abdomen and upper leg can alleviate uncomfortableness while sleeping. \nIf lying on your side worsens your hip pain, place a pillow or blanket at the small of your back and sleep leaning against it.\n This will reduce pressure on the hip you are sleeping on."
            dispatcher.utter_message(response_text)
            return []
        else:
            action_default(self,dispatcher,tracker,domain)
            return[]                    
                    
class ActionMakeDoctorsAppointment(Action):
    def name(self):
        return "action_make_doctors_appointment"
    def run(self,dispatcher,tracker,domain):
        intent_result = intent_classification_check(self, dispatcher, tracker, domain)
        if intent_result == 1 :
            response_text = "When would you like to see your doctor?"
            dispatcher.utter_message(response_text)
            return []
        else:
            action_default(self,dispatcher,tracker,domain)
            return[]  
class ActionAlternativeAnswer(Action):
    def name(self):
        return "action_alternative_answer"
    def run(self,dispatcher,tracker,domain):
        intent_result = intent_classification_check(self, dispatcher, tracker, domain)
        if intent_result == 1 :
            response_text = "I'm afraid I don't have information on it yet.\n I recommend accessing internet for that.\n I'll let you know when I acquire the knowledge later."
            dispatcher.utter_message(response_text)
            return []
        else:
            action_default(self,dispatcher,tracker,domain)
            return[] 
                    
class ActionAskMedicalAdvice(Action):
    def name(self):
        return "action_ask_medical_advice"
    def run(self,dispatcher,tracker,domain):
        intent_result = intent_classification_check(self, dispatcher, tracker, domain)
        if intent_result == 1 :
            response_text = "I'm sorry, I can't give you specific answer but I can forward your question to a doctor or give you general info on the symptom"
            attachment_buttons = {'actions' :[{
                                                    'name' : "ask doctor",
                                                    'text' : "To Doctor",
                                                    'type' : "button",
                                                    'value' : "",
                                                    'style': "primary"},{
                                                    'name' : "ask general info",
                                                    'text' : "General info",
                                                    'type' : "button",
                                                    'value' : ""}]}
            dispatcher.utter_button_message(response_text,attachment_buttons)
            return []
        else:
            action_default(self,dispatcher,tracker,domain)
            return[] 
class ActionSymptomStillBad(Action):
    def name(self):
        return "action_symptom_still_bad"
    def run(self,dispatcher,tracker,domain):
        intent_result = intent_classification_check(self, dispatcher, tracker, domain)
        if intent_result == 1 :
            response_text = "It is not uncommon to have pain around hip area during pregnancy.\n This occurs because your body is preparing itself for labor. \nSoreness and pain are often felt the strongest on the side where the baby tends to lie in your uterus."
            response_text += "I found some remedies for hip pain. Would you like to see it?"
            attachment_buttons = {'actions' :[{
                                                    'name' : "ask remedy",
                                                    'text' : "Yes",
                                                    'type' : "button",
                                                    'value' : "",
                                                    'style': "primary"},{
                                                    'name' : "no thanks",
                                                    'text' : "No",
                                                    'type' : "button",
                                                    'value' : ""}]}
            dispatcher.utter_button_message(response_text,attachment_buttons)
            return []
        else:
            action_default(self,dispatcher,tracker,domain)
            return[]             
class ActionSymptomWorse(Action):
    def name(self):
        return "action_symptom_worse"
    def run(self,dispatcher,tracker,domain):
        intent_result = intent_classification_check(self, dispatcher, tracker, domain)
        if intent_result == 1 :
            response_text = "If the pain persists, You would be better go see your doctor."
            dispatcher.utter_message(response_text)
            return []
        else:
            action_default(self,dispatcher,tracker,domain)
            return[] 
class ActionDisagree(Action):
    def name(self):
        return "action_disagree_forward_doctor"
    def run(self,dispatcher,tracker,domain):
        intent_result = intent_classification_check(self, dispatcher, tracker, domain)
        if intent_result == 1 :
            response_text = "I am afraid I might not be able to get the exact anwer without these. Anyways when I get answer, I will tell you. "
            dispatcher.utter_message(response_text)
            return []
        else:
            action_default(self,dispatcher,tracker,domain)
            return[]             
class ActionAskDoctor(Action):
    def name(self):
        return "action_ask_doctor"
    def run(self,dispatcher,tracker,domain):
        intent_result = intent_classification_check(self, dispatcher, tracker, domain)
        if intent_result == 1 :
            response_text = "I will forward your basic information and your symptom to OBGYN doctors' forum and ask if anyone can answer.\n Do you agree passing the information? Your name, address and contact information weill not be shared by me."
            attachment_buttons = {'actions' :[{
                                                    'name' : "agree on sending info",
                                                    'text' : "Agree",
                                                    'type' : "button",
                                                    'value' : "",
                                                    'style': "primary"},{
                                                    'name' : "disagree",
                                                    'text' : "Disagree",
                                                    'type' : "button",
                                                    'value' : "",
                                                    'style' : "danger"}]}
            dispatcher.utter_button_message(response_text,attachment_buttons)
            return []
        else:
            action_default(self,dispatcher,tracker,domain)
            return[]             
class ActionAskBadMood(Action):
    def name(self):
        return "action_ask_bad_mood"
    def run(self,dispatcher,tracker,domain):
        intent_result = intent_classification_check(self, dispatcher, tracker, domain)
        if intent_result == 1 :
            response_text = "Are you not feeling well regarding your pregnancy symptoms? Please let me know how I can help."
            attachment_buttons = {'actions' :[{
                                                    'name' : "ask advice",
                                                    'text' : "Advice",
                                                    'type' : "button",
                                                    'value' : "",
                                                    'style': "primary"},{
                                                    'name' : "play music",
                                                    'text' : "Music",
                                                    'type' : "button",
                                                    'value' : "",
                                                    'style': "primary"},{
                                                    'name' : "great",
                                                    'text' : "Book",
                                                    'type' : "button",
                                                    'value' : ""},{
                                                    'name' : "great",
                                                    'text' : "Pregnancy Q",
                                                    'type' : "button",
                                                    'value' : ""},{
                                                    'name' : "no thanks",
                                                    'text' : "Nothing",
                                                    'type' : "button",
                                                    'value' : ""}]}
            dispatcher.utter_button_message(response_text,attachment_buttons)
            return []
        else:
            action_default(self,dispatcher,tracker,domain)
            return[] 


class ActionSaveClipboard(Action):
    def name(self):
        return "action_save_clipboard"
    def run(self,dispatcher,tracker,domain):
        intent_result = intent_classification_check(self, dispatcher, tracker, domain)
        if intent_result == 1 :
            client = MongoClient('localhost',27017)
            db = client.user_database
            result = db.user_data.find()
            clip_contents=tracker.get_slot('clipboard')
            if clip_contents is None :
                clip_contents = ''
            attachment_buttons = {'actions' :[{
                                                'name' : "save clipboard...",
                                                'text' : "Clipboard",
                                                'type' : "button",
                                                'value' : "",
                                                'style': "primary",
                                                'confirm' : {
                                                    'title': "Clipboard",
                                                    'text' : clip_contents,
                                                    'dismiss_text' : "Close"}}]}
            dispatcher.utter_button_message('',attachment_buttons)
            return []
        else:
            action_default(self,dispatcher,tracker,domain)
            return[]   
       

class ActionAskDoctorsAppointment(Action):
    def name(self):
        return "ask_doctors_appointment"
    def run(self,dispatcher,tracker,domain):
        intent_result = intent_classification_check(self, dispatcher, tracker, domain)
        if intent_result == 1 :
            client = MongoClient('localhost',27017)
            db = client.user_database
            result = db.user_data.find()
            attachment_buttons = {'actions' :[{
                                                'name' : "make appointment",
                                                'text' : "Yes",
                                                'type' : "button",
                                                'value' : "",
                                                'style': "primary"},{
                                                'name' : "no thanks",
                                                'text' : "No",
                                                'type' : "button",
                                                'value' : "",
                                                'style': "danger"}]}
            if result :
                if result[0]['schedule']['appointment'] :
                    recent_schedule = result[0]['schedule']['appointment'][0]
                    print('recent_schedule check',recent_schedule)
                    dispatcher.utter_button_message('My record show that your next visit to ' + recent_schedule['doctor_name'] + ' is ' + recent_schedule['date'] + '. Do you want to reschedule?',attachment_buttons)
                else :
                    dispatcher.utter_button_message('You don\'t have any appointment. Do you like to make an appointment?',attachment_buttons)
            else :
                dispatcher.utter_button_message('You don\'t have any appointment. Do you like to make an appointment?',attachment_buttons)
            return []
        else:
            action_default(self,dispatcher,tracker,domain)
            return[] 

class ActionAskAdvice(Action):
    def name(self):
        return "action_ask_advice"        
    def run(self,dispatcher,tracker,domain):
        intent_result = intent_classification_check(self, dispatcher, tracker, domain)
        if intent_result == 1 :
            response_text = 'You may be feeling like you\'ve been pregnant for forever, but keep in mind the big day is less than two months away. \nYou should also note that most babies don\'t arrive on their due date or even within a couple of days of that target. Many babies arrive after week 38 or (and you may not want to read this) a couple of weeks after their due date. Every pregnancy is different. \nDoctors will want you to complete all 40 weeks to increase the chance of a healthy baby.'
          
            client = MongoClient('localhost',27017)
            db = client.user_database
            result = db.user_data.find()
            if result:
                clipboard_data = result[0]['clipboard']
                clip_data=clipboard_data['contents'] 
                clip_data+='\n\n'+response_text
                db.user_data.update_one({"_id": 1}, {"$set": {"clipboard":{"date":datetime.now().strftime('%Y-%m-%d %H:%m'),"contents":clip_data}}})
                tracker.update(SlotSet("clipboard",clip_data))
            dispatcher.utter_message(response_text)
            return []    
        else:
            action_default(self,dispatcher,tracker,domain)
            return[]  
            
class ActionFoodRecommendation(Action):
    def name(self):
        return "action_food_recommendation"
    def run(self,dispatcher,tracker,domain):
        intent_result = intent_classification_check(self, dispatcher, tracker, domain)
        if intent_result == 1 :
            reponse_text = 'Your weight is okay and you can eat whatever you want unless the doctor advised otherwise. Recommended calories are 2,200Kcal a day and try to avoid caffeine during pregnancy'
            dispatcher.utter_message(reponse_text)
            return []
        else:
            action_default(self,dispatcher,tracker,domain)
            return[]    

class ActionAskSymptom(Action):
    def name(self):
        return "action_ask_symptom"
    def run(self,dispatcher,tracker,domain):
        intent_result = intent_classification_check(self, dispatcher, tracker, domain)
        if intent_result == 1 :
            print('KB Data ......')
            reponse_text = 'Bloating is probably one of your least favorite pregnancy symptoms, and it usually shows up around week 11.\n'
            reponse_text += 'The bad news? It typically lasts until delivery day. \nBut you don’t have to suffer through it.\n'
            reponse_text += 'There are plenty of things you can do to beat the bloat and start feeling like your old self again. \nWater will help keep things moving in your gastrointestinal tract, so you can avoid constipation and the inevitable bloat that goes along with it.\n In addition, smaller meals are easier for your body to digest. \nOverloading your digestive system will only lead to more gas and bloating. \nPlus, eating six small meals will help keep your body and your baby  well nourished.'
            dispatcher.utter_message(reponse_text)
            client = MongoClient('localhost',27017)
            db = client.user_database
            result = db.user_data.find()
            if result :
                symptom_list = result[0]['chat_info']['symptoms']
                if symptom_list :
                    reponse_text = 'How are you doing with your ' + symptom_list[0]['name'] + '?'
                    attachment_buttons = {'actions' :[{
                                                    'name' : "great",
                                                    'text' : "Choose...",
                                                    'type' : "select",
                                                    'options': [
                                                                {
                                                                'text': "Better",
                                                                'value': "symptom better"
                                                                },{
                                                                'text': "Still there",
                                                                'value': "symptom still bad"
                                                                },{
                                                                'text': "Worse",
                                                                'value': "symptom worse"
                                                                }]}]}
                    dispatcher.utter_button_message(reponse_text,attachment_buttons)
            return []
        else:
            action_default(self,dispatcher,tracker,domain)
            return[]  
class ActionSymptomBetter(Action):
    def name(self):
        return 'action_symptom_better'  
    def run(self, dispatcher,tracker,domain): 
        intent_result = intent_classification_check(self, dispatcher, tracker, domain)
        if intent_result == 1 :
            response_text = 'Oh, great! Let me know if your symptoms worsen.'
            dispatcher.utter_message(response_text)
            return []  
        else:
            action_default(self,dispatcher,tracker,domain)
            return[] 
class ActionSetRemind(Action):
    def name(cls):
        return 'action_set_remind'
    def run(cls,dispatcher,tracker,domain):
        intent_result = intent_classification_check(cls, dispatcher, tracker, domain)
        if intent_result == 1 :
            action = 'action_ask_symptom'
            print("latest_bot_utterance===>",tracker.latest_bot_utterance)
            print("tracker.latest_message===>",tracker.latest_message)
            print("latest_action===>",tracker.latest_action_name)
            ReminderScheduled(action,datetime.now()+ timedelta(minutes=5))
            dispatcher.utter_message("Ok, I will let you know then.")
            return []
        else:
            action_default(self,dispatcher,tracker,domain)
            return[]   

class ActionAskSymptomBloom(Action):
    def name(self):
        return 'action_ask_symptom_bloom'
    def run(self,dispatcher,tracker,domain):
        intent_result = intent_classification_check(self, dispatcher, tracker, domain)
        if intent_result == 1 :
            print('KB Data ......')
            reponse_text = 'Bloom Symptom KB'
            #dispatcher.utter_message(reponse_text)
            client = MongoClient('localhost',27017)
            db = client.user_database
            result = db.user_data.find()   
            if result :
                health_info = result[0]['health_info']
                reponse_text += '\n You\'re in week'+ str(health_info['weeks']) + '. If they are not painful or regular, they may be Braxton Hicks contractions. You can try using Belli device. '
                reponse_text += 'Do you want more info?' 
                attachment_buttons = {'actions' :[{
                                                    'name' : "ask symptom more info",
                                                    'text' : "Yes",
                                                    'type' : "button",
                                                    'value' : "",
                                                    'style' : "primary"},{
                                                    'name' : "no thanks",
                                                    'text' : "No",
                                                    'type' : "button",
                                                    'value' : "",
                                                    'style' : "danger"}]}
                dispatcher.utter_button_message(reponse_text,attachment_buttons)
            return []
        else:
            action_default(self,dispatcher,tracker,domain)
            return[]                                       
class ActionAskMoreInfo(Action):
    def name(self):
        return 'action_ask_more_info'
    def run(self,dispatcher,tracker,domain):
        intent_result = intent_classification_check(self, dispatcher, tracker, domain)
        if intent_result == 1 :
            response_text = "Before 'true' labor begins, you may have 'false' labor pains. These are also known as Braxton Hicks contractions. They are your body's way of getting ready for the real thing -- the day you give birth -- but they are not a sign that labor has begun or is getting ready to begin. I'll put more info on your Clipboard."  
            clip_data = tracker.get_slot('clipboard')
            if clip_data is None :
                clip_data = ''
            clip_data += '\n\nbloom symptom : Before \'true\' labor begins, you may have \'false\' labor pains.'
            tracker.update(SlotSet("clipboard",clip_data))
            client = MongoClient('localhost',27017)
            db = client.user_database
            db.user_data.update_one({"_id": 1}, {"$set": {"clipboard":{"date":datetime.now().strftime('%Y-%m-%d %H:%m'),"contents":clip_data}}})
            dispatcher.utter_message(response_text)
            return []
        else:
            action_default(self,dispatcher,tracker,domain)
            return[]  
class ActionStartGreetTrigger(Action):
    def name(self):
        return 'action_start_greet_trigger'
    def run(self,dispatcher,tracker,domain):
        trigger_time = '10:54'
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
                                                'name' : "Not Bad",
                                                'text' : "Not Bad",
                                                'type' : "button",
                                                'value' : ""},{
                                                'name' : "bad mood",
                                                'text' : "Bad",
                                                'type' : "button",
                                                'value' : "",
                                                'style': "danger"}]}
                if result :
                    user_info = result[0]
                    
                    date_format = "%Y-%m-%d"
                    a = datetime.strptime(datetime.now().strftime(date_format),date_format)
                    b = datetime.strptime(user_info['health_info']['weight_date'], date_format+' %H:%M:%S')
                    days_ago = a - b
                    weeks =str(user_info['health_info']['weeks'])
                    response_text ='Hello, '+user_info['user_info']['user_name']+'. \n'
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
        intent_result = intent_classification_check(self, dispatcher, tracker, domain)
        if intent_result == 1 :
            client = MongoClient('localhost',27017)
            db = client.user_database
            result = db.user_data.find()
            if result:
                user_info = result[0]
                health_info = result[0]['health_info']
                remain_patch = 42 - health_info['weeks']
                response_text = 'You need about '+ str(remain_patch) + 'more patches before birth. \n'
                response_text += 'Shall I order '+ str(remain_patch) + 'using the same address ('+ user_info['user_info']['address']+') and '
                response_text += 'payment method? It\'s $20 including taxes and shipping.'
                attachment_buttons = {'actions' :[{
                                            'name' : "confirm purchase",
                                            'text' : "Yes",
                                            'type' : "button",
                                            'value' : "",
                                            'style' : "primary"},{
                                            'name' : "no thanks",
                                            'text' : "No",
                                            'type' : "button",
                                            'value' : "",
                                            'style' : "danger"
                                            }]}
                dispatcher.utter_button_message(response_text,attachment_buttons)
            return [] 
        else:
            action_default(self,dispatcher,tracker,domain)
            return[]   
     
class ActionDeviceTrigger(Action):
    def name(self):
        return 'action_device_trigger'
    def run(self, dispatcher,tracker,domain):
        response_text = 'You have high blood pressure! It is 138/60. High BP could cause pre-eclampsia so you\'d better take extra caution'
        response_text += 'Do you want to know more about pre-eclampsia?'
        attachment_buttons = {'actions' :[{
                                        'name' : "more about the disease",
                                        'text' : "Yes",
                                        'type' : "button",
                                        'value' : "",
                                        'style' : "primary"},{
                                        'name' : "no thanks",
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
        intent_result = intent_classification_check(self, dispatcher, tracker, domain)
        if intent_result == 1 :
            disease = tracker.get_slot('disease')   
            if disease :
                response_text = 'Pre-eclampsia is when you have high blood pressure and protein in your urine during pregnancy. \nIt can happen at any point after the 20th week of pregnancy, though in some cases it occurs earlier. \nYou may also have low clotting factors (platelets) in your blood or indicators of kidney or liver trouble. \nThis condition is also called toxemia or pregnancy-induced hypertension (PIH). \nEclampsia is a severe complication of preeclampsia. Eclampsia includes high blood pressure resulting in seizures during pregnancy. \nApproximately 5 to 10 percent of all pregnant women get preeclampsia.'
                attachment_buttons = {'actions' :[{
                                            'name' : "food for disease",
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
        else :
            action_default(self,dispatcher,tracker,domain)
            return[]   
class ActionAskFood(Action):
    def name(self):
        return 'action_ask_food'  
    def run(self, dispatcher,tracker,domain):
        intent_result = intent_classification_check(self, dispatcher, tracker, domain)
        if intent_result == 1 :
            disease = tracker.get_slot('disease') 
            if disease :
                response_text = 'I recommend food containg Ca, mineral, Fe. \nThey can help your blood circulations as well as High bp control. \nBesides, they are good for your baby\'s nutrition.'
                dispatcher.utter_message(response_text)
            return []  
        else:
            action_default(self,dispatcher,tracker,domain)
            return[]   
        
class ActionAskSupplements(Action):
    def name(self):
        return 'action_ask_supplements'  
    def run(self, dispatcher,tracker,domain): 
        intent_result = intent_classification_check(self, dispatcher, tracker, domain)
        if intent_result == 1 :
            disease = tracker.get_slot('disease') 
            if disease :
                response_text = 'That is a good idea. However, you\'d beeter talk to your doctor first before purchaseing supplements.'
                response_text += 'Besides, they are good for your baby\'s nutrition.'
                dispatcher.utter_message(response_text)
            return []  
        else:
            action_default(self,dispatcher,tracker,domain)
            return[]    
class ActionDenial(Action):
    def name(self):
        return 'action_denial'  
    def run(self, dispatcher,tracker,domain): 
        intent_result = intent_classification_check(self, dispatcher, tracker, domain)
        if intent_result == 1 :
            response_text = 'Okay. Ask me again anytime!'
            dispatcher.utter_message(response_text)
            return []  
        else:
            action_default(self,dispatcher,tracker,domain)
            return[]               
               
def action_default(cls,dispatcher,tracker,domain):
        dispatcher.utter_message("I am sorry. I don't understand what you are saying.")
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
        
def intent_classification_check(cls, dispatcher, tracker, domain):
    confidence_check = tracker.latest_message.intent['confidence']
    print("intent check===>",confidence_check)
    if confidence_check >= 0.25:
        return 1
    else:
        return 2    
        
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
