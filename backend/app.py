from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import os
import tempfile

from backend.my_parser import extract_text

from .summarizer import summarize_text

from .embedder import chunk_text, embed_chunks

from .vector_store import build_faiss_index, search_faiss

from .qa_answerer import answer_question
from .challenge_me import generate_questions, evaluate_answer


app = FastAPI()

# Allow frontend (e.g., Streamlit or React) to access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global memory
doc_text = ""
chunks = []
embeddings = []
index = None

@app.get("/")
def root():
    return {"message": "GenAI Assistant API is running"}

@app.post("/upload/")
async def upload_doc(file: UploadFile = File(...)):
    global doc_text, chunks, embeddings, index

    ext = file.filename.split(".")[-1].lower()
    tmp_dir = tempfile.mkdtemp()
    path = os.path.join(tmp_dir, file.filename)

    with open(path, "wb") as f:
        f.write(await file.read())

    doc_text = extract_text(path)
    summary = summarize_text(doc_text)
    chunks = chunk_text(doc_text)
    embeddings = embed_chunks(chunks)
    index = build_faiss_index(embeddings)

    return {"summary": summary}

@app.post("/ask/")
async def ask(query: str = Form(...)):
    if index is None:
        return JSONResponse(status_code=400, content={"error": "Document not uploaded"})

    answer, context = answer_question(query, chunks, embeddings, index)
    return {"answer": answer, "justification": context}

@app.get("/challenge/")
async def challenge():
    if not doc_text:
        return JSONResponse(status_code=400, content={"error": "Document not uploaded"})

    questions = generate_questions(doc_text)
    return {"questions": questions}

@app.post("/evaluate/")
async def evaluate(question: str = Form(...), user_answer: str = Form(...)):
    if not doc_text:
        return JSONResponse(status_code=400, content={"error": "Document not uploaded"})

    feedback = evaluate_answer(question, user_answer, doc_text)
    return {"evaluation": feedback}
