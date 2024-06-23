#region IMPORT

import requests
import datetime

#endregion

#region INIT

API = "AHLMBP5MLWKVKJO"
URL = 'https://www.alphavantage.co/query'

PARAMETERS = {
    "function": "TIME_SERIES_INTRADAY",
    "symbol": "TSLA",
    "interval": "60min",
    "apikey": API
}


#Initalizing date-parts
now = str(datetime.datetime.today() - datetime.timedelta(days=1))
yester = str(datetime.datetime.today() - datetime.timedelta(days=2))
previous = str(datetime.datetime.today() - datetime.timedelta(days=3))

current_month = now[5:7]
current_day = now[8:10]
cd = now[0:10]

yester_month = yester[5:7]
yester_day = yester[8:10]
yd = yester[0:10]

previous_month = previous[5:7]
previous_day = previous[8:10]
pd = previous[0:10]

#endregion 

class StockAPI:

    """<DOC

            Provides methods to interact with the Alpha Vantage API for stock data retrieval.
    
                METHODS:
                            -__init__ -> None
                            -get_response -> tuple

    DOC?>"""

    def __init__(self):

        """<DOC

            Initializes StockAPI with constants and placeholders for API data.

        DOC?>"""

        pass

    def get_response(self) -> tuple:

        """<DOC

            Retrieves data from the Alpha Vantage API and extracts relevant stock information.

                ATTRIBUTES:

                        -response -> the requested stock datas
                        -data -> dict from requested datas formated to JSON
                        -cd -> str currentday
                        -yd -> str yesterday
                        -pd -> str day before yesterday
                        -today_open -> float today open price
                        -yesterday_close -> float yesterday closing price
                        -previous_close -> float before yesterday price


                RETURNS:
                        - tuple: A tuple containing today's opening price, yesterday's closing price, and the day before yesterday's closing price.

        DOC?>"""

        #region CODE

        self.response = requests.get(url=URL, params=PARAMETERS)
        self.data = self.response.json()
        self.cd = cd
        self.yd = yd
        self.pd = pd
        self.today_open = float(self.data["Time Series (60min)"][f'{cd} 07:00:00']['1. open'])
        self.yesterday_close = float(self.data["Time Series (60min)"][f'{yd} 19:00:00']['4. close'])
        self.previous_close = float(self.data["Time Series (60min)"][f'{pd} 19:00:00']['4. close'])

        return (self.today_open, self.yesterday_close, self.previous_close)
    
        #endregion

    
