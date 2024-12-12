import requests
import os

# -----------------NUTRI API-----------------
#
# NUTRI_KEY = "175763ce993f2441ef17d1d380b44246"
# NUTRI_ID = "04fd0f4f"
# NUTRI_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
# query = "running"
# WEIGHT = 63
# HEIGHT = 178
# AGE = 33
#
# nutri_header = {
#     "x-app-id": NUTRI_ID,
#     "x-app-key": NUTRI_KEY,
# }
#
# nutri_params = {
#     "query": query,
#     "weight_kg": WEIGHT,
#     "height_cm": HEIGHT,
#     "age": AGE,
# }
#
# nutri_response = requests.post(url=NUTRI_ENDPOINT, json=nutri_params, headers=nutri_header)
# nutri_response.raise_for_status()
# data = nutri_response.json()
# print(nutri_response, data)


# -----------------SHEETY API-----------------

BEARER_TOKEN = os.environ["BEARER_TOKEN"]
SHEETY_ENDPOINT = os.environ["SHEETY_ENDPOINT"]
print(SHEETY_ENDPOINT)
print(BEARER_TOKEN)

date = input("An welchem Datum: ")
ausgabe = input("Was war der Grund für die Ausgabe?: ")
betrag = float(input("Wie hoch war der Betrag? (ohne €): "))

sheety_header = {
    "Authorization": f"Bearer {BEARER_TOKEN}",
}

sheety_body = {
    "2024": {
        "datum": date,
        "ausgabe": ausgabe,
        "betragInEuro": betrag
    }
}

sheety_response = requests.post(url=SHEETY_ENDPOINT, json=sheety_body, headers=sheety_header)
sheety_response.raise_for_status()
print(sheety_response.json())
print(sheety_response.status_code)