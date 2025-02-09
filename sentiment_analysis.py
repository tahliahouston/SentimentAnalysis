from textblob import TextBlob


def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment_polarity = blob.sentiment.polarity

    if sentiment_polarity > 0:
        return "Positive"
    elif sentiment_polarity < 0:
        return "Negative"
    else:
        return "Neutral"

# Main program
if __name__ == "__main__":
    print("Welcome to the Sentiment Analysis Tool!")
    while True:
        # Get user input
        user_input = input("Enter a sentence (or type 'exit' to quit): ")
        if user_input.lower() == "exit":
            break

        sentiment = analyze_sentiment(user_input)
        print(f"Sentiment: {sentiment}\n")