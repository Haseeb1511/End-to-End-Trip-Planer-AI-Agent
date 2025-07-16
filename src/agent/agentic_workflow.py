from langgraph.prebuilt import ToolNode,tools_condition
from langgraph.graph import StateGraph,START,END,MessagesState
from langchain_openai import ChatOpenAI

from src.prompt_library.prompts import SYSTEM_PROMPT
from src.config.model_loader import ModelLoader



from src.tools.calculator import CalculatorTool
from src.tools.currency_converion_tool import CurrencyConverterTool
from src.tools.weather_tool import WeatherInfoTool
from src.tools.place_search_tool import PlaceSearchTool
from src.exception import MyException
import sys

class GraphBuilder():

    def __init__(self,model_provider:str="groq"):
        """This methood define the TOOLS"""

        self.model_loader = ModelLoader(model_provider="groq")
        self.llm = self.model_loader.load_llm()

        self.tools = []

        self.weather_tool = WeatherInfoTool()
        self.calculator_tool = CalculatorTool()
        self.place_search_tool = PlaceSearchTool()
        self.currency_converter_tool = CurrencyConverterTool()

        self.tools.extend(self.weather_tool.weather_tool_list +
                          self.calculator_tool.calculator_tool_list +
                          self.place_search_tool.place_search_tool_list +
                          self.currency_converter_tool.currency_converter_tool_list)

        self.llm_with_tools = self.llm.bind_tools(self.tools)

        self.graph = None
        self.system_prompt = SYSTEM_PROMPT


    def agent_function(self, state: MessagesState):
        try:
            query = state["messages"]
            input = [self.system_prompt] + query
            response = self.llm_with_tools.invoke(input)
            if response is None:
                response = ["Sorry, I could not generate a response."]
            return {"messages": response}
        except Exception as e:
            raise MyException(e,sys) from e



    def build_graph(self):
        try:
            """This Methood create the graph structure"""
            graph_builder = StateGraph(MessagesState)
            graph_builder.add_node("agent",self.agent_function)
            graph_builder.add_edge(START,"agent")
            graph_builder.add_node("tools",ToolNode(tools=self.tools))
            graph_builder.add_conditional_edges("agent",tools_condition)
            graph_builder.add_edge("tools","agent")
            graph_builder.add_edge("agent",END)
            self.graph = graph_builder.compile()
            return self.graph
        except Exception as e:
            raise MyException(e,sys) from e

    def __call__(self):  # __call__ == It lets an instance of your class be called like a function
        return self.build_graph()