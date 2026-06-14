import os
from dotenv import load_dotenv
import json
import requests

load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")
FILE = "history_data.json"

def fetchWeather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    try :
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()

            weather_data = {
                "City": data.get("name"),
                "Temperature (°C)": data["main"]["temp"],
                "Humidity %": data["main"]["humidity"],
                # converting m/s to km/hr
                "Wind_speed (Km/hr)": (data["wind"]["speed"])*3.6,
                "Description": data["weather"][0]["description"],
                "lat": data["coord"]["lat"],
                "lon": data["coord"]["lon"]
            }

            return weather_data
            
        elif response.status_code == 404:
            print(f"| ***Error: City '{city}' not found. Please check the spelling.***")
            return None
        else:
            print(f"API Error: Status code {response.status_code}")
            return None
            
    except requests.exceptions.ConnectionError:
        print("Network Error: Could not connect to the internet.")
        return None

def fetchAQI(lat,lon):
    url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={API_KEY}"
    try :
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data["list"][0]["main"]["aqi"])
        else:
            print(f"API Error: Status code {response.status_code}")
            return None
            
    except requests.exceptions.ConnectionError:
        print("Network Error: Could not connect to the internet.")
        return None

def fetchData(city):
    weather_data = fetchWeather(city)
    if not (weather_data is None):
        aqi = fetchAQI(weather_data["lat"],weather_data["lon"])
        aqi_status = ["Good", "Fair", "Moderate", "Poor", "Very Poor"]
        advisory = [
                    'Air quality is satisfactory.', 
                    'Air quality is acceptable.', 
                    'Sensitive individuals should reduce outdoor activity.', 
                    'Avoid prolonged outdoor exertion.', 
                    'Stay indoors if possible.'
                    ]
    
        weather_data["AQI"]=aqi
        weather_data["AQI Status"]=aqi_status[aqi-1]
        weather_data["Advisory"] = advisory[aqi-1]
        return weather_data
    else:
        return None

def historyData(FILE):
    if os.path.exists(FILE):
        try:
            with open(FILE, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return []
    return []

def saveHistory(FILE,weather_data):
    history = historyData(FILE)

    history.append(weather_data)
    history = history[-5:]

    with open(FILE, "w") as file:
       json.dump(history,file,indent=3)

def display(data):
    print("X","="*78,"X")
    for obj in data:
        for key in obj:
            if key != "lat" and key != "lon":
                if isinstance(obj[key], float):
                    str = f"| {key:<20}: {obj[key]:.2f}"
                    print(f"{str:<80} |")
                else:
                    str = f"| {key:<20}: {obj[key]}"
                    print(f"{str:<80} |")
        print("X","="*78,"X")

def main():
    print(f"\n{' Weather & Air Quality CLI Dashboard ':=^82}\n")
    if historyData(FILE):
        print(f"{' Previously Searched City ':*^82}")
        print(f"| {historyData(FILE)[-1]['City']:<80}|")
    else:
        print(f"{' Previous Searched City ':*^82}")
        print(f"{' NO PREVIOUS DATA ':*^82}")

    while True:
        print(f"\n{' Weather & Air Quality CLI Dashboard ':=^82}\n|")
        print("| What do you want to do? \n|=>Enter the city name to see current weather. \n|=>Type 'History' to see previous searched cities. \n|=>Want to exit enter 'y'\n|")
        
        choice = input("| Type Here : ").lower().strip()
        print("|")

        if choice == "history":
            if historyData(FILE):
                print(f"{' Previously Searched Cities ':*^82}")
                display(historyData(FILE))
            else:
                print(f"{' Previously Searched Cities':*^82}")
                print(f"{' NO PREVIOUS DATA ':*^82}")
        elif choice == "y":
            break
        else:
            data = fetchData(choice)
            if not(data is None):
                print(f"{' Current Weather ':=^82}")
                display([fetchData(choice)])
                saveHistory(FILE,fetchData(choice))
if __name__=="__main__":
    main()