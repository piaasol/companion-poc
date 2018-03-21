## default intent 
* default
- utter_alternative_answer

## ask alternative answer
* ask_general
 - utter_alternative_answer

## flow 1-1     <!--check doctors appointment -->
* ask_doctors_appointment
 - ask_doctors_appointment
* make_doctors_appointment
 - utter_make_doctors_appointment
   
## flow 2-1     <!--food recommendation -->
* ask_food_recommendation
 - action_food_recommendation

## flow 3-1     <!--ask medical question-->
* ask_medical_advice
  - utter_ask_medical_advice
* ask_doctor
  - utter_ask_doctor
* ask_forward_doctor
  - utter_ask_forward_doctor  
  
## flow 3-2
* ask_medical_advice
  - utter_ask_medical_advice
* ask_general_info
  - utter_ask_general_info

## flow 4       <!--ask device-->
* user_device_question
  - utter_ask_device

## flow 5       <!--ask device purchase-->
* ask_device_purchase
  - action_ask_device_purchase
* confirm_purchase
  - utter_confirm_purchase

## flow 6       <!--ask symptom bloom-->
* ask_symptom_bloom
  - action_ask_symptom_bloom
* ask_symptom_more_info
  - utter_ask_symptom_more_info
  - utter_save_clipboard

## flow 7-1       <!-- ask symptom-->
* ask_bad_symptom
  - action_ask_symptom
* symptom_still_bad
  - utter_symptom_still_bad
* ask_remedy
  - utter_ask_remedy

## flow 7-2
* ask_bad_symptom
  - action_ask_symptom
* symptom_worse
  - utter_symptom_still_bad
* ask_remedy
  - utter_ask_remedy 

## flow 11    <!-- bot trigger greet  -->
* greet
  - utter_greet

## flow 11-12-1              
* start_greet_trigger              
  - action_start_greet_trigger
* ask_bad_mood <!-- user utterance, in format _intent[entities] -->
  - utter_ask_bad_mood
* ask_advice
  - utter_ask_advice
  - utter_save_clipboard
  
## flow 11-12-2
* start_greet_trigger
 - action_start_greet_trigger
* ask_bad_mood <!-- user utterance, in format _intent[entities] -->
 - utter_ask_bad_mood
* ask_music
 - utter_play_music

## flow 11-12-3
* start_greet_trigger
 - action_start_greet_trigger
* ask_bad_mood <!-- user utterance, in format _intent[entities] -->
 - utter_ask_bad_mood
* mood_great
 - utter_happy
 
## flow 13-1
* measure_trigger
 - utter_measure_trigger

## flow 14
* start_product_recommendation_trigger
 - action_product_recommendation_trigger  
 
## set reminder
* user_set_reminder
 - action_set_remind
## play music path
* ask_music
 - utter_play_music
 
## advice path
* ask_advice
- utter_ask_advice
- utter_save_clipboard

## happy path
* mood_great
 - utter_happy

## comment bad symptom
* ask_bad_symptom
 - action_ask_symptom
  
## make doctors appointment
* make_doctors_appointment
 - utter_make_doctors_appointment
  
## ask doctor
* ask_doctor
 - utter_ask_doctor

## ask_general_info
 * ask_general_info
 - utter_ask_general_info

## device trigger
* start_device_trigger
 - action_device_trigger
* ask_disease
 - action_ask_disease 
* ask_food_advice
 - action_ask_food 
* ask_supplements 
 - action_ask_supplements
 
## food advice
* ask_food_advice
 - action_ask_food 
 
## ask desease
* ask_disease
 - action_ask_disease

## supplement 
* ask_supplements 
 - action_ask_supplements 

## say goodbye
* goodbye
  - utter_goodbye

## ask advice
* ask_advice
  - utter_ask_advice
  - utter_save_clipboard  
  
## ask remedy
* ask_remedy
  - utter_ask_remedy 

## symptom more info
* ask_symptom_more_info
  - utter_ask_symptom_more_info
  - utter_save_clipboard  

## ask doctor
* ask_doctor
  - utter_ask_doctor
* ask_forward_doctor
  - utter_ask_forward_doctor 
  
## confirm purchase
* confirm_purchase
  - utter_confirm_purchase