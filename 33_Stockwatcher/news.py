#region IMPORT

import requests
import stock
import html

#endregion 

#region INIT

API_KEY = "YOUR API KEY"
URL = 'https://newsapi.org/v2/everything'

PARAMETERS = {          #Assemble the paramstructure for requesting

    "q": "Tesla",
    "from": stock.pd,
    "sortBy": "popularity",
    "apiKey": API_KEY
}

response = requests.get(url=URL, params=PARAMETERS)
data = response.json()
news = []

#print(data["articles"][0]["url"])

#endregion

class TeslaNews:

    """<DOC

        Retrieves and provides access to Tesla-related news articles.

            METHODS:
                        -__init__ -> None
                        -get_news -> None

    DOC?>"""

    def __init__(self):

        """<DOC

            Initializes TeslaNews object.

        DOC?>"""

        pass

    def get_news(self, i: int) -> None:

        """<DOC

            Retrieves a specific Tesla-related news article URL.

                PARAMETERS:
                            - i (int): Index of the article in the fetched data.

                ATTRIBUTES:
                            -news -> str

        DOC?>"""

        #region CODE

        self.news = data["articles"][i]["url"]

        #endregion 
