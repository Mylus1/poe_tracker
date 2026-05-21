import requests
import poe_tracker.poe_tracker.urls as urls
from pprint import pprint

url = urls.Currency

response = requests.get(url)
response.raise_for_status()  # Check if the request was successful
data = response.json()

for currency in data.get("lines", []):
    print(f"{currency['id']}: {currency['primaryValue']} chaos")