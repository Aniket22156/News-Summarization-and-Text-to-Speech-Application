from bs4 import BeautifulSoup
import requests
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from openai import OpenAI
from pathlib import Path
from transformers import pipeline
import spacy

# Load the NLP model for Named Entity Recognition (NER)
nlp = spacy.load("en_core_web_sm")

# Initialize OpenAI client at the top
client = OpenAI(api_key="Add you open api key here")

# Load the summarization pipeline
summarizer = pipeline("summarization")


def extract_news(company_name):
    # Base URL for Yahoo News search
    base_url = "https://news.search.yahoo.com/search?p="
    search_url = f"{base_url}{company_name.replace(' ', '+')}"

    # Send a GET request to Yahoo News
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(search_url, headers=headers)

    if response.status_code != 200:
        print("Error fetching Yahoo News")
        return []  # Return an empty list if the request fails

    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all news articles
    articles = []
    for item in soup.find_all('div', class_='NewsArticle')[:10]:  # Limit to 10 articles
        # Extract the title
        title_element = item.find('h4', class_='s-title')
        if not title_element:
            continue  # Skip if the title is not found
        title = title_element.text.strip()

        # Extract the link
        link_element = title_element.find('a')
        if not link_element or not link_element.get('href'):
            continue  # Skip if the link is not found
        link = link_element['href']

        # Extract the summary
        summary_element = item.find('p', class_='s-desc')
        summary = summary_element.text.strip() if summary_element else title  # Fallback to title if summary missing

        # Fetch the full content of the article
        try:
            article_response = requests.get(link, headers=headers)
            if article_response.status_code == 200:
                article_soup = BeautifulSoup(article_response.text, 'html.parser')
                article_content = article_soup.find('p')  # Extract first paragraph (adjust based on structure)
                if article_content:
                    article_text = article_content.get_text()
                    summary = summarizer(article_text, max_length=230, min_length=30, do_sample=False)[0]['summary_text']
            else:
                summary = title  # Fallback if the article page cannot be fetched
        except Exception as e:
            print(f"Error fetching article content: {e}")
            summary = title  # Fallback if an error occurs

        topics = extract_key_topics(title + " " + summary)

        # Add the article to the list
        articles.append({
            'title': title,
            'summary': summary,
            'content': summary,  # Use the summary as content for now
            'topics': topics,  # Placeholder for topics
            'link': link  # Add the full link to the article
        })

    return articles


def extract_key_topics(text):
    """Extract key topics from the text using Named Entity Recognition (NER)."""
    doc = nlp(text)
    keywords = set()
    for ent in doc.ents:
        if ent.label_ in ['PERSON', 'ORG', 'GPE', 'PRODUCT', 'EVENT']:
            keywords.add(ent.text)
    return list(keywords)


def analyze_sentiment(text):
    analyzer = SentimentIntensityAnalyzer()

    # Clean the text (remove special characters, extra spaces, etc.)
    cleaned_text = " ".join(text.split())  # Remove extra spaces
    cleaned_text = ''.join(e for e in cleaned_text if e.isalnum() or e.isspace())  # Remove special characters

    # Get sentiment scores
    sentiment_score = analyzer.polarity_scores(cleaned_text)

    # Determine sentiment based on compound score
    if sentiment_score['compound'] >= 0.05:
        return 'Positive'
    elif sentiment_score['compound'] <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'


def translate_to_hindi(text):
    """Translates English text to Hindi using OpenAI GPT."""
    response = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": "Translate the following text into Hindi."},
            {"role": "user", "content": text}
        ]
    )
    return response.choices[0].message.content


def generate_tts(text):
    """Generates an MP3 audio file from the input Hindi text using OpenAI GPT-4o Mini TTS."""
    speech_file_path = Path("static/output.mp3")

    hindi_text = translate_to_hindi(text)  # Convert text to Hindi before TTS

    response = client.audio.speech.create(
        model="gpt-4o-mini-tts",
        voice="alloy",
        input=hindi_text,
        instructions="Speak in Hindi with a clear and natural accent."
    )

    response.stream_to_file(speech_file_path)
    print("✅ TTS Audio generated successfully in Hindi: static/output.mp3")
    return "static/output.mp3"  # Return file path