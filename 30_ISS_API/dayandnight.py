#region IMPORT

import requests
import datetime

#endregion 

#region INIT

# Get current time
current_time = datetime.datetime.now()

# Define my position
my_position = (47.429100, 17.832670)

# Define parameters for API request
requested_parameters = {
    "lat": my_position[0],
    "lng": my_position[1],
    "formatted": 0
}

# Make request to sunrise-sunset API
response = requests.get(url="https://api.sunrise-sunset.org/json", params=requested_parameters)

# Convert API response to dictionary
sunrise_sunset_dict = response.json()

# Extract sunrise and sunset times from API response
sunset = sunrise_sunset_dict["results"]["sunset"]
sunrise = sunrise_sunset_dict["results"]["sunrise"]

# Extract hours from sunrise and sunset times
sunrise_hour_str = sunrise.split("T")[1].split(":")[0]
sunset_hour_str = sunset.split("T")[1].split(":")[0]

# Convert hour strings to integers
if sunrise_hour_str[0] == "0":
    sunrise_hour = int(sunrise_hour_str[1])
else:
    sunrise_hour = int(sunrise_hour_str)

if sunset_hour_str[0] == "0":
    sunset_hour = int(sunset_hour_str[1])
else:
    sunset_hour = int(sunset_hour_str)

# Determine current hour
current_hour = current_time.hour

#endregion

class DayAndNight:

    """<DOC

        Represents the day and night testing mechanism based on the geolocation.

            METHODS: 
                    -__init__ -> None
                    -is_daytime -> bool

    DOC?>"""

    def __init__(self):

        """<DOC

            Initialize the DayAndNight object.

        DOC?>"""

        #region CODE

        pass
    
        #endregion 

    def is_daytime(self) -> bool:

        """<DOC
        
            Check if it is daytime based on current time, sunrise, and sunset.

                RETURN: bool depends on the daylight

        DOC?>"""

        #region CODE

        if current_hour > sunrise_hour and current_hour < sunset_hour:
            is_daytime = True
        else:
            is_daytime = False
        
        return is_daytime
    
        #endregion
