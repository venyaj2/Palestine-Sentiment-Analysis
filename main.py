from data_collection import collect_articles
from preprocessing import preprocess_articles
from sentiment_analysis import analyze_articles
from visualization import visualize_sentiments

def main():
    api_key = '8fa5137bb34a433a8b5b11b770c1df92'
    articles = collect_articles(api_key)
    if articles:
        preprocessed_texts = preprocess_articles(articles)
        sentiments = analyze_articles(preprocessed_texts)
        visualize_sentiments(articles, sentiments)

if __name__ == "__main__":
    main()
