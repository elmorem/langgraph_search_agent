from dotenv import load_dotenv
from langgraph.prebuilt.tool_node import ToolNode
from react import react_agent_runnable, tools
from state import AgentState

load_dotenv(override=True)

def run_agent_reasoning_engine(state: AgentState):
    agent_outcome = react_agent_runnable.invoke(state)
    return {"agent_outcome": agent_outcome}

tool_node = ToolNode(tools=tools)

def execture_tools(state: AgentState):
    """
    Execute the tools in the agent state.
    """
    agent_action = state["agent_outcome"]
    output = ToolNode.invoke(agent_action)
    return {"intermediate_steps": [(agent_action, str(output))]}

