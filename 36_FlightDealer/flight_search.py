#region IMPORT

import requests
from flight_data import FlightData

#endregion

#region INIT

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = "*********"

#endregion

class FlightSearch:

    """<DOC

        Handles flight searching and retrieval of destination codes.

            METHODS:
                        -get_destination_code -> str
                        -check_flights -> FlightData or None

    DOC?>"""

    def get_destination_code(self, city_name: str) -> str:

        """<DOC

                Retrieves the IATA code for a given city.
    
                    PARAMETERS:
                                -city_name (str): The name of the city to get the IATA code for.
        
                    RETURNS: str: The IATA code for the given city.
                
        DOC?>"""

        #region CODE

        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        headers = {"apikey": TEQUILA_API_KEY}
        query = {"term": city_name, "location_types": "city"}
        response = requests.get(url=location_endpoint, headers=headers, params=query)
        results = response.json()["locations"]
        code = results[0]["code"]
        return code

        #endregion

    def check_flights(self, origin_city_code: str, destination_city_code: str, from_time, to_time) -> FlightData or None:

        """<DOC

                Checks for flights between two cities within a date range.

                    PARAMETERS:
                                -origin_city_code (str): The IATA code of the origin city.
                                -destination_city_code (str): The IATA code of the destination city.
                                -from_time (datetime): The start date for the search.
                                -to_time (datetime): The end date for the search.
        
                    RETURNS: FlightData or None: An instance of FlightData if a flight is found, otherwise None.
                            

        DOC?>"""

        #region CODE

        headers = {"apikey": TEQUILA_API_KEY}
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }

        response = requests.get(
            url=f"{TEQUILA_ENDPOINT}/v2/search",
            headers=headers,
            params=query,
        )

        try:
            data = response.json()["data"][0]
            
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.destination_city}: £{flight_data.price}")
        
        return flight_data

        #endregion CODE
