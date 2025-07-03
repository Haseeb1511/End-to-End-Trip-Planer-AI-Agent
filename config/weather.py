import os
from dotenv import  load_dotenv
load_dotenv()

import requests

class WeatherForecastTool:
    
    def __init__(self,api_key):
        self.api_key = os.getenv("OPENWEATHER_API_K")
        self.base_url  = "https://api.openweathermap.org/data/2.5"

    def get_current_weather(self,place:str):
        try:
            url = f"{self.base_url}/weather"
            param = {"q":place,
                    "appid":self.api_key}
            response = requests.get(url=url,params=param)
            return response.json() if response.status_code==200 else {}
        except Exception as e:
            print(f"An error occured while connecting with weather api :{e}")     


    def get_forecast_weather(self,place:str):
        try:
            url = f"{self.base_url}/forecast"
            param = {"q":place,
                    "appid":self.api_key,
                    "cnt":10,
                    "units":"metric"}
            response = requests.get(url=url,params=param)
            return response.json() if response.status_code==200 else {}
        except Exception as e:
            print(f"An error occured while connecting with weather api :{e}") 

