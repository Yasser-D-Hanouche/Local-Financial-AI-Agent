import os
from financial_news_retriever import fetch_financial_news
from dbman import get_database_retriever
from test_agent1 import start_chat

def main():
    print("=== Welcome to your Personal AI Financial Analyst ===")
    
    symbol = input("Enter the stock symbol you want to research (e.g., AAPL, NVDA, TSLA): ").upper()
    api_key = "Your API key here" 
    
    print("\n--- Step 1: Downloading latest news ---")
    fetch_financial_news(symbol, api_key)
    
    print("\n--- Step 2: Preparing the AI memory ---")
    file_path = f"./stocks/financial_news_{symbol}.txt"
    
    if not os.path.exists(file_path):
        print("Error: Could not find the news data. Stopping here.")
        return

    retriever = get_database_retriever(file_path)
    
    print("\n--- Step 3: Starting the Chat ---")
    start_chat(retriever)

if __name__ == "__main__":
    main()
