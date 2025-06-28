
from langgraph.prebuilt import ToolNode,tools_condition
from langgraph.graph import StateGraph,START,END,MessagesState
from langchain_openai import ChatOpenAI

from prompt_library.prompts import SYSTEM_PROMPT


class Graphbuilder():
    def __init__(self):
        """This methood define the TOOLS"""
        self.tools = [

        ]
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