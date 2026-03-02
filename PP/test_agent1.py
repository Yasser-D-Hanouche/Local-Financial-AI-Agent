from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

def start_chat(retriever):
    print("\nStarting the Financial AI Assistant...")
    
    model = OllamaLLM(model="llama3.2:1b")

    template = """
    You are a financial advisor assistant. Use ONLY the following financial data to answer the question. 
    If the data doesn't contain enough information to answer, say "I don't have enough information to answer that question."

    FINANCIAL DATA: 
    {financial_data}

    QUESTION: 
    {question}

    Provide a clear, concise answer based on the data above.
    """

    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model

    print("Assistant is ready! (Type 'exit' or 'c' to quit)")
    
    while True:
        print("\n" + "-" * 40)
        question = input("Your question: ")
        
        if question.lower() in ['c', 'exit', 'quit']:
            print("Goodbye!")
            break
        
        data = retriever.invoke(question)
        print(f"[Debug] Found {len(data)} matching paragraphs from the database.")
        print("The AI is thinking. It may take a bit of time...")
        
        financial_data = "\n\n".join([doc.page_content for doc in data])
        
        result = chain.invoke({
            "financial_data": financial_data, 
            "question": question
        })
        
        print("\nAssistant:")
        print(result)