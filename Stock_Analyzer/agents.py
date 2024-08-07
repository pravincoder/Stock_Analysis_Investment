from textwrap import dedent
import os
from crewai import Agent
from tools import YFinanceTools
from langchain_openai import ChatOpenAI #(Remove '#' If you are using OpenAI)
#from exa_tools import ExaSearchTool
from langchain_groq import ChatGroq
#from serp import SerpApi

""" llm = ChatOpenAI(
    base_url='http://localhost:11434/v1',
    model='mistral:latest',
    api_key='NA'
) #(If you are using Ollama) """

llm = ChatGroq(
    model = 'llama-3.1-70b-versatile',
    api_key='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'
)

""" llm = ChatOpenAI(
    model='gpt-3.5-turbo',
    api_key=os.getenv('OPENAI_API_KEY')
) #(If you are using ChatGPT) """
class Stock_bot_agents(): 
    def stock_anaylsis(self):
        return Agent(
            role = "Stock Analysis",
            goal = "To create a report on stock analysis.",
            tools = YFinanceTools.tools(),
            backstory=dedent("""
            As a stock analyst you are working for a Goldman Sachs company.
            you have been assigned to create a report of the analysis of the {stock_name} stock.
            You must try to keep a professional tone and should meet the given Requirements.
            You will get $1000 as a bonus if you complete the task within 3 iterations.
            """),
            verbose=True,llm=llm,allow_delegation=False
        )
    
    def investment_analysis(self):
        return Agent(
            role = "Stock Report",
            goal = "To create a report of the Investment analysis.",
            tools = YFinanceTools.tools(),
            backstory=dedent("""
            As a Investment analyst you are working for a Goldman Sachs company.
            you have been assigned to create a report of the Investment in the {stock_name} stock.
            You must try to keep a professional tone and should meet the given Requirements.

            You will get $1000 as a bonus if you complete the task within 3 iterations.                                       
            """),
            verbose=True,llm = llm,allow_delegation=False
        )