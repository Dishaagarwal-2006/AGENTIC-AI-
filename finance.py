from agno.agent import Agent
from agno.models.groq import Groq
from dotenv import load_dotenv
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.website import WebsiteTools
from agno.tools.yfinance import YFinanceTools 


load_dotenv()

def build_agent():
    return Agent(
        model=Groq(id="llama-3.1-8b-instant"),

        tools=[
            DuckDuckGoTools(),
            WebsiteTools(),
            YFinanceTools()
            
        ],

        markdown=True,

        instructions="""
        You are an expert financial assistant specializing in stocks, investing, markets, personal finance, and company analysis.""",

        add_datetime_to_context=True,
        debug_mode=True
    )

groq_agent = build_agent()

groq_agent.print_response(
    "What is the current stock price of Apple Inc. (AAPL)?"
)