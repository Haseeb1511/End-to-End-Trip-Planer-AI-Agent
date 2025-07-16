from langchain_tavily import TavilySearch
import os,sys
from langchain_google_community import GooglePlacesAPIWrapper,GooglePlacesTool

class GooglePlaceSearchTool:

    def __init__(self,api_key):
        self.place_wrapper = GooglePlacesAPIWrapper(gplaces_api_key=api_key)
        self.place_tool = GooglePlacesTool(api_wrapper=self.place_wrapper)

    def google_search_attraction(self,place:str)->dict:
        """Searches for attractive place in the specified places using GooldePlace API"""
        return self.place_tool.run(f"Top attractive places in and arround {place}")
    
    def google_search_resturent(self,place:str)->dict:
        """Searches for avaliable Resturnet in the specified places using GooldePlace API"""
        return self.place_tool.run(f"what are the top 7 returnet and eater in and arround {place}")
    
    def google_search_activity(self,place:str)->dict:
        """Searches for popular activities in the specified place using GooglePlaces API."""
        return self.place_tool.run(f"Activities in and around {place}")
    
    def google_search_transportation(self,place:str):
        """Searches for available modes of transportation in the specified place using GooglePlaces API."""
        return self.places_tool.run(f"What are the different modes of transportations available in {place}")
    

class TavilySearchTool:
    def __init__(self):
        pass

    def tavily_search_attraction(self,place:str):
        """Searches for attractive place in the specified places using TavilySearch API"""
        tavily_tool = TavilySearch(topic="general",include_answer="advanced")
        result = tavily_tool.invoke({"query":f"Top attractive places in and arround {place}"})
        if isinstance(result,dict) and result.get("answer"):
            return result["answer"]
        return result
    
    def tavily_search_restaurants(self, place: str) -> dict:
        """Searches for available restaurants in the specified place using TavilySearch."""
        tavily_tool = TavilySearch(topic="general", include_answer="advanced")
        result = tavily_tool.invoke({"query":f"what are the top 7 returnet and eater in and arround {place}"})
        if isinstance(result,dict) and result.get("answer"):
            result["answer"]
        return result
    
    def tavily_search_activity(self, place: str) -> dict:
        """Searches for popular activities in the specified place using TavilySearch."""
        tavily_tool = TavilySearch(topic="general", include_answer="advanced")
        result = tavily_tool.invoke({"query": f"activities in and around {place}"})
        if isinstance(result,dict) and result.get("answer"):
            return result["answer"]
        return result
    
    def tavily_search_transportation(self, place: str) -> dict:
        """Searches for available modes of transportation in the specified place using TavilySearch."""
        tavily_tool = TavilySearch(topic="general", include_answer="advanced")
        result = tavily_tool.invoke({"query": f"What are the different modes of transportations available in {place}"})
        if isinstance(result, dict) and result.get("answer"):
            return result["answer"]
        return result


