import requests
import time
import os

def fetch_financial_news(symbol, api_key ):
    #api_key = 'JGTGEOS9F12I5X7P'  
    #symbol = 'AAPL'                

    url = f'https://www.alphavantage.co/query?function=NEWS_SENTIMENT&tickers={symbol}&apikey={api_key}'

    print(f"Fetching news for {symbol}...")
    
    try:
        response = requests.get(url)
        data = response.json()
    except Exception:
        print("Could not access the internet")
        return
    
    folder = "./stocks"
    os.makedirs(folder, exist_ok=True)
    file_path = f"{folder}/financial_news_{symbol}.txt"

    if "feed" in data:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(f"--- FINANCIAL NEWS REPORT: {symbol} ---\n")
            file.write(f"Generated on: {time.strftime('%Y-%m-%d %H:%M:%S')}\n\n")

            for article in data['feed'][:1]: 
                title = article.get('title', 'No Title')
                summary = article.get('summary', 'No Summary available.')
                
                raw_date = article.get('time_published', '')
                formatted_date = f"{raw_date[:4]}-{raw_date[4:6]}-{raw_date[6:8]}" if raw_date else "Unknown"  
                        
                ticker_sentiment = "N/A"
                for t in article.get('ticker_sentiment', []):
                    if t['ticker'] == symbol:
                        ticker_sentiment = t['ticker_sentiment_label']
                        break

                file.write(f"TITLE: {title}\n")
                file.write(f"Article dating from: {formatted_date}\n")
                file.write(f"SENTIMENT: {ticker_sentiment}\n")
                file.write(f"SUMMARY: {summary}\n")
                file.write("-" * 50 + "\n\n")
                
        print("Success! Your news report is saved in 'financial_news_[Symbol].txt'.")
    else:
        # Handle errors (like hitting the 25-request daily limit)
        print("Error: Could not find news. You might have hit your daily API limit.")
        if "Note" in data:
            print(f"Alpha Vantage says: {data['Note']}")