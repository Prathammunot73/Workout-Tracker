import requests
from datetime import datetime

WEIGHT_KG=14
HEIGHT_CM=160
AGE=21
GENDER="male"

APP_ID="app_e1ac6a8dc0a940b9bd06af51"
API_KEY="nix_live_b3zbOvbFXxXzeYH35YJxBAIWMUUYIfwJ"

exercise_endpoint="https://app.100daysofpython.dev/v1/nutrition/natural/exercise"
sheet_endpoint="https://api.sheety.co/fa179106036defe96a8eafa0f261bfec/workoutTracking/workouts"

exercise_text=input("Which exercise you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters={
    "query":exercise_text,
    "weight_kg":WEIGHT_KG,
    "height_cm":HEIGHT_CM,
    "age":AGE,
    "gender":GENDER
}

response=requests.post(url=exercise_endpoint,json=parameters,headers=headers)
result=response.json()
print(result)

today=datetime.now().strftime("%d/%m/%Y")
now_time=datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs={
        "workout":{
            "date":today,
            "time":now_time,
            "exercise":exercise["name"].title(),
            "duration":exercise["duration_min"],
            "calories":exercise["nf_calories"]
        }
    }

    sheet_response=requests.post(sheet_endpoint,json=sheet_inputs)
    print(sheet_response.text)