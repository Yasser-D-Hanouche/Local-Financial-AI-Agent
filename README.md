# 🤖 Local Financial AI Analyst (RAG)
A privacy-first, local AI assistant that fetches real-time financial news and answers questions using **Retrieval-Augmented Generation (RAG)**.

---

## 🌟 Overview
This project allows users to research stocks (like AAPL, NVDA, TSLA) by combining live market news with a local Large Language Model. Instead of the AI "guessing" or using old data, it searches a local database of recent articles to provide factual, data-driven answers.

### 🛠️ The Tech Stack
* **LLM:** [Ollama](https://ollama.com/) (Llama 3.2:1b) for local, private inference.
* **Orchestration:** [LangChain](https://www.langchain.com/) for RAG pipeline management.
* **Vector Database:** [ChromaDB](https://www.trychroma.com/) for persistent document storage.
* **Data Sources:** Alpha Vantage API.

---

## 📐 How It Works
1.  **Ingestion:** The app fetches the latest news summaries for a specific ticker.
2.  **Embedding:** Text is split into chunks and converted into mathematical vectors using `nomic-embed-text`.
3.  **Storage:** These vectors are stored in a local ChromaDB collection.
4.  **Retrieval:** When you ask a question, the system finds the 5 most relevant news snippets.
5.  **Generation:** The LLM uses those snippets as "context" to generate a concise financial summary.



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
