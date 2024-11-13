from flask import Flask, render_template, request
from grammarcorrection import detect_language, correct_grammar_and_translate, analyze_sentiment, summarize_text,paraphrase_text

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/grammar", methods=["GET", "POST"])
def grammar_check():
    corrected_text = None
    if request.method == "POST":
        text = request.form["text"]
        corrected_text, _ = correct_grammar_and_translate(text)
    return render_template("grammar.html", corrected_text=corrected_text)

@app.route("/summarize", methods=["GET", "POST"])
def text_summarization():
    small_summary = medium_summary = large_summary = None
    if request.method == "POST":
        text = request.form["text"]
        small_summary = summarize_text(text, "small")
        medium_summary = summarize_text(text, "medium")
        large_summary = summarize_text(text, "large")
    return render_template("summarization.html", 
                           small_summary=small_summary, 
                           medium_summary=medium_summary, 
                           large_summary=large_summary)
@app.route("/paraphrase", methods=["GET", "POST"])
def paraphrasing():
    paraphrased_text = None
    if request.method == "POST":
        text = request.form["text"]
        paraphrased_text = paraphrase_text(text)  # Get the paraphrased version
    return render_template("paraphrasing.html", paraphrased_text=paraphrased_text)


if __name__ == "__main__":
    app.run(debug=True)
