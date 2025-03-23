# **News Summarization and Text-to-Speech Application**

[![Generic badge](https://img.shields.io/badge/🤗%20Hugging%20Face-Spaces-blue.svg)](https://huggingface.co/spaces/Aniket22145/News_Summarization_and_Text-to-Speech_Application)

This project is a **Streamlit-based web application** that fetches news articles related to a given company, performs sentiment analysis, summarizes the articles, and generates a Hindi text-to-speech (TTS) audio summary using **OpenAI's TTS API**. The application is designed to help users quickly understand the sentiment and key topics in news coverage about a company.

---

## **Table of Contents**
1. [Overview](#overview)
2. [Features](#features)
3. [How It Works](#how-it-works)
4. [Technologies Used](#technologies-used)
5. [Why We Use These Technologies](#why-we-use-these-technologies)
6. [Project Structure](#project-structure)
7. [How to Run the Project](#how-to-run-the-project)
8. [Future Enhancements](#future-enhancements)

---

## **Overview**
The application allows users to:
1. Enter a company name (e.g., "Tesla").
2. Optionally, enter a topic to filter the news articles.
3. Fetch the latest news articles related to the company.
4. Analyze the sentiment of the articles (positive, negative, or neutral).
5. Summarize the articles and extract key topics.
6. Generate a Hindi audio summary of the news using **OpenAI's TTS API**.

The application is built using **Streamlit** for the frontend and **Flask** for the backend API. It leverages various NLP (Natural Language Processing) tools and libraries to perform sentiment analysis, summarization, and text-to-speech conversion.

---

## **Features**
1. **News Fetching**:
   - Fetches the latest news articles from Yahoo News using web scraping.
2. **Sentiment Analysis**:
   - Uses the **VADER Sentiment Analyzer** to determine the sentiment of each article.
3. **Summarization**:
   - Summarizes the content of each article using the **Hugging Face Transformers** library.
4. **Topic Extraction**:
   - Extracts key topics from the articles using **spaCy** for Named Entity Recognition (NER).
5. **Text-to-Speech (TTS)**:
   - Translates the summary into Hindi and generates an audio file using **OpenAI's TTS API**.
6. **Query Feature**:
   - Allows users to filter articles based on a specific topic or keyword.
7. **Comparative Analysis**:
   - Provides a comparative analysis of the sentiment distribution and generates insights based on the news coverage.

---

## **How It Works**
1. **User Input**:
   - The user enters a company name and optionally a topic to filter the news articles.
2. **News Fetching**:
   - The application scrapes Yahoo News for articles related to the company.
3. **Sentiment Analysis**:
   - Each article is analyzed for sentiment (positive, negative, or neutral).
4. **Summarization**:
   - The content of each article is summarized using a pre-trained summarization model.
5. **Topic Extraction**:
   - Key topics (e.g., people, organizations, locations) are extracted from the articles.
6. **Text-to-Speech**:
   - The summary is translated into Hindi using **OpenAI GPT** and converted into an audio file using **OpenAI's TTS API**.
7. **Query Feature**:
   - The user can filter articles based on a specific topic or keyword. Only articles containing the query in their topics or content are displayed.
8. **Report Generation**:
   - A detailed report is generated, including sentiment distribution, comparative analysis, and the audio summary.

---

## **Technologies Used**
1. **Streamlit**:
   - Used for building the frontend of the application.
2. **Flask**:
   - Used for the backend API to handle requests and generate reports.
3. **BeautifulSoup**:
   - Used for web scraping to fetch news articles from Yahoo News.
4. **VADER Sentiment Analyzer**:
   - Used for sentiment analysis of the news articles.
5. **Hugging Face Transformers**:
   - Used for summarizing the content of the articles.
6. **spaCy**:
   - Used for Named Entity Recognition (NER) to extract key topics.
7. **OpenAI GPT**:
   - Used for translating the summary into Hindi.
8. **OpenAI TTS API**:
   - Used for generating Hindi audio from the translated text.
9. **Requests**:
   - Used for making HTTP requests to fetch news articles and interact with the backend API.

---

## **Why We Use These Technologies**
1. **Streamlit**:
   - Streamlit is a powerful and easy-to-use framework for building data-driven web applications. It allows us to create interactive UIs with minimal code.
2. **Flask**:
   - Flask is a lightweight and flexible web framework for Python. It is used to create the backend API that processes requests and generates reports.
3. **BeautifulSoup**:
   - BeautifulSoup is a Python library for parsing HTML and XML documents. It is used to scrape news articles from Yahoo News.
4. **VADER Sentiment Analyzer**:
   - VADER (Valence Aware Dictionary and sEntiment Reasoner) is a rule-based sentiment analysis tool specifically designed for social media text. It is used to analyze the sentiment of news articles.
5. **Hugging Face Transformers**:
   - Hugging Face provides pre-trained models for various NLP tasks, including summarization. We use the `sshleifer/distilbart-cnn-12-6` model to summarize the articles.
6. **spaCy**:
   - spaCy is a powerful NLP library for tasks like Named Entity Recognition (NER). It is used to extract key topics (e.g., people, organizations, locations) from the articles.
7. **OpenAI GPT**:
   - OpenAI GPT is used for translating the summary into Hindi. It provides high-quality translations and is easy to integrate.
8. **OpenAI TTS API**:
   - OpenAI's TTS API is used for generating high-quality Hindi audio from the translated text. It supports multiple languages and voices, making it ideal for this application.
9. **Requests**:
   - The `requests` library is used to make HTTP requests to fetch news articles and interact with the backend API.

---

## **Project Structure**
News_Summarization_and_Text-to-Speech_Application/
```bash
├── app.py # Main Streamlit application

├── api.py # Flask backend API

├── utils.py # Utility functions (news fetching, sentiment analysis, etc.)
├── requirements.txt # List of dependencies
├── static/ # Folder for storing audio files
│ └── output.mp3 # Generated Hindi audio file
└── README.md # Project documentation
```


---

## **How to Run the Project**
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/News_Summarization_and_Text-to-Speech_Application.git
   cd News_Summarization_and_Text-to-Speech_Application
2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
3. **Set Up OpenAI API Key**:
   ```bash
   client = OpenAI(api_key="Add you open api key here")
4. **Run the Flask Backend**:
   ```bash
   python api.py
5. **Run the Streamlit Frontend**:
   ```bash
   streamlit run app.py

## Conclusion:
This project demonstrates how to build a data-driven web application using Streamlit, Flask, and various NLP tools. It provides users with a quick and easy way to understand the sentiment and key topics in news coverage about a company. The application leverages OpenAI's TTS API for generating high-quality Hindi audio summaries and includes a query feature to filter articles based on specific topics or keywords, making it a valuable tool for investors, analysts, and researchers.
