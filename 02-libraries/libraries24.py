import requests

url = "https://api.exchangerate.host/latest"

response = requests.get(url)
precios = response.json()
print(f"1 euro son {precios['rates']['VND']} dongs vietnamitas")
