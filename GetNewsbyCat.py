import requests
import json

def get_news(api_key, country, category):
    url = f'https://newsapi.org/v2/top-headlines?country={country}&category={category}&apiKey={api_key}'
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
    api_key = "a0d3d0a51fef48269da19bd9da0448d8"
      # Replace 'YOUR_API_KEY' with your actual API key
    country = input("Which country news do you want?:")
    category= input("Which topic do you want to knwo about?:")

    articles = get_news(api_key, country, category)
    if articles:
        print(f"Top {category.capitalize()} News from {country}:")
        print("---------------------------------------------")
        display_news(articles)
    else:
        print("No news articles found.")

if __name__ == "__main__":
    main()
