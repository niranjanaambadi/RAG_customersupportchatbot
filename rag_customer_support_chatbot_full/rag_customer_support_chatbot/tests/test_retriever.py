from retriever.vector_store import add_documents, retrieve_relevant_chunks

def test_retrieval():
    add_documents(["Reset password", "Change username"])
    results = retrieve_relevant_chunks("How to reset password?", k=1)
    assert "Reset password" in results