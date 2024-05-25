from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def index():
    # Read sentiment results from JSON file
    with open('sentiment_results.json', 'r') as json_file:
        data = json.load(json_file)
        sources = data["source"]
        sentiment_scores = data["sentiment"]
        article_urls = data["article"]

    # Combine sources and sentiment scores into a list of tuples
    sentiment_results = list(zip(sources, sentiment_scores, article_urls))

    avg_sentiments = {}
    for source, score, _ in sentiment_results:
        if source not in avg_sentiments:
            avg_sentiments[source] = [score]
        else:
            avg_sentiments[source].append(score)

    avg_sentiments = {source: sum(scores) / len(scores) for source, scores in avg_sentiments.items()}

    return render_template('index.html', sentiment_results=sentiment_results, avg_sentiments=avg_sentiments)
if __name__ == '__main__':
    app.run(debug=True)