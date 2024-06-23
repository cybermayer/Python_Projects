#region IMPORT

from pprint import pprint
import requests

#endregion

#region INIT

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/YOUR_PATH_TO_THE_DOCUMENT"

#endregion

class DataManager:

    """<DOC

        Manages data retrieval and updating for destination information.

            METHODS:
                        -__init__ -> None
                        -get_destination_data -> dict
                        -update_destination_codes -> None

    DOC?>"""

    def __init__(self) -> None:

        """<DOC

            Initialize the DataManager object with an empty dictionary for destination data.

        DOC?>"""

        self.destination_data = {}

    def get_destination_data(self) -> dict:

        """<DOC

            Retrieves destination data from the Sheety API.

                RETURNS: dict: - The destination data.    
                    
        DOC?>"""

        #region CODE

        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

        #endregion CODE

    def update_destination_codes(self) -> None:

        """<DOC

            Updates the IATA codes for each destination in the Sheety API.

        DOC?>"""

        #region CODE

        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)

        #endregion CODE
