## default 1-1       <!-- no intents found -->
* default
 - utter_alternative_answer
 * ask_doctor
  - utter_ask_doctor
  
## default 1-2       <!-- no intents found -->
  * default
  - utter_alternative_answer
  * ask_general_info
  - utter_ask_general_info
  
## flow 1-1     <!--check doctors appointment -->
  * ask_doctors_appointment
   - utter_ask_doctors_appointment
  * make_doctors_appointment
   - utter_make_doctors_appointment
  

## flow12-1              <!-- bot trigger greet  -->
* greet              
  - utter_greet  <!--health over view, Enviornmental info, checking feeling included in the action-->
  - utter_check_context
* comment_bad_symptom <!-- user utterance, in format _intent[entities] -->
  - utter_comment_bad_symptom
* ask_advice
  - utter_ask_advice
  - utter_save_clipboard
  
## flow12-2
* greet
 - utter_greet  <!--health over view, Enviornmental info, checking feeling included in the action-->
* comment_bad_symptom <!-- user utterance, in format _intent[entities] -->
 - utter_comment_bad_symptom
* ask_music
 - utter_play_music
 
 
## feeling bad path 2
* greet
 - utter_greet  <!--health over view, Enviornmental info, checking feeling included in the action-->
* comment_bad_symptom <!-- user utterance, in format _intent[entities] -->
 - utter_comment_bad_symptom
* mood_great
 - utter_happy
 
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
 * comment_bad_symptom
  - utter_comment_bad_symptom
  
## make doctors appointment
  * make_doctors_appointment
   - utter_make_doctors_appointment
  
## ask doctor
* ask_doctor
 - utter_ask_doctor

## ask_general_info
 * ask_general_info
 - utter_ask_general_info
 
## sad path 1               <!-- this is already the start of the next story -->
* greet
  - utter_greet             <!-- action of the bot to execute -->
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* mood_affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* mood_deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye
