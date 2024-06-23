class FlightData:

    """<DOC

        Represents flight data.

            METHODS:
                        -__init__ -> None

    DOC?>"""

    def __init__(self, price: int, origin_city: str, origin_airport: str, destination_city: str, destination_airport: str, out_date: str, return_date: str) -> None:

        """<DOC

            Initialize the FlightData object with the provided flight details.

                PARAMETERS:
                            -price (int): The price of the flight.
                            -origin_city (str): The city of origin.
                            -origin_airport (str): The airport of origin.
                            -destination_city (str): The destination city.
                            -destination_airport (str): The destination airport.
                            -out_date (str): The departure date.
                            -return_date (str): The return date.

        DOC?>"""

        self.price = price
        self.origin_city = origin_city
        self.origin_airport = origin_airport
        self.destination_city = destination_city
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date
