
import requests
from dotenv import load_dotenv

# Load API key from environment variables
load_dotenv()
GROQ_API_KEY = "APIKEY"
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

def summarize_text(text, summary_length="medium"):
    """Summarize the text in small, medium, or large length using the GROQ API."""
    summary_prompt = ""
    
    if summary_length == "small":
        summary_prompt = f"Summarize this text in a few sentences:\n\n{text}"
    elif summary_length == "medium":
        summary_prompt = f"Summarize this text in a concise paragraph:\n\n{text}"
    elif summary_length == "large":
        summary_prompt = f"Summarize this text in a detailed but brief paragraph:\n\n{text}"

    payload = {
        "model": "llama3-8b-8192",
        "messages": [
            {
                "role": "user",
                "content": summary_prompt
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
            summary = data["choices"][0]["message"]["content"].strip()
            return summary
        return "Unable to summarize text."
    except requests.exceptions.RequestException:
        return "Unable to summarize text."
def paraphrase_text(text):
    """Paraphrase the text while keeping the meaning intact."""
    paraphrase_payload = {
        "model": "llama3-8b-8192",  # Or any other paraphrasing model you use
        "messages": [
            {
                "role": "user",
                "content": f"Paraphrase the following text without changing its meaning:\n\n{text}"
            }
        ]
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {GROQ_API_KEY}"
    }

    try:
        response = requests.post(GROQ_API_ENDPOINT, json=paraphrase_payload, headers=headers)
        response.raise_for_status()
        data = response.json()
        if "choices" in data and len(data["choices"]) > 0:
            return data["choices"][0]["message"]["content"].strip()
        return "Unable to paraphrase the text."
    except requests.exceptions.RequestException:
        return "Error paraphrasing the text."

