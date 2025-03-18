from flask import Flask, render_template, request
import requests
from datetime import datetime

app = Flask(__name__)

API_KEY = "84fc1abf89a440cc9411840f4e0e183c"  # Your NewsAPI key
BASE_URL = "https://newsapi.org/v2/top-headlines"  # Correct API endpoint

@app.route('/')
def home():
    country = request.args.get('country', 'us')  # Default country US
    category = request.args.get('category', 'general')  # Default category General
    
    url = f"{BASE_URL}?country={country}&category={category}&apiKey={API_KEY}"
    
    try:
        response = requests.get(url)
        news_data = response.json()
        
        if news_data.get("status") == "ok":
            articles = news_data.get("articles", [])
        else:
            articles = []
            
        # Format the publish date for each article
        for article in articles:
            if article.get("publishedAt"):
                date_obj = datetime.strptime(article["publishedAt"], "%Y-%m-%dT%H:%M:%SZ")
                article["formatted_date"] = date_obj.strftime("%B %d, %Y")
            else:
                article["formatted_date"] = "Unknown date"
                
    except Exception as e:
        print(f"Error fetching news: {e}")
        articles = []
    
    # List of available countries and categories for the dropdown
    countries = [
        {"code": "us", "name": "United States"},
        {"code": "gb", "name": "United Kingdom"},
        {"code": "in", "name": "India"},
        {"code": "ca", "name": "Canada"},
        {"code": "au", "name": "Australia"}
    ]
    
    categories = [
        {"code": "general", "name": "General"},
        {"code": "business", "name": "Business"},
        {"code": "technology", "name": "Technology"},
        {"code": "sports", "name": "Sports"},
        {"code": "entertainment", "name": "Entertainment"},
        {"code": "health", "name": "Health"},
        {"code": "science", "name": "Science"}
    ]
    
    return render_template('index.html', 
                          articles=articles, 
                          selected_country=country, 
                          selected_category=category,
                          countries=countries,
                          categories=categories,
                          datetime=datetime)

if __name__ == '__main__':
    app.run(debug=True)
