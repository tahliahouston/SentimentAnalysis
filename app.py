from flask import Flask, request, render_template
from textblob import TextBlob

app = Flask(__name__)

# Function to analyze sentiment
def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment_polarity = blob.sentiment.polarity
    if sentiment_polarity > 0:
        return "Positive"
    elif sentiment_polarity < 0:
        return "Negative"
    else:
        return "Neutral"

# Home page
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        user_input = request.form["text"]
        sentiment = analyze_sentiment(user_input)
        return render_template("index.html", sentiment=sentiment, user_input=user_input)
    return render_template("index.html", sentiment=None, user_input=None)

# Run the app
if __name__ == "__main__":
    app.run(debug=True)