import requests
import config

api_key = config.API_KEY_Task1

base_currency, target_currency = map(
    str, input("Введите основную и целевую валюты: ").split()
)
amount = int(input("Введите номинал: "))
url = f"https://api.freecurrencyapi.com/v1/latest?apikey={api_key}&base_currency={base_currency}&currencies={target_currency}"

response = requests.get(url)

info = response.json()

if info["data"] and info["data"][target_currency]:
    converted = amount * info["data"][target_currency]
    print(f"{amount} {base_currency} составляют {converted:.2f} {target_currency}")
else:
    print("Указанная валюта не найдена")
