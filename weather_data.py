import requests
import json

# OpenWeatherMap API endpoint and API key
api_endpoint = "https://api.openweathermap.org/data/2.5/weather"
api_key = "a94674834395ff8b8aa7cddee69ef429"  # Replace 'YOUR_API_KEY' with your actual API key

# Parameters for the API request (coordinates of Prague)
params = {
    "q": "Prague,CZ",  # City name and country code
    "appid": api_key,  # API key
    "units": "metric"  # Units for temperature (metric for Celsius)
}

# Send GET request to OpenWeatherMap API
response = requests.get(api_endpoint, params=params)

# Check if request was successful (status code 200)
if response.status_code == 200:
    # Parse JSON response
    data = response.json()

    # Extract relevant data
    relevant_data = {
        "city": data["name"],
        "country": data["sys"]["country"],
        "temperature": data["main"]["temp"],
        "weather_description": data["weather"][0]["description"]
    }

    # Print extracted data
    print("Extracted Data:")
    print(json.dumps(relevant_data, indent=4))

    # Save extracted data to a JSON file
    with open("weather_data.json", "w") as json_file:
        json.dump(relevant_data, json_file, indent=4)

    print("Weather data saved to 'weather_data.json' file.")
else:
    print("Failed to retrieve weather data. Status code:", response.status_code)
