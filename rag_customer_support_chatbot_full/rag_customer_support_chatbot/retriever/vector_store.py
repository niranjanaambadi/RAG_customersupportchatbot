import faiss
import numpy as np
from retriever.embedding import get_embedding_model, embed_text

embedding_model = get_embedding_model()

# In-memory FAISS index and document store
dimension = 384  # Dimension for MiniLM embeddings
index = faiss.IndexFlatL2(dimension)
documents = []

def add_documents(docs):
    global documents
    embeddings = [embed_text(embedding_model, doc) for doc in docs]
    vectors = np.stack([e.cpu().numpy() for e in embeddings])
    index.add(vectors)
    documents.extend(docs)

def retrieve_relevant_chunks(query, k=3):
    query_embedding = embed_text(embedding_model, query).cpu().numpy().reshape(1, -1)
    _, I = index.search(query_embedding, k)
    return [documents[i] for i in I[0] if i < len(documents)]