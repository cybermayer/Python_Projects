import requests
from datetime import datetime

# API credentials for Nutritionix API
API_ID = 'YOUR ID'
API_KEY = "YOUR API KEY"

# URL endpoint for Nutritionix natural exercise API
URL = "https://trackapi.nutritionix.com/v2/natural/exercise"

# User object containing user information
user_object = {
 "id": API_ID,
 "first_name": "YOUR FIRST NAME",
 "last_name": "YOUR LAST NAME"
}

# Request body containing exercise query and user details
request_body = {
 "query": "ran 3 miles",
 "gender": "male",
 "weight_kg": 85.0,
 "height_cm": 172.0,
 "age": 26
}

# Headers for Nutritionix API authentication
headers = {
 "x-app-id": API_ID,
 "x-app-key": API_KEY
}

# Make a POST request to Nutritionix API with the exercise query and transform it to dict.
response = requests.post(url=URL, json=request_body, headers=headers)
result = response.json()

# URL for Sheety API to update Google Sheets
SPREADSHEET_URL = "https://api.sheety.co/6e728c031dc6c3a8bbb7786c1ea4c8db/myWorkouts/workouts"

# Get the current date and time in the format dd/mm/yy
today = datetime.now().strftime("%d/%m/%y")
actual_time = datetime.now().strftime("%X")

# Extract exercise details from the Nutritionix API response
exercise = result["exercises"][0]["user_input"]
duration = result["exercises"][0]["duration_min"]
calories = result["exercises"][0]["nf_calories"]

# Parameters for the workout entry to be added to the Google Sheets
EXERCISE_PARAMS = {
      "workout": {
             "date": today,
             "time": actual_time,
             "exercise": exercise,
             "duration": duration,
             "calories": calories
      }
}

# Headers for Sheety API authentication
headers = {
 "Authorization": "Bearer + token"
}

# Make a POST request to Sheety API to update the Google Sheets with the workout entry
ss_response = requests.post(url=SPREADSHEET_URL, json=EXERCISE_PARAMS, headers=headers)

# Print the response from Sheety API
print(ss_response.json())
