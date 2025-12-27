import requests
import json
import csv

API_KEY = "YOUR_NEWSAPI_KEY"
URL = "https://newsapi.org/v2/top-headlines?country=in&apiKey=" + API_KEY

def fetch_news():
    response = requests.get(URL)
    data = response.json()
    return data["articles"]

def filter_news(news, keyword):
    return [n for n in news if keyword.lower() in n["title"].lower()]

def save_json(news):
    with open("news.json", "w") as f:
        json.dump(news, f, indent=4)

def save_csv(news):
    with open("news.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Title", "Source"])
        for n in news:
            writer.writerow([n["title"], n["source"]["name"]])

news = fetch_news()
key = input("Enter keyword: ")
filtered = filter_news(news, key)
save_json(filtered)
save_csv(filtered)
print("News saved successfully")
