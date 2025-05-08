from sentence_transformers import SentenceTransformer

def get_embedding_model(model_name='all-MiniLM-L6-v2'):
    return SentenceTransformer(model_name)

def embed_text(model, text):
    return model.encode(text, convert_to_tensor=True)