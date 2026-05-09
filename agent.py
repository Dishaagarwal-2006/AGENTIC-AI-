from agno.agent import Agent
from agno.models.groq import Groq
from dotenv import load_dotenv

from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.website import WebsiteTools

load_dotenv()

def build_agent():
    return Agent(
        model=Groq(id="llama-3.1-8b-instant"),

        tools=[
            DuckDuckGoTools(),
            WebsiteTools()
        ],

        markdown=True,

        instructions="""
        You are a helpful AI research assistant.
        When given a URL, analyze the website carefully.
        """,

        add_datetime_to_context=True,
    )

groq_agent = build_agent()

groq_agent.print_response(
    "Summarize this website: https://www.nvidia.com"
)

