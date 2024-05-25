import requests

def collect_articles(api_key):
    url = 'https://newsapi.org/v2/everything'
    params = {
        'q': 'Palestine OR Gaza OR West Bank',  # Search query
        # 'sources': 'bbc-news,cnn,al-jazeera-english,fox-news,the-guardian-uk,the-new-york-times,reuters,associated-press,the-washington-post',  # News sources
        'from': '2024-04-25',  # Start date
        'to': '2024-05-24',  # End date
        'language': 'en',
        'sortBy': 'relevancy',  # Sorting criteria
        'apiKey': api_key  # Your API key
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    response = requests.get(url, params=params, headers=headers)

    if response.status_code == 200:
        articles = response.json().get('articles')
        if articles:
            print(f"Retrieved {len(articles)} articles")
            return articles
        else:
            print("No articles found")
            return []
    else:
        print(f"Failed to retrieve articles: {response.status_code}")
        print(f"Response: {response.json()}")
        return []