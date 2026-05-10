from dotenv import load_dotenv
load_dotenv()

from textwrap import dedent

from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.youtube import YouTubeTools


def get_youtube_agent():

    youtube_agent = Agent(
        name="YouTube Agent",

        model=Groq(
            id="llama-3.3-70b-versatile"
        ),

        tools=[YouTubeTools()],

        instructions=dedent("""
            You are an expert YouTube content analyst.

            Analyze the video carefully and provide:
            1. Summary
            2. Important timestamps
            3. Key concepts
            4. Actionable insights
        """),

        markdown=True
    )

    return youtube_agent
# youtube_agent.print_response(
#     "Summarize this video: https://www.youtube.com/watch?v=dQw4w9WgXcQ",
#     stream=True
# )
