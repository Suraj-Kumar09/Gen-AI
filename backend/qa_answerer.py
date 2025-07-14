from sentence_transformers import SentenceTransformer
from .vector_store import search_faiss
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

def answer_question(query, chunks, embeddings, index, k=3):
    query_embedding = model.encode(query)
    top_k_idx, _ = search_faiss(index, query_embedding, k)
    
    context = "\n\n".join([chunks[i] for i in top_k_idx])
    justification = f"This is supported by content found in {len(top_k_idx)} similar chunks."
    answer = f"Based on the document, here's a relevant answer:\n{context[:300]}..."  # Stub
    
    return answer, justification
