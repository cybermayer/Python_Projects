import requests 
import datetime  
import dayandnight  # Import the custom module dayandnight

dayandnight = dayandnight.DayAndNight()  # Instantiate the DayAndNight class from the dayandnight module

# Make a GET request to fetch ISS location data
response = requests.get(url="http://api.open-notify.org/iss-now.json")

response.raise_for_status()  # Raise an HTTPError for bad responses

requested_data = response.json()  # Parse the JSON response into a Python dictionary
latitude = float(requested_data["iss_position"]["latitude"])  # Extract latitude from the response
longitude = float(requested_data["iss_position"]["longitude"])  # Extract longitude from the response

positon = (latitude, longitude)  # Create a tuple with ISS position
my_position = (float(47.429100), float(17.832670))  # Define my position as a tuple

is_daytime = dayandnight.is_daytime()  # Determine if it's daytime using the DayAndNight class

# Check if ISS coordinates are within a certain range of my position and it's nighttime
if my_position[0] <= (latitude+5) and my_position[0] >= (latitude-5) and my_position[1] <= (longitude+5) and my_position[1] >= (longitude-5) and is_daytime == False:
    print("Look at the sky!")  # Print message to look at the sky if ISS is overhead
else:
    print(f"The ISS coordinates: lat = {latitude}, lon = {longitude}")  # Print ISS coordinates if conditions are not met
