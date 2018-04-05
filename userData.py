import pymongo
from pymongo import MongoClient

client = MongoClient('localhost',27017)
db = client.user_database
user_insert = db.user_data

user_data = {
  "_id": 1,
  "user_info" : {
    "email" : "grace_silvia@gmail.com",
    "user_name" : "silvia",
    "birthday" : "1982-03-14",
    "gender" : "female",
    "dudate" : "2018-05-21",
    "height" : 163,
    "start_weight" : 58.4,
    "address" : "seoul",
    "job" : "working_mom",
    "multiparity" : 0
    },
    "health_info" : {
      "trimester" : "third",
      "weeks" : 34,
      "weight" : 71,
      "weight_device_id" : "TNT01S",
      "weight_date" : "2018-02-20 07:00:00",
      "blood_pressure_device_id" : "BP2017",
      "blood_pressure_high" : 138,
      "blood_pressure_low" : 60,
      "blood_pressure_date" : "2018-04-03 20:33:00",
      "bloom_device_id" : "BM2017",
      "bloom" : "regular",
      "bloom_date" : "2018-04-03 20:00:00"
    },
    "chat_info" : {
      "trimester" : "",
      "weeks" : "",
      "weight" : "",
      "blood_pressure_high" : "",
      "blood_pressure_low" : "",
      "mood_date" : "2018-04-04 08:30:00",
      "mood" : 0,
      "symptoms" : [
        { "name" : "hip_pain",
          "severity" : "medium",
          "frequency" : 4,
          "context" : "hypertension diagmosis"
        }
      ]
    },
    "service" : {
      "music" : "active",
      "book_list" : "All about pregnancy",
      "commerce" : [{
       "item" : "patch",
       "purchase_date" : "2018-01-17"
      }]
   },
   "schedule" : {
     "appointment" : [
       {
         "doctor_name" : "Dr.Brown",
         "date" : "2018-02-21 10:00:00"
       }
     ],
     "trigger" : {
       "wakeup_time" : "07:00:00",
       "sleep_time" : "23:00:00"
     }
   },
   "clipboard" : {
     "date" : "",
     "contents" : ""
   }
  
}
print('db insert start...')
user_insert.remove()
user_insert.insert(user_data)
print('db insert finish...')
