from flask import Blueprint, render_template, request
import requests
import os

main = Blueprint('main', __name__)

# Main route for the app
@main.route('/', methods=['GET', 'POST'])
def index():
    sentiment = None
    if request.method == 'POST':
        text = request.form.get('text')  # Get the text from the form
        if text:
            sentiment = analyze_sentiment(text)  # Call the sentiment analysis function
        else:
            sentiment = {'error': 'No text entered'}
    
    return render_template('index.html', sentiment=sentiment)

def analyze_sentiment(text):
    """
    Analyzes the sentiment of the given text using Google Cloud NLP API.

    Args:
        text (str): The text to analyze.

    Returns:
        dict: A dictionary containing the sentiment score and confidence score.
    """
    api_key = os.getenv('API_KEY')  # Load API key from .env
    nlp_endpoint = os.getenv('NLP_ENDPOINT')  # Load endpoint from .env

    headers = {
        'Content-Type': 'application/json',
    }

    data = {
        'document': {
            'type': 'PLAIN_TEXT',
            'content': text
        },
        'encodingType': 'UTF8'
    }

    # Make a POST request to the Google NLP API
    response = requests.post(f"{nlp_endpoint}?key={api_key}", headers=headers, json=data)

    if response.status_code == 200:
        sentiment = response.json()['documentSentiment']
        return {
            'sentiment': sentiment['magnitude'],  # Magnitude represents the strength of sentiment
            'confidence': sentiment['score']  # Score represents positive/negative sentiment
        }
    else:
        return {'error': f"Error: {response.status_code}, {response.text}"}
