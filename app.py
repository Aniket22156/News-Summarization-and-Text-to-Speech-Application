import streamlit as st
import requests

# API endpoint
API_URL = "http://127.0.0.1:5000"

st.title("News Summarization and Text-to-Speech Application")

# Store report in session state
if "report" not in st.session_state:
    st.session_state.report = None

# User input
company_name = st.text_input("Enter Company Name", "Tesla")
topic_query = st.text_input("Search for a topic", "")

if st.button("Generate Report"):
    with st.spinner("Fetching news and analyzing sentiment..."):
        response = requests.post(
            f"{API_URL}/generate_report",
            json={"company_name": company_name}
        )

    if response.status_code == 200:
        st.session_state.report = response.json()
    else:
        st.error("Failed to generate report. Please try again.")

# Display the report only if it exists in session state
if st.session_state.report:
    report = st.session_state.report

    st.subheader("Sentiment Report")
    st.write(f"**Company**: {report['company']}")

    if not report['articles']:
        st.warning("No articles found for the given company.")
    else:
        for article in report['articles']:
            if topic_query.lower() in " ".join(article.get("topics", [])).lower():
                st.write(f"**Title**: {article['title']}")
                st.write(f"**Summary**: {article['summary']}")
                st.write(f"**Sentiment**: {article['sentiment']}")
                st.write(f"**Topics**: {', '.join(article.get('topics', []))}")
                st.write("---")

    # Display comparative analysis
    st.subheader("Comparative Analysis")
    sentiment_distribution = report['comparative_sentiment_score']['sentiment_distribution']
    st.write(
        f"**Sentiment Distribution**: Positive: {sentiment_distribution['positive']}, "
        f"Negative: {sentiment_distribution['negative']}, "
        f"Neutral: {sentiment_distribution['neutral']}"
    )

    for comparison in report['comparative_sentiment_score']['coverage_differences']:
        st.write(f"**Comparison**: {comparison['comparison']}")
        st.write(f"**Impact**: {comparison['impact']}")

    # Play Hindi TTS (only if available)
    if report.get('audio_url'):
        st.subheader("Hindi Text-to-Speech")
        st.audio(report['audio_url'], format='audio/mp3')
    else:
        st.warning("No audio summary available.")