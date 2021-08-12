import requests

# TODO 1: give an api call to https://opentdb.com/api.php?amount=10&type=boolean

parameters = {
    'amount': '10',
    'type': 'boolean'
}
response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
question_data = response.json()["results"]
