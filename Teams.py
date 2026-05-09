from agno.agent import Agent
from agno.models.groq import Groq
from dotenv import load_dotenv
from agno.team import Team

load_dotenv()

eng_agent = Agent(
    name="English Agent",
    role="You answer questions in English."
)

chi_agent = Agent(
    name="Chinese Agent",
    role="You answer questions in Chinese."
)

hin_agent = Agent(
    name="Hindi Agent",
    role="You answer questions in Hindi."
)

team_leader = Team(
    name="Multilingual Team",

    members=[eng_agent, chi_agent, hin_agent],

    instructions="""
    You are a multilingual AI team.
    Detect the user's language and respond in that language.
    """,

    model=Groq(
        id="llama-3.1-8b-instant"
    ),

    markdown=True,
    show_members_responses=True
)

team_leader.print_response(
    "What is the capital of France?"
)

team_leader.print_response(
    "法国的首都是哪里？"
)

team_leader.print_response(
    "फ्रांस की राजधानी क्या है?"
)


