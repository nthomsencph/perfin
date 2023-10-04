from langchain.agents import AgentType, Tool, initialize_agent
from langchain.chat_models import ChatOpenAI
from langchain.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain

from perfin.agent.prompts import AGENT_SYSTEM_MESSAGE, DB_CHAIN_PROMPT
from perfin.config import API_KEY, DB_URL

llm = ChatOpenAI(
    temperature=0.7,
    model="gpt-3.5-turbo",
    verbose=True,
    openai_api_key=API_KEY,
    streaming=True,
)
db_chain = SQLDatabaseChain.from_llm(
    llm,
    SQLDatabase.from_uri(DB_URL),
    verbose=True,
    prompt=DB_CHAIN_PROMPT,
    # return_intermediate=True
)
tools = [
    Tool(
        name="TransactionsDB",
        func=db_chain.run,
        description="useful for when you need to answer questions about past transactions. The required input is the full user message as a string.",
    )
]

AGENT = initialize_agent(
    tools,
    llm,
    agent=AgentType.OPENAI_MULTI_FUNCTIONS,
    verbose=True,
    handle_parsing_errors=True,
    agent_kwargs={"system_message": AGENT_SYSTEM_MESSAGE},
)
