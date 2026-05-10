import streamlit as st

from youtube_analyzer import get_youtube_agent

st.title("🎥YouTube AI Analyzer")

video_url = st.text_input("Enter YouTube URL")

if st.button("Analyze Video"):

    youtube_agent = get_youtube_agent()

    with st.spinner("Analyzing video..."):

        response = youtube_agent.run(
            f"Summarize this video: {video_url}"
        )
        st.markdown("Analysis Report of Vedio:")
        st.write(response.content)

