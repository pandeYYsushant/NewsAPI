import requests
import json

def get_news(api_key, query, from_date, to_date):
    url = f'https://newsapi.org/v2/everything?q={query}&from={from_date}&to={to_date}&sortBy=popularity&apiKey={api_key}'
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        articles = data['articles']
        return articles
    else:
        print("Failed to fetch news:", data['message'])
        return []

def display_news(articles):
    for idx, article in enumerate(articles, start=1):
        print(f"{idx}. {article['title']}")
        print(f"   Source: {article['source']['name']}")
        print(f"   URL: {article['url']}")
        print()

def main():
    api_key = "a0d3d0a51fef48269da19bd9da0448d8"  # Replace 'YOUR_API_KEY' with your actual API key
    query = input("Which topic do you want to knwo about?:")
    from_date = input("From date: ex-[2024-03-20]")
    to_date = input("To date:ex-[2024-03-21]")
    articles = get_news(api_key, query, from_date, to_date)
    if articles:
        print(f"Top {query.capitalize()} News (Global):")
        print("---------------------------------------------")
        display_news(articles)
    else:
        print("No news articles found.")

if __name__ == "__main__":
    main()
