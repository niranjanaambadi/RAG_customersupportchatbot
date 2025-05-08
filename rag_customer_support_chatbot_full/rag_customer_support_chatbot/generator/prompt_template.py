def build_prompt(context, question):
    return f"""You are a helpful customer support assistant. Use the context below to answer the question accurately.

Context:
{context}

Question:
{question}

Answer:"""