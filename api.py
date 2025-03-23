from flask import Flask, request, jsonify
from utils import extract_news, analyze_sentiment, generate_tts

app = Flask(__name__)


@app.route('/generate_report', methods=['POST'])
def generate_report():
    data = request.json
    company_name = data.get('company_name', 'Tesla')

    # Step 1: Extract news articles
    articles = extract_news(company_name)

    if not articles:
        return jsonify({"error": "No news articles found for the given company."}), 404

    # Step 2: Perform sentiment analysis
    analyzed_articles = []
    for article in articles:
        sentiment = analyze_sentiment(article.get('content', ''))
        analyzed_articles.append({
            'title': article.get('title', 'No Title'),
            'summary': article.get('summary', 'No Summary'),
            'sentiment': sentiment,
            'topics': article.get('topics', [])
        })

    # Step 3: Comparative analysis
    sentiment_distribution = {
        'positive': sum(1 for a in analyzed_articles if a['sentiment'] == 'Positive'),
        'negative': sum(1 for a in analyzed_articles if a['sentiment'] == 'Negative'),
        'neutral': sum(1 for a in analyzed_articles if a['sentiment'] == 'Neutral')
    }

    # Step 4: Generate dynamic coverage_differences
    coverage_differences = []

    # Example logic for generating comparisons and impacts
    if sentiment_distribution['positive'] > sentiment_distribution['negative']:
        coverage_differences.append({
            'comparison': 'Most articles highlight positive news about the company.',
            'impact': 'Investors may feel optimistic about the company\'s growth prospects.'
        })
    elif sentiment_distribution['negative'] > sentiment_distribution['positive']:
        coverage_differences.append({
            'comparison': 'Most articles discuss challenges or negative aspects of the company.',
            'impact': 'Investors may remain cautious due to potential risks or regulatory scrutiny.'
        })
    else:
        coverage_differences.append({
            'comparison': 'The coverage is balanced, with both positive and negative news.',
            'impact': 'Investors may weigh the pros and cons before making decisions.'
        })

    # Step 4: Generate TTS
    summary_text = " ".join([a['summary'] for a in analyzed_articles if a['summary']])

    if summary_text.strip():
        audio_url = generate_tts(summary_text)
    else:
        audio_url = None

    # Step 5: Prepare final report
    report = {
        'company': company_name,
        'articles': analyzed_articles,
        'comparative_sentiment_score': {
            'sentiment_distribution': sentiment_distribution,
            'coverage_differences': coverage_differences
        },
        'audio_url': audio_url
    }

    return jsonify(report)


if __name__ == '__main__':
    app.run(debug=True)