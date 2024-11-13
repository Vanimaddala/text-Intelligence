from flask import Flask, render_template, request
from grammarcorrection import detect_language, correct_grammar_and_translate, analyze_sentiment

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    language = None
    corrected_text = None
    english_translation = None
    sentiment = None

    if request.method == "POST":
        text = request.form["text"]
        
        # Call the functions from grammardetection.py
        language = detect_language(text)
        corrected_text, english_translation = correct_grammar_and_translate(text)
        sentiment = analyze_sentiment(corrected_text)

    return render_template(
        "index.html", 
        language=language, 
        corrected_text=corrected_text, 
        english_translation=english_translation, 
        sentiment=sentiment
    )

if __name__ == "__main__":
    app.run(debug=True)
