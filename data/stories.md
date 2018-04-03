## default intent 
* default
- action_alternative_answer

## ask alternative answer
* ask_general
 - action_alternative_answer

## flow 1-1     <!--check doctors appointment -->
* ask_doctors_appointment
 - ask_doctors_appointment
* make_doctors_appointment
 - action_make_doctors_appointment
   
## flow 2-1     <!--food recommendation -->
* ask_food_recommendation
 - action_food_recommendation

## flow 3-1     <!--ask medical question-->
* ask_medical_advice
  - action_ask_medical_advice
* ask_doctor
  - action_ask_doctor
* ask_forward_doctor
  - action_ask_forward_doctor  
  
## flow 3-2
* ask_medical_advice
  - action_ask_medical_advice
* ask_general_info
  - action_ask_general_info

## flow 4       <!--ask device-->
* user_device_question
  - action_ask_device

## flow 5       <!--ask device purchase-->
* ask_device_purchase
  - action_ask_device_purchase
* confirm_purchase
  - action_confirm_purchase

## flow 6       <!--ask symptom bloom-->
* ask_symptom_bloom
  - action_ask_symptom_bloom
* ask_symptom_more_info
  - action_ask_more_info
  - action_save_clipboard

## flow 7-1       <!-- ask symptom-->
* ask_bad_symptom
  - action_ask_symptom
* ask_symptom_still_bad
  - action_symptom_still_bad
* ask_remedy
  - action_ask_remedy

## flow 7-2
* ask_bad_symptom
  - action_ask_symptom
* ask_symptom_worse
  - action_symptom_worse

## flow 11    <!-- bot trigger greet  -->
* greet
  - action_greet

## flow 11-12-1              
* start_greet_trigger              
  - action_start_greet_trigger
* ask_bad_mood <!-- user utterance, in format _intent[entities] -->
  - action_ask_bad_mood
* ask_advice
  - action_ask_advice
  - action_save_clipboard
  
## flow 11-12-2
* start_greet_trigger
 - action_start_greet_trigger
* ask_bad_mood <!-- user utterance, in format _intent[entities] -->
 - action_ask_bad_mood
* ask_music
 - action_play_music

## flow 11-12-3
* start_greet_trigger
 - action_start_greet_trigger
* ask_bad_mood <!-- user utterance, in format _intent[entities] -->
 - action_ask_bad_mood
* mood_great
 - action_happy
 
## flow 14
* start_product_recommendation_trigger
 - action_product_recommendation_trigger  
 
## set reminder
* user_set_reminder
 - action_set_remind
## play music path
* ask_music
 - action_play_music
 
## advice path
* ask_advice
- action_ask_advice
- action_save_clipboard

## happy path
* mood_great
 - action_happy

## comment bad symptom
* ask_bad_symptom
 - action_ask_symptom
  
## make doctors appointment
* make_doctors_appointment
 - action_make_doctors_appointment
  
## ask doctor
* ask_doctor
 - action_ask_doctor

## ask_general_info
 * ask_general_info
 - action_ask_general_info

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
  - action_goodbye

## ask advice
* ask_advice
  - action_ask_advice
  - action_save_clipboard  
  
## ask remedy
* ask_remedy
  - action_ask_remedy 

## symptom more info
* ask_symptom_more_info
  - action_ask_more_info
  - action_save_clipboard  

## ask doctor
* ask_doctor
  - action_ask_doctor
* ask_forward_doctor
  - action_ask_forward_doctor 
  
## confirm purchase
* confirm_purchase
  - action_confirm_purchase

## ask bad mood
* ask_bad_mood
  - action_ask_bad_mood

## mood not bad
* mood_not_bad
 - action_not_bad

## symptom better
* ask_symptom_better
 - action_symptom_better

## symptom worse
* ask_symptom_worse
 - action_symptom_worse

## answer denial
* answer_denial
 - action_denial 

## disagree forward doctor
* disagree_forward_doctor
 - action_disagree_forward_doctor 

## ask pregnancy q
* ask_pregnancy_q
 - action_pregnancy_q
 
## ask book
* ask_book
 - action_ask_book  

## good night trigger
* start_good_night_trigger 
 - action_good_night_trigger

## prenatal music play 
* play_prenatal_music
 - action_play_prenatal_music 
## excerpt trigger
* start_excerpt_trigger
 - action_start_excerpt_trigger
* ask_excerpt_info
 - action_ask_excerpt_info  