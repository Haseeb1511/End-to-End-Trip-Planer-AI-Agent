import os
from src.config.currency_converter import CurrencyConverter
from langchain.tools import tool

from pathlib import Path
from dotenv import load_dotenv
env_path = Path(__file__).resolve().parents[1] / ".env"
load_dotenv(dotenv_path=env_path)


class CurrencyConverterTool:
    def __init__(self):
        self.api_key = os.getenv("EXCHANGE_RATE_API_KEY")
        self.currency_converter = CurrencyConverter(self.api_key)
        self.currency_converter_tool_list = self._setup_tool()

    def _setup_tool(self)->list:

        """Setup all tools for the currency converter tool"""
        @tool
        def convert_currency(amount: float, from_currency: str, to_currency: str):
            """Convert amount from one currency to another"""
            return self.currency_converter.convert(amount,from_currency,to_currency)
        return [convert_currency]
