from fastapi import FastAPI,HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel,Field
from typing import List
from fastapi.responses import JSONResponse
import os
from src.agent.agentic_workflow import GraphBuilder
from langchain_core.messages import HumanMessage


class Query(BaseModel):
    question: str
    travel_start_date:str
    travel_end_date:str
    budget_range:List[int]

app = FastAPI()
#In FastAPI (and Starlette, which FastAPI is built on), CORSMiddleware is used to handle Cross-Origin Resource Sharing (CORS).CORS is a security feature implemented by browsers.
#It controls which websites (origins) are allowed to make requests (like POST, GET) to your FastAPI server.
# ---->> When your FastAPI backend is separate from your frontend (e.g., React, Streamlit, or a mobile app
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],         # ← Allow ANY origin (public)
    allow_credentials=True,      # ← Allow cookies, auth headers
    allow_methods=["*"],         # ← Allow ALL HTTP methods (GET, POST, PUT, etc.)
    allow_headers=["*"],         # ← Allow ALL custom headers
)


@app.post("/query")
async def query(query:Query):
    try:
        print(query)
        graph = GraphBuilder(model_provider = "openai")
        workflow = graph()  #it is due to  __call__  in Graphbuilder call it let us call it as a function (build_graph -->Methood)

        graph_png = workflow.get_graph().draw_mermaid_png()
        with open("my_graph.png","wb") as f:
            f.write(graph_png)
        print(f"Graph build and stored in {os.getcwd()}")

        user_prompt = f"""
        User Query: {query.question}
        Travel Dates: {query.travel_start_date} to {query.travel_end_date}  
        Budget Range: PKR {query.budget_range[0]:,} to PKR {query.budget_range[1]:,}
        Please use this information to create a complete travel itinerary.
        """

        messages={"messages": [HumanMessage(content=user_prompt)]}
        output = workflow.invoke(messages)

        # if result is dict with messages
        if isinstance(output, dict) and "messages" in output and output["messages"]:
            final_output = output["messages"][-1].content if hasattr(output["messages"][-1], "content") else str(output["messages"][-1])
        else:
            final_output = "No answer generated."
        return {"answer":final_output}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

    
        
##uvicorn app:app --reload --port 8000
#uvicorn backend.app:app --reload --port 8000