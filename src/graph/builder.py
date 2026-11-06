from langgraph.graph import END, START, StateGraph

from graph.Node.decide import decide
from graph.Node.format_output import format_output
from graph.Node.receive import receive
from graph.state import State


builder = StateGraph(State)

builder.add_node("receive", receive)
builder.add_node("decide", decide)
builder.add_node("format_output", format_output)

builder.add_edge(START, "receive")
builder.add_edge("receive", "decide")
builder.add_edge("decide", "format_output")
builder.add_edge("format_output", END)

graph = builder.compile()