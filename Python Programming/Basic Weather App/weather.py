import requests

def get_weather(city_name):
    api_key = "" 
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": city_name, "appid": api_key, "units": "metric"}

    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        
        if data["cod"] == 200:
            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            weather_description = data["weather"][0]["description"]
            print(f"Weather in {city_name}:")
            print(f"Temperature: {temperature}°C")
            print(f"Humidity: {humidity}%")
            print(f"Description: {weather_description}")
        else:
            print("City not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def main():
    print("Welcome to the Weather App!")
    city_name = input("Enter the city name: ")
    get_weather(city_name)

if __name__ == "__main__":
    main()
