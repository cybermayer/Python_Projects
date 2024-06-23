#Import necessary modules and classes
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

#Initializing objects
data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

#Initializing the constants and variabels
ORIGIN_CITY_IATA = "IATA OF YOUR CITY"
sheet_data = data_manager.get_destination_data()

#Data management
if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

#Define the search window: from tomorrow + 6Months
tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

#Iterate over each destination in the sheet data
for destination in sheet_data:
    #Check for flights to the destination within the search window
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    #If a flight were found with a price lower than our specified preferences:
    if flight.price < destination["lowestPrice"]:
        #Send an SMS notification with the flight details
        notification_manager.send_sms(
            message=f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
        )
