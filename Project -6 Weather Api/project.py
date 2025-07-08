import requests

API_KEY = "8753ed0174f3ba1d882ef9248decfbf8"
BASE_URL = "http://api.weatherstack.com/current"

def get_weather(city_name):
    params = {
        'access_key': API_KEY,
        'query': city_name
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()

        if "current" in data:
            location = data['location']['name']
            temp = data['current']['temperature']
            humidity = data['current']['humidity']
            description = data['current']['weather_descriptions'][0]

            print(f"\nWeather in {location}:")
            print(f"Temperature: {temp}°C")
            print(f"Humidity: {humidity}%")
            print(f"Condition: {description}")
        else:
            print("City not found or invalid API response.")
    else:
        print("Failed to fetch data from weatherstack.")

def main():
    print("== Weather App ==")
    city = input("Enter city name: ")
    get_weather(city)

main()
