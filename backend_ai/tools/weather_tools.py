import os
import requests
from tools.base_tools import BaseTool


class WeatherTool(BaseTool):
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


    def get_weather(self, city: str):
        api_key = os.getenv("WEATHER_API_KEY")


        def call():
            r = requests.get(self.BASE_URL, params={
                "q": city,
                "appid": api_key,
                "units": "metric"
            })
            r.raise_for_status()
            data = r.json()
            return {
                "city": city,
                "temperature": f"{data['main']['temp']}°C",
                "condition": data['weather'][0]['description']
            }

        return self.retry(call) 