from pydantic import BaseModel,Field
from typing import Optional,Literal,Any
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI

from src.exception import MyException
import sys
import os
from src.config.config_loader import load_config
from dotenv import load_dotenv
from pathlib import Path

#load .env from root folder
env_path = Path(__file__).resolve().parents[1] / ".env"
load_dotenv(dotenv_path=env_path)

#Path(__file__).resolve() gets the full absolute path of your Python file
#t builds a full path to .env → loads it → your env vars are se

groq_api = os.getenv("GROQ_API_KEY")
openai_api = os.getenv("OPENAI_API_KEY")

class ConfigLoader:
    def __init__(self):
        self.config = load_config()  #Load configuration file

    def __getitem__(self,key):
        return self.config[key]    #we give key and get corresponsidng value from config.yaml        Properly returns the value
    

class ModelLoader(BaseModel):
    model_provider:Literal["groq","openai"] = "openai"
    config:Optional[ConfigLoader]=Field(default=None,exclude=True)

    def model_post_init(self, __context:Any):
        self.config=ConfigLoader() #we load ConfigLoader class and store in in self.config variable
    
    class Config:
        arbitrary_types_allowed = True  #Allows you to store non-primitive Python objects in your Pydantic model without validation errors.

    def load_llm(self):
        try:
            """Load nad return the llm"""
            if self.model_provider=="groq":
                print("loading model from groq")
                model_name = self.config["llm"]["groq"]["model_name"]
                llm = ChatGroq(model=model_name)

            elif self.model_provider=="openai":
                print("Loading openai llm")
                model_name = self.config["llm"]["openai"]["model_name"]
                llm = ChatOpenAI(model=model_name,streaming=True)

            return llm
        except Exception as e:
            raise MyException(e,sys) from e
        





