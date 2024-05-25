import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import json

def visualize_sentiments(articles, sentiments):
    sentiment_data = {
        'source': [article['source']['name'] for article in articles if article['content']],
        'sentiment': sentiments
    }

    sentiment_data2 = {
        'source': [article['source']['name'] for article in articles if article['content']],
        'sentiment': sentiments,
        'article': [article['url'] for article in articles if article['content']]
    }

    with open('sentiment_results.json', 'w') as json_file:
        json.dump(sentiment_data2, json_file)


    df = pd.DataFrame(sentiment_data)

    plt.figure(figsize=(12, 6))
    sns.boxplot(x='source', y='sentiment', data=df)
    plt.xticks(rotation=90)
    plt.title('Sentiment Analysis of News Articles on Palestine')
    plt.xlabel('News Source')
    plt.ylabel('Sentiment Score')
    plt.show()