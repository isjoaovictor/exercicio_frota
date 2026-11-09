from langgraph.graph import END, START, StateGraph

from graph.Node.analyze import analyze
from graph.Node.answer_rules import answer_rules
from graph.Node.classify import classify
from graph.Node.decide import decide
from graph.Node.format_output import format_output
from graph.Node.human_review import human_review
from graph.Node.prepare import prepare
from graph.Node.receive import receive
from graph.Node.refuse import refuse
from graph.Node.tools import tools
from graph.routing import route_by_intent
from graph.state import State


builder = StateGraph(State)

builder.add_node("receive", receive)
builder.add_node("classify", classify)
builder.add_node("prepare", prepare)
builder.add_node("analyze", analyze)
builder.add_node("tools", tools)
builder.add_node("human_review", human_review)
builder.add_node("answer_rules", answer_rules)
builder.add_node("refuse", refuse)
builder.add_node("decide", decide)
builder.add_node("format_output", format_output)


builder.add_edge(START, "receive")
builder.add_edge("receive", "classify")
builder.add_conditional_edges(
    "classify",
     route_by_intent, {
    "primeiro_a_chegar": "prepare",
    "regras": "answer_rules",
    "fora_escopo": "refuse"
})
builder.add_edge("prepare", "analyze")
builder.add_edge("refuse", END)
builder.add_edge("answer_rules", END)
builder.add_edge("format_output", END)

graph = builder.compile()
