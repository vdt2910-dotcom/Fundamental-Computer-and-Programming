import requests

api_key = "fd73335f50f466c79df40bb3e9d7dbae"

city = input("Enter municipality name: ")

geo_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={api_key}"

geo_response = requests.get(geo_url)
geo_data = geo_response.json()

if isinstance(geo_data, list) and len(geo_data) > 0:
    lat = geo_data[0]["lat"]
    lon = geo_data[0]["lon"]

    weather_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "lat": lat,
        "lon": lon,
        "appid": api_key,
        "units": "metric"
    }

    weather_response = requests.get(weather_url)
    weather_data = weather_response.json()

    if "weather" in weather_data and "main" in weather_data:
        description = weather_data["weather"][0]["description"]
        temperature = weather_data["main"]["temp"]

        print("Weather:", description)
        print("Temperature:", temperature, "°C")
    else:
        print("Error getting weather data:")
        print(weather_data)

else:
    print("City not found or API error.")
    print("Response:", geo_data)