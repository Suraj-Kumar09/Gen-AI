## Gen-AI
✅GenAI Document Assistant

A local, interactive AI assistant that reads user-uploaded documents (PDF/TXT) to provide deep comprehension, context-aware Q&A, and logic-based challenges with justifications grounded in the source document.

---
🔹Features

- **Document Upload:** Supports PDF and TXT files.  
- **Auto Summary:** Generates a concise ≤150-word summary immediately after upload.  
- **Ask Anything:** Free-form questions answered with contextual understanding and source justification.  
- **Challenge Me:** AI-generated comprehension and logic questions; evaluates user answers with detailed feedback.  
- **Justified Answers:** All responses are grounded with references to specific document sections.  
- **Local Web Interface:** Built with FastAPI backend and Streamlit frontend for smooth interaction.

---

💡Folder Structure

```bash
genai_assistant/
├── backend/
│   ├── app.py                ✅ ← You will run this
│   ├── parser.py
│   ├── summarizer.py
│   ├── embedder.py
│   ├── vector_store.py
│   ├── qa_answerer.py
│   └── challenge_me.py
├── data/
│   └── uploaded_docs/
├── frontend/
│   └──app.py      (optional UI)
├── requirements.txt

```
🛠 Usage
Upload a PDF or TXT document.

View the auto-generated summary.

Ask free-form questions about the document.

Use "Challenge Me" mode to answer AI-generated comprehension questions and receive feedback.

📜Dependencies
Python 3.8+

FastAPI

Uvicorn

Streamlit

Transformers (Hugging Face)

Sentence-Transformers

PyPDF2

FAISS

python-multipart

🔮Contributing
Contributions welcome! Please open issues or submit pull requests.

## NOTE:- In This projects upload any pdf or txt file and this GEN AI summerise this and Give output in MAX.>150 words.
