from agent.agentic_workflow import GraphBuilder

graph = GraphBuilder(model_provider="openai")
workflow = graph()
print(workflow.invoke({"messages": ["Hello!"]}))
