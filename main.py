from dotenv import load_dotenv
from langchain_core.agents import AgentFinish
from langgraph.graph import END, StateGraph
from nodes import run_agent_reasoning_engine, execture_tools
from state import AgentState

load_dotenv(override=True)

AGENT_REASON = "agent_reason"
ACT = "act"

def should_continue(state: AgentState) -> str:
    if isinstance(state["agent_outcome"], AgentFinish):
        return END
    return ACT




if __name__ == "__main__":
    print("Hello, World!")