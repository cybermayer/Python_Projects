#Data fetching file

import requests

parameters = {
    
    "amount": 4098,
    "type": "boolean"

}

response = requests.get(url="https://opentdb.com/api.php", params=parameters)

response.raise_for_status()

data = response.json()

question_data = data["results"]



