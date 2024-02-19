import os
from  typing import TextIO
from dotenv import load_dotenv

import openai
import pandas as pd
import streamlit as st
from langchain.agents import create_csv_agent, create_pandas_dataframe_agent
from langchain.llms import OpenAI


# Load environment variables from .env file
load_dotenv()

# Access the API key
openai_api_key = os.getenv("OPENAI_API_KEY")

def get_answer_csv(file: TextIO, query: str) -> str:
    """
    Returns the answer to the given query by querying a CSV file.

    Args:
    - file (str): the file path to the CSV file to query.
    - query (str): the question to ask the agent.

    Returns:
    - answer (str): the answer to the query from the CSV file.
    """
    # Create an agent using OpenAI and the CSV file path
    agent = create_csv_agent(OpenAI(api_key=openai_api_key, model="code-davinci:002"), "titanic.csv", verbose=False)

    # Run the agent on the given query and return the answer
    answer = agent.run(query)
    return answer

