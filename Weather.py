import requests
import plyer
from plyer import notification
import json

Current_City=input("Enter the city name: ")
api_key = "43f4d90b448573ffd02979d5b34695cb"
url = f"http://api.openweathermap.org/data/2.5/weather?q={Current_City}&appid={api_key}&units=metric"
response=requests.get(url)
data=response.json()
if data["cod"] == 200:
    temp = data["main"]["temp"]
    desc = data["weather"][0]["description"]

    # 7. Create the message
    weather_message = f"Current Temp: {temp}°C\nCondition: {desc.title()}"

    notification.notify(
         title=f"Weather in {Current_City.title()} 🌦",
        message=weather_message,
        timeout=10
    )
else:
    print("City not found. Please check the name and try again.")
