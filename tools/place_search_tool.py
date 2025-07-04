from config.place_info_search import GooglePlaceSearchTool,TavilySearchTool
from dotenv import load_dotenv
load_dotenv()
import os
from langchain.tools import tool


class PlaceSearchTool:

    def __init__(self):
        self.google_api_key = os.environ.get("GPLACES_API_KEY")
        self.google_place_search = GooglePlaceSearchTool(api_key=self.google_api_key)
        self.tavily_place_search = TavilySearchTool()
        self.place_search_tool_list = self._setup_tools()

    def _setup_tools(self) ->list:
        """Setup all tools for the place search tool"""

        @tool
        def search_attraction(place:str):
            """Search attractions of a place"""
            try:
                attraction_result = self.google_place_search.google_search_attraction(place)
                if attraction_result:
                    return f"Top attractive places in and arround {place} as suggested bu google: {attraction_result}"
            except Exception as e:
                tavily_result = self.tavily_place_search.tavily_search_attraction(place)
                return f"goolge can not find the result \nfollowing are the attraction of {place} : {tavily_result}"
            
        @tool
        def search_resturent(place:str):
            """Search restaurants of a place"""
            try:
                resturent_result = self.google_place_search.google_search_resturent(place)
                if resturent_result:
                    return f"Following are the restaurants of {place} as suggested by google: {resturent_result}"
            except Exception as e:
                tavily_result = self.tavily_place_search.tavily_search_restaurants(place)
                return f"Google cannot find the details due to {e}. \nFollowing are the restaurants of {place}: {tavily_result}"
            

        @tool
        def search_activity(place:str):
            """Search activities of a place"""
            try:
                activity_result = self.google_place_search.google_search_activity(place)
                if activity_result:
                    return f"Following are the activities in and around {place} as suggested by google: {activity_result}"
            except Exception as e:
                tavily_result = self.tavily_search.tavily_search_activity(place)
                return f"Google cannot find the details due to {e}. \nFollowing are the activities of {place}: {tavily_result}"
            
        @tool
        def search_transportation(place:str):
            """Search transportation of a place"""
            try:
                transportation_result = self.google_place_search.google_search_transportation(place)
                if transportation_result:
                    return f"Following are the modes of transportation available in {place} as suggested by google: {transportation_result}"
            except Exception as e:
                tavily_result = self.tavily_search.tavily_search_transportation(place)
                return f"Google cannot find the details due to {e}. \nFollowing are the modes of transportation available in {place}: {tavily_result}"  
        
        return [search_activity,search_attraction,search_resturent,search_transportation]

        
