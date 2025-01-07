import urllib.request, urllib.error, urllib.parse
import json
from datetime import datetime

api_key = "fa07f03ac7822f26f40d5bb67daf3d3c"
weather_url = "http://api.openweathermap.org/data/2.5/forecast?"

city = input("Enter the name of the city: ")
start_date = input("Enter the start date (YYYY-MM-DD): ")
end_date = input("Enter the end date (YYYY-MM-DD): ")

parsed_url = f"{weather_url}q={city}&appid={api_key}&units=metric"

try:
    response = urllib.request.urlopen(parsed_url)
    weather_data = json.load(response)
    print(f"Weather forecast of {city} from {start_date} to {end_date}")
    for forecast in weather_data['list']:
        forecast_date = forecast['dt_txt']
        forecast_datetime = datetime.strptime(forecast_date, '%Y-%m-%d %H:%M:%S')
        start_datetime = datetime.strptime(start_date, '%Y-%m-%d')
        end_datetime = datetime.strptime(end_date, '%Y-%m-%d')

        if start_datetime <= forecast_datetime <= end_datetime:
            temp = forecast['main']['temp']
            description = forecast['weather'][0]['description']
            print(f"Date: {forecast_date} | Temperature: {temp}°C | Description: {description}")

except urllib.error.URLError as e:
    print(f"An HTTP error occurred: {e.reason}")
except Exception as e:
    print(f"An error: {e}")
