from fastapi import FastAPI
from pydantic import BaseModel
from ingestion.ingest_documents import load_kb
from retriever.vector_store import retrieve_relevant_chunks
from generator.llm_generator import generate_answer

app = FastAPI()
load_kb()

class Query(BaseModel):
    query: str

@app.post("/ask")
def ask(query: Query):
    context = retrieve_relevant_chunks(query.query)
    answer = generate_answer(query.query, context)
    return {"answer": answer}