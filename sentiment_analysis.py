from textblob import TextBlob

def analyze_sentiment(text):
    analysis = TextBlob(text)
    return analysis.sentiment.polarity

def analyze_articles(texts):
    sentiments = [analyze_sentiment(text) for text in texts]
    return sentiments