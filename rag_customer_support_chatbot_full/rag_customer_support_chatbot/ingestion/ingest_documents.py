from retriever.vector_store import add_documents

def load_kb(file_path="data/example_kb.txt"):
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()
    chunks = [chunk.strip() for chunk in text.split("\n") if chunk.strip()]
    add_documents(chunks)
    print("Knowledge base ingested successfully.")

if __name__ == "__main__":
    load_kb()