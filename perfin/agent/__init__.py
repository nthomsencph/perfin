from langchain.chat_models.openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain

from perfin.config import API_KEY, DB_URL

TEMPLATE = """Given an input question, first create a syntactically correct {dialect} query to run, then look at the results of the query and return the answer.
Use the following format:

Question: "Question here"
SQLQuery: "SQL Query to run"
SQLResult: "Result of the SQLQuery"
Answer: "Final answer here"

Only use rows with 'user_key'='{user}' from the '{table}' table. The table has the following columns:

{table_columns}.

All amounts are in DKK. Remember that
- expenses are negative (e.g. -100.0)
- income is positive (e.g. 100.0)
- the balance is the sum of all transactions up to and including the current transaction

Question: {query}"""

PROMPT = PromptTemplate(
    input_variables=["query", "user", "table", "table_columns", "dialect"],
    template=TEMPLATE,
)

# Some examples of SQL queries that corrsespond to questions are:

# {few_shot_examples}

DB_CHAIN = SQLDatabaseChain.from_llm(
    ChatOpenAI(
        temperature=0.7, model="gpt-3.5-turbo", verbose=True, openai_api_key=API_KEY
    ),
    SQLDatabase.from_uri(DB_URL),
    verbose=True,
)
