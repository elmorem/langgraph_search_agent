from dotenv import load_dotenv
from langchain import hub
from langchain.agents import create_react_agent
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import Tool
from langchain_openai import ChatOpenAI


load_dotenv(override=True)

llm = ChatOpenAI(model= "gpt-3.5-turbo-1106", temperature=0)

react_prompt: PromptTemplate = hub.pull("hwchase17/react")

@Tool
def triple(num: float) -> float:
    """
    :param num: The number to be tripled.
    :return: The tripled number.
    """
    return float(num) * 3
tools = [
    TavilySearchResults(),
    triple,
]

react_agent_runnable = create_react_agent(
    llm=llm,
    tools=tools,
    prompt=react_prompt,
    verbose=True,
)
