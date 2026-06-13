import os
from dotenv import load_dotenv
import json
import requests

load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

def fetchData(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    try :
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()

            weather_data = {
                "city": data.get("name"),
                "temp": data["main"]["temp"],
                "humidity": data["main"]["humidity"],
                "wind_speed": data["wind"]["speed"],
                "description": data["weather"][0]["description"],
                "lat": data["coord"]["lat"],
                "lon": data["coord"]["lon"]
            }

            return weather_data
            
        elif response.status_code == 404:
            print(f"Error: City '{city}' not found. Please check the spelling.")
            return None
        else:
            print(f"API Error: Status code {response.status_code}")
            return None
            
    except requests.exceptions.ConnectionError:
        print("Network Error: Could not connect to the internet.")
        return None
