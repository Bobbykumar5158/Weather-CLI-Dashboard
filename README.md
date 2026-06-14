# Weather-CLI-Dashboard
ForgeTrack 2026 
6 Week skill accelerate program organized by SAE, Delhi Technological University (DTU)
Forge Track week-2 Project

# Features

* Fetch current weather data for any city
* Display:
  * Temperature
  * Humidity
  * Wind Speed
  * Weather Description

* Fetch Air Quality Index (AQI)
* Display AQI advisory messages
* Store last 5 searched cities in a JSON file
* View search history using `history` command

* Robust error handling for:
  * Invalid city names
  * Network issues
  * Missing API data
  * API failures

---

# Project Structure

Weather-CLI-Dashboard/

├── main.py

├── history_data.json

├── .env

├── .env.example

├── .gitignore

├── requirements.txt

└── README.md

---

# Installation

## Clone the Repository

```bash
git clone <your_repository_link>
```

## Open Project Folder

```bash
cd Weather-CLI-Dashboard
```

## Install Required Libraries

```bash
pip install -r requirements.txt
```

---

# API Setup

1. Create a free account on OpenWeatherMap
2. Generate your API key
3. Create a `.env` file in the project folder
4. Add your API key like this:

```env
OPENWEATHER_API_KEY=your_api_key_here
```

---

# Running the Program
Run the following command:

```bash
python main.py
```

---

# Example Usage

## Weather Search

```bash
====================== Weather & Air Quality CLI Dashboard =======================

**************************** Previously Searched City ****************************
| Italy                                                                           |

====================== Weather & Air Quality CLI Dashboard =======================
|
| What do you want to do? 
|=>Enter the city name to see current weather. 
|=>Type 'History' to see previous searched cities. 
|=>Want to exit enter 'y'
|
| Type Here :Delhi 
```

# Example Output

```bash
================================ Current Weather =================================
X ============================================================================== X
| City                : Delhi                                                    |
| Temperature (°C)    : 41.45                                                    |
| Humidity %          : 18                                                       |
| Wind_speed (Km/hr)  : 8.03                                                     |
| Description         : clear sky                                                |
| AQI                 : 3                                                        |
| AQI Status          : Moderate                                                 |
| Advisory            : Sensitive individuals should reduce outdoor activity.    |
X ============================================================================== X

```

---

# Search History
```bash
====================== Weather & Air Quality CLI Dashboard =======================
|
| What do you want to do? 
|=>Enter the city name to see current weather. 
|=>Type 'History' to see previous searched cities. 
|=>Want to exit enter 'y'
|
| Type Here : history
|
```
To view previously searched 5 City.
```bash
*************************** Previously Searched Cities ***************************
X ============================================================================== X
| City                : Goa                                                      |
| Temperature (°C)    : 26.74                                                    |
| Humidity %          : 81                                                       |
| Wind_speed (Km/hr)  : 5.76                                                     |
| Description         : scattered clouds                                         |
| AQI                 : 1                                                        |
| AQI Status          : Good                                                     |
| Advisory            : Air quality is satisfactory.                             |
X ============================================================================== X
| City                : Uttar Pradesh                                            |
| Temperature (°C)    : 40.76                                                    |
| Humidity %          : 18                                                       |
| Wind_speed (Km/hr)  : 21.35                                                    |
| Description         : clear sky                                                |
| AQI                 : 3                                                        |
| AQI Status          : Moderate                                                 |
| Advisory            : Sensitive individuals should reduce outdoor activity.    |
X ============================================================================== X
| City                : Italy                                                    |
| Temperature (°C)    : 24.44                                                    |
| Humidity %          : 89                                                       |
| Wind_speed (Km/hr)  : 4.82                                                     |
| Description         : clear sky                                                |
| AQI                 : 1                                                        |
| AQI Status          : Good                                                     |
| Advisory            : Air quality is satisfactory.                             |
X ============================================================================== X
| City                : Japan                                                    |
| Temperature (°C)    : 23.87                                                    |
| Humidity %          : 76                                                       |
| Wind_speed (Km/hr)  : 1.62                                                     |
| Description         : moderate rain                                            |
| AQI                 : 3                                                        |
| AQI Status          : Moderate                                                 |
| Advisory            : Sensitive individuals should reduce outdoor activity.    |
X ============================================================================== X
| City                : Delhi                                                    |
| Temperature (°C)    : 41.45                                                    |
| Humidity %          : 18                                                       |
| Wind_speed (Km/hr)  : 8.03                                                     |
| Description         : clear sky                                                |
| AQI                 : 3                                                        |
| AQI Status          : Moderate                                                 |
| Advisory            : Sensitive individuals should reduce outdoor activity.    |
X ============================================================================== X
```
---

# Error Handling

This project handles:

* Invalid city names
* Internet connection failures
* Missing JSON fields
* Unexpected errors

without crashing the program.

---

# Learning Outcomes

This project helped practice:

* REST APIs
* JSON parsing
* Python dictionaries and lists
* File handling
* Exception handling
* Environment variables
* Working with real-world API data

---

# API Used

OpenWeatherMap API:
https://openweathermap.org/api

---

# Submission Requirements Covered

* Weather Data
* AQI Data
* Search History
* Error Handling
* `.env` Security
* `.env.example`
* GitHub Repository
* README Documentation

---