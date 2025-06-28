from fastapi import FastAPI,HTTPException
from pydantic import BaseModel,Field
from fastapi.responses import JSONResponse
import os
from agent.agentic_workflow import Graphbuilder
from IPython.display import display,Image

class Query(BaseModel):
    query:str=Field(...,description="Enter query here",examples="What is the weather in Paris?")

app = FastAPI()

@app.post("/query")

async def query(query:Query):
    try:
        print(query)
        graph = Graphbuilder(model_provider = "openai")
        app =graph()

        graph_png = display(Image(app.get_graph().draw_mermaid_png()))
        with open("my_graph.png","wb") as f:
            f.write(graph_png)
        print(f"Graph build and stored in {os.getcwd()}")

        messages = {"messages":[query.question]}
        output = app.invoke(messages)

        # if result is dict with messages
        if isinstance(output,dict) and "messages" in output:
            final_output = output["messages"][-1].content
        else:
            final_output = str(output)
        return {"answer":final_output}
    except Exception as e:
        return JSONResponse(status_code=500,content={"error",str(e)})
    
        
        



