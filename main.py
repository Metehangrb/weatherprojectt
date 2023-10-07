import requests

city = input("Enter a city name: ")
url = "https://api.collectapi.com/weather/getWeather"
params = {
    "data.lang": "tr",
    "data.city": city
}
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'apikey 16MtrZ8stgop3a5BiiOoiJ:7hyk5wVI2e8L09DgCAdcjO'
}

response = requests.get(url, params=params, headers=headers)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print('Error fetching weather data')
