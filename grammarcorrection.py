import requests
import json
from dotenv import load_dotenv
import os

# Load API key from environment variables
load_dotenv()
GROQ_API_KEY = "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"
GROQ_API_ENDPOINT = "https://api.groq.com/openai/v1/chat/completions"

def detect_language(text):
    """Detect the language of the given text using the GROQ API."""
    if not GROQ_API_KEY:
        return None

    payload = {
        "model": "llama3-8b-8192",
        "messages": [
            {
                "role": "user",
                "content": f"Detect the language of this text: {text}"
            }
        ]
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {GROQ_API_KEY}"
    }

    try:
        response = requests.post(GROQ_API_ENDPOINT, json=payload, headers=headers)
        response.raise_for_status()
        data = response.json()
        if "choices" in data and data["choices"]:
            language = data["choices"][0]["message"]["content"].split(": ")[-1].strip()
            return language
        return None
    except requests.exceptions.RequestException:
        return None

def correct_grammar_and_translate(text):
    """Correct grammar in the same language and provide an English translation."""
    payload = {
        "model": "llama3-8b-8192",
        "messages": [
            {
                "role": "user",
                "content": f"Please correct the grammar in the following text and then translate it to English:\n\n{text}"
            }
        ]
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {GROQ_API_KEY}"
    }

    try:
        response = requests.post(GROQ_API_ENDPOINT, json=payload, headers=headers)
        response.raise_for_status()
        data = response.json()
        if "choices" in data and len(data["choices"]) > 0:
            response_text = data["choices"][0]["message"]["content"].strip().split("\n\n")
            corrected_text = response_text[0].strip() if len(response_text) > 0 else text
            english_translation = response_text[1].strip() if len(response_text) > 1 else "Translation unavailable."
            return corrected_text, english_translation
        return text, "Translation unavailable."
    except requests.exceptions.RequestException:
        return text, "Translation unavailable."

def analyze_sentiment(text):
    """Perform sentiment analysis on the corrected text."""
    payload = {
        "model": "llama3-8b-8192",
        "messages": [
            {
                "role": "user",
                "content": f"Analyze the sentiment of the following text: {text}"
            }
        ]
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {GROQ_API_KEY}"
    }

    try:
        response = requests.post(GROQ_API_ENDPOINT, json=payload, headers=headers)
        response.raise_for_status()
        data = response.json()
        if "choices" in data and len(data["choices"]) > 0:
            sentiment_analysis = data["choices"][0]["message"]["content"]
            return sentiment_analysis
        return "Unable to analyze sentiment."
    except requests.exceptions.RequestException:
        return "Unable to analyze sentiment."
