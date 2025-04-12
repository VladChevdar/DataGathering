import requests
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")
CITY = 'Portland'
STATE = 'OR'
COUNTRY = 'US'

# Current weather
current_url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY},{STATE},{COUNTRY}&appid={API_KEY}&units=imperial"

# 3-day forecast
forecast_url = f"https://api.openweathermap.org/data/2.5/forecast?q={CITY},{STATE},{COUNTRY}&appid={API_KEY}&units=imperial"

current_response = requests.get(current_url).json()
is_raining_now = any('rain' in weather['main'].lower() for weather in current_response.get('weather', []))

forecast_response = requests.get(forecast_url).json()
now = datetime.utcnow()
three_days_later = now + timedelta(days=3)

is_rain_forecasted = False
for item in forecast_response.get('list', []):
    forecast_time = datetime.utcfromtimestamp(item['dt'])
    if now <= forecast_time <= three_days_later:
        if any('rain' in weather['main'].lower() for weather in item.get('weather', [])):
            is_rain_forecasted = True
            break

print("A. Is it raining in Portland, OR right now?")
print("Yes" if is_raining_now else "No")

print("B. Is it forecasted to be raining in Portland within the next three days?")
print("Yes" if is_rain_forecasted else "No")