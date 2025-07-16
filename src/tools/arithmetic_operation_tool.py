from langchain.tools import tool
import os,sys
from langchain_community.utilities.alpha_vantage import AlphaVantageAPIWrapper
from src.exception import MyException

from pathlib import Path
from dotenv import load_dotenv
env_path = Path(__file__).resolve().parents[1] / ".env"
load_dotenv(dotenv_path=env_path)

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
    try:
        os.getenv["ALPHAVANTAGE_API_KEY"] = os.getenv("ALPHAVANTAGE_API_KEY")
        alpha_vantage = AlphaVantageAPIWrapper()
        response = alpha_vantage._get_exchange_rate(from_currency=from_currency,to_currency=to_currency)
        exchange_rate = exchange_rate["Realtime Currency Exchange Rate"]["From_Currency Code"]
        return value*float(exchange_rate)  # To get desired value in the required currency
    except Exception as e:
        raise MyException(e,sys) from e