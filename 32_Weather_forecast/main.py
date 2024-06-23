#region IMPORT

import requests  
from twilio.rest import Client 

#endregion 

account_sid = "YOUR ACCOUNT SID"  # Twilio account SID
auth_token = "YOUR AUTHORIZATION TOKEN"  # Twilio authorization token

#region INIT

API_KEY = "YOUR API KEY"  # API key for weather API
CITY = "YOUR CITY"  # City for which weather data is requested
CURRENT_WEATHER = "http://api.weatherapi.com/v1/current.json"  # Endpoint for current weather data
FORECAST_WEATHER = "http://api.weatherapi.com/v1/forecast.json"  # Endpoint for forecast weather data

parameters = {          #request parameters
    "key": API_KEY,
    "q": CITY,
    "aqi": "no",
    "hours": 12
}

#endregion

response = requests.get(url="http://api.weatherapi.com/v1/forecast.json", params=parameters)  # Make a GET request to fetch forecast weather data

response.raise_for_status()  # Raise an HTTPError for bad responses

weather_data = response.json()  # Parse the JSON response into a Python dictionary

# Loop through the forecast data to check chance of rain for the next 12 hours
for i in range(0, 12):
    chance_of_rain = weather_data["forecast"]["forecastday"][0]["hour"][i]["chance_of_rain"]
    if chance_of_rain > 40:
        umbrella = True  # Set umbrella flag to True if chance of rain is greater than 40%

# If umbrella flag is True, send a message using Twilio
if umbrella == True:
    client = Client(account_sid, auth_token)  # Instantiate Twilio Client with credentials
    message = client.messages.create(
        from_="+13158955213",  
        body="Today could be a rainy day. Don't forget the ☂️", 
        to="+3630secret" 
    )

    print(message.status) 
