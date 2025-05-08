from ingestion.ingest_documents import load_kb
from retriever.vector_store import retrieve_relevant_chunks
from generator.llm_generator import generate_answer

def run_chatbot():
    load_kb()
    print("Chatbot is ready. Type 'exit' to quit.")
    while True:
        query = input("You: ")
        if query.lower() == "exit":
            break
        context = retrieve_relevant_chunks(query)
        answer = generate_answer(query, context)
        print(f"Bot: {answer}\n")

if __name__ == "__main__":
    run_chatbot()