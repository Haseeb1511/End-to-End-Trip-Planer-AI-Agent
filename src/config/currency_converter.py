import requests

class CurrencyConverter:
    def __init__(self, api_key: str):
        self.base_url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest"

    def convert(self, amount: float, from_currency: str, to_currency: str) -> float:
        """
        Convert the given amount from one currency to another currency.
        """
        url = f"{self.base_url}/{from_currency.upper()}"
        response = requests.get(url)

        if response.status_code != 200:
            raise Exception("API call failed", response.json())

        rates = response.json().get("conversion_rates")
        if not rates or to_currency.upper() not in rates:
            raise ValueError(f"Currency '{to_currency}' not found in exchange rates.")

        rate = rates[to_currency.upper()]
        return amount * rate
