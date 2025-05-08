import streamlit as st
from ingestion.ingest_documents import load_kb
from retriever.vector_store import retrieve_relevant_chunks
from generator.llm_generator import generate_answer

st.title("Customer Support Chatbot")
load_kb()

query = st.text_input("Ask a question:")
if query:
    context = retrieve_relevant_chunks(query)
    answer = generate_answer(query, context)
    st.write("### Answer:")
    st.write(answer)