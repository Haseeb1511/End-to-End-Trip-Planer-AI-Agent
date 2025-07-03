from pydantic import BaseModel,Field
from typing import Optional,Literal,Any
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI

from utils.config_loader import load_config
from dotenv import load_dotenv
load_dotenv()



class ConfigLoader:
    def __init__(self):
        self.config = load_config()  #Load configuration file

    def __getitem__(self,key):
        self.config[key]    #we give key and get corresponsidng value from config.yaml
    


class ModelLoader(BaseModel):
    model_provider:Literal["groq","openai"] = "openai"
    config:Optional[ConfigLoader]=Field(default=None,exclude=True)

    def model_post_init(self, __context:Any):
        self.config=ConfigLoader() #we load ConfigLoader class and store in in self.config variable
    
    class Config:
        arbitrary_types_allowed = True  #Allows you to store non-primitive Python objects in your Pydantic model without validation errors.

    def load_llm(self):
        """Load nad return the llm"""
        if self.model_provider=="groq":
            print("loading model from groq")
            model_name = self.config["llm"]["groq"]["model_name"]
            llm = ChatGroq(model=model_name)

        elif self.model_provider=="openai":
            print("Loading openai llm")
            model_name = self.config["llm"]["openai"]["model_name"]
            llm = ChatOpenAI(model=model_name)

        return llm





