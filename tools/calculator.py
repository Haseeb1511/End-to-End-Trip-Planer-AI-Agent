from config.expense_calculator import Calculator
from langchain.tools import tool



class CalculatorTool:
    def __init__(self):
        self.calculator = Calculator()
        self.calculator_tool_list = self._setup_tools()

    def _setup_tools(self)->list:
        """Setup all tools for the calculator tool"""

        @tool
        def estimate_toal_hotel_cost(price_per_night:str,total_days:float):
            """calculate total hotel cost"""
            return self.calculator.multiply(price_per_night,total_days)
        @tool
        def total_hotel_expanse(*cost:float):
            """Calculate total hotel expense"""
            return self.calculator.calculate_total()
        @tool
        def calculate_daily_hotel_expense(total:str,days:int):
            """Calculate daily budget"""       
            return self.calculator.calculate_daily_budget(total,days)
        
        return [estimate_toal_hotel_cost,total_hotel_expanse,calculate_daily_hotel_expense]



