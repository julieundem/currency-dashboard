import requests

URL = "https://openexchangerates.org/api/latest.json"
params = {
    "app_id" : "39ed09df88944c8687ca648c527d3705",
    "symbols" : "EUR,GBP,CNY,AUD,AED,CAD,ILS,INR,MXN,KRW,JPY,ZAR,BRL,PEN,SSP"

    }

# make request
response = requests.get(URL,params=params)

# turn into json
response.raise_for_status()
data = response.json()

# print useful pieces

print(data["base"])
print(data["timestamp"])
print(data["rates"]["EUR"])
print(data["rates"]["GBP"])
print(len(data["rates"]))