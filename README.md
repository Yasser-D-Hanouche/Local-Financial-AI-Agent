# Local Financial RAG Assistant 📈
An AI-powered financial advisor that uses **Retrieval-Augmented Generation (RAG)** to answer questions based on live stock news.

## Features
- **Live Data:** Fetches news using Alpha Vantage and Yahoo Finance APIs.
- **Local AI:** Uses Ollama (Llama 3.2:1b) for 100% private data processing.
- **Persistent Memory:** Uses ChromaDB to store and retrieve financial news.

## Setup
1. Install [Ollama](https://ollama.com/) and run `ollama pull llama3.2:1b`.
2. Clone this repo.
3. Install dependencies: `pip install -r requirements.txt`.
4. Run the app: `python main.py`.
