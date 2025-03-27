import operator
from typing import Annotated, TypedDict, Union

from langchain_core.agents import AgentAction, AgentFinish

class AgentState(TypedDict):
    """
    Agent state to be used in the agent executor.
    """
    input: str
    agent_outcome: Union[AgentAction, AgentFinish, None]
    intermediate = Annotated[
        list[tuple[AgentAction, str]], operator.add
        
        ]