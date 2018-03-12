
## flow 1-1     <!--check doctors appointment -->
  * ask_doctors_appointment
   - action_ask_doctors_appointment
  * make_doctors_appointment
   - utter_make_doctors_appointment
   
## flow 2-1     <!--food recommendation -->
* ask_food_recommendation
- utter_ask_food_recommendation

## flow 3-1     <!--ask medical question-->
* ask_medical_advice
- utter_alternative_answer
* ask_doctor
- utter_ask_doctor
  
## flow 3-2
* ask_medical_advice
- utter_alternative_answer
* ask_general_info
- utter_ask_general_info

## flow 4       <!--ask device-->
* ask_device
- utter_ask_device

## flow 5       <!--ask device purchase-->
* ask_device_purchase
- utter_ask_device_purchase
* confirm_purchase
- utter_confirm_purchase

## flow 6       <!--ask symptom bloom-->
* ask_symptom_bloom
- utter_ask_symptom_bloom
* ask_symptom_more_info
- utter_ask_symptom_more_info
- utter_save_clipboard

## flow 7-1       <!-- ask symptom-->
* ask_bad_symptom
- utter_ask_bad_symptom
* symptom_still_bad
- utter_symptom_still_bad
* ask_remedy
- utter_ask_remedy

## flow 7-2
* ask_bad_symptom
- utter_ask_bad_symptom
* symptom_worse
- utter_symptom_still_bad
* ask_remedy
- utter_ask_remedy
## flow 11-12-1              <!-- bot trigger greet  -->
* greet              
  - action_greet_trigger
* ask_bad_mood <!-- user utterance, in format _intent[entities] -->
  - utter_ask_bad_mood
* ask_advice
  - utter_ask_advice
  - utter_save_clipboard
  
## flow 11-12-2
* greet
 - action_greet_trigger
* ask_bad_mood <!-- user utterance, in format _intent[entities] -->
 - utter_ask_bad_mood
* ask_music
 - utter_play_music

## flow 11-12-3
* greet
 - action_greet_trigger
* ask_bad_mood <!-- user utterance, in format _intent[entities] -->
 - utter_ask_bad_mood
* mood_great
 - utter_happy
 
 ## flow 13-1
 * measure_trigger
 - utter_measure_trigger
 
 
## set reminder
* user_set_reminder
- utter_set_reminder
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
  - utter_ask_bad_symptom
  
## make doctors appointment
  * make_doctors_appointment
   - utter_make_doctors_appointment
  
## ask doctor
* ask_doctor
 - utter_ask_doctor

## ask_general_info
 * ask_general_info
 - utter_ask_general_info
 

## say goodbye
* goodbye
  - utter_goodbye
