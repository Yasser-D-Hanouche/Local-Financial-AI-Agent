# 📈 AI Financial Analyst: Local RAG Pipeline

A high-performance, **privacy-first** financial research tool. This application uses **Retrieval-Augmented Generation (RAG)** to analyze real-time market news locally, ensuring your investment queries never leave your machine.

---

## 🧠 Why This Project?
Traditional LLMs (like ChatGPT) have a "knowledge cutoff" and can't see today's news. This project solves that by:

* **Real-time Data:** Injecting live news from Alpha Vantage and Yahoo Finance.
* **Contextual Memory:** Using a vector database (ChromaDB) to store and compare multiple stocks.
* **Total Privacy:** Running completely offline via **Ollama**—no data is sent to OpenAI or Google.

---

## 🛠️ Technical Architecture

### The RAG Workflow
1.  **Ingestion Engine:** Fetches raw market data and news for specific tickers (AAPL, NVDA, etc.).

2.  **Document Processing:** Uses `RecursiveCharacterTextSplitter` to break long articles into semantic chunks.
3.  **Vector Embedding:** Converts text chunks into 768-dimensional vectors using the `nomic-embed-text` model.

4.  **Semantic Search:** Queries **ChromaDB** for the top **K=5** most relevant snippets based on user input.
5.  **Augmented Generation:** Passes snippets to **Llama 3.2 (1b)** with a specialized financial advisor prompt.



---

## 🚀 Getting Started

### Prerequisites
* Python 3.10+
* [Ollama](https://ollama.com/) installed and running.
* An [Alpha Vantage API Key](https://www.alphavantage.co/support/#api-key) (Free).

### Installation
1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/Yasser-D-Hanouche/Local-Financial-AI-Agent.git](https://github.com/Yasser-D-Hanouche/Local-Financial-AI-Agent.git)
    cd Local-Financial-AI-Agent
    ```
2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Pull the local models:**
    ```bash
    ollama pull llama3.2:1b
    ollama pull nomic-embed-text
    ```

### Usage
Run the main script and follow the prompts:
```bash
python main.py
