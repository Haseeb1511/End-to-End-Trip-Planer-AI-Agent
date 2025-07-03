from typing import Any,Dict,List,TypedDict
import os
from dotenv import load_dotenv
load_dotenv()
from langchain.tools import tool

from config.weather import WeatherForecastTool




class WeatherInfoTool:

    def __init__(self):
        self.api_key = os.getenv("OPENWEATHER_API_KEY")
        self.weather_service = WeatherForecastTool(self.api_key)
        self.weather_tool_list = self._setup_tools()

    def _setup_tools(self):
        """Setup all tool for weather forcast tool"""
        @tool
        def get_current_weather(city:str)->str:
            """Get current weather for a Given City"""
            weather_data = self.weather_service.get_current_weather(city)
            if weather_data:
                temp = weather_data.get('main', {}).get('temp', 'N/A') #Get tempreature of city
                desc = weather_data.get('weather', [{}])[0].get('description', 'N/A') #Get descritption 
                return f"Current weather in {city}: {temp}°C, {desc}"
            return f"Could not fetch weather for {city}"
        
        @tool
        def get_weather_forecast(city:str)->str:
            """Get weather forecast for City"""
            forecast_data = self.weather_service.get_forecast_weather(city)
            if forecast_data and "list" in forecast_data:
                forecast_summary  = []
                for i in range(len(forecast_data["list"])):
                    item = forecast_data['list'][i]
                    date = item['dt_txt'].split(' ')[0]
                    temp = item['main']['temp']
                    desc = item['weather'][0]['description']
                    forecast_summary.append(f"{date}: {temp} degree celcius , {desc}")
                return f"Weather forecast for {city}:\n" + "\n".join(forecast_summary)
            return f"Could not fetch forecast for {city}"
    
        return [get_current_weather, get_weather_forecast]