from langchain.tools import tool
from dotenv import load_dotenv
load_dotenv()
import os
from langchain_community.utilities.alpha_vantage import AlphaVantageAPIWrapper



@tool
def multiply(a:int,b:int)->int:
    """This Function multiply two integer"""
    return a*b

@tool
def add(a:int,b:int)->int:
    """This tool add two integer"""
    return a+b



#Alpha Vantage Alpha Vantage provides realtime and historical financial market data through a set of powerful and developer-friendly data APIs and spreadsheets.
@tool
def currency_converter(from_currency:str,to_currency:str,value:float)->float:
    os.getenv["ALPHAVANTAGE_API_KEY"] = os.getenv("ALPHAVANTAGE_API_KEY")
    alpha_vantage = AlphaVantageAPIWrapper()
    response = alpha_vantage._get_exchange_rate(from_currency=from_currency,to_currency=to_currency)
    exchange_rate = exchange_rate["Realtime Currency Exchange Rate"]["From_Currency Code"]
    return value*float(exchange_rate)  # To get desired value in the required currency
    