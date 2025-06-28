
from langgraph.prebuilt import ToolNode,tools_condition
from langgraph.graph import StateGraph,START,END,MessagesState
from langchain_openai import ChatOpenAI

from prompt_library.prompts import SYSTEM_PROMPT
from utils.model_loader import ModelLoader

from tools.calculator import
from tools.currency_converion_tool import
from tools.weather_tool import WeatherInfoTool
from tools.place_search_tool import


class Graphbuilder():

    def __init__(self,model_provider:str="groq"):
        """This methood define the TOOLS"""

        self.model_loader = ModelLoader(model_provider="openai")
        self.llm = self.model_loader.load_llm()

        self.tools = []

        self.weather_tool = WeatherInfoTool()
        self.calculator_tool = 
        self.place_search_tool = 
        self.currency_converter_tool = 

        self.tools.extend()

        self.tools = ([
 
        ])
        self.llm_With_tools = self.llm.bind_tools(self.tools)

        self.graph = None
        self.system_prompt = SYSTEM_PROMPT  #we use self.variable_name ==only when we need to later use them in another methood


    def agent_funtion(self,state:MessagesState):
        """This Methood define the agent(model) functionality"""
        query = state["messages"]
        input = [self.system_prompt]+query
        response = self.llm_with_tools.invoke(input)
        return {"messages":response}


    def build_graph(self):
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

    def __call__(self):  # __call__ == It lets an instance of your class be called like a function
        return self.build_graph()