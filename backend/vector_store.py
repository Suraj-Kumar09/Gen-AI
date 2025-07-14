import faiss
import numpy as np

def build_faiss_index(vectors):
    dim = len(vectors[0])
    index = faiss.IndexFlatL2(dim)
    index.add(np.array(vectors).astype('float32'))
    return index

def search_faiss(index, query_vector, k=3):
    D, I = index.search(np.array([query_vector]).astype('float32'), k)
    return I[0], D[0]
