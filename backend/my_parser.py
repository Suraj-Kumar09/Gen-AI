import fitz  # PyMuPDF

def extract_text(file_path: str) -> str:
    if file_path.endswith('.pdf'):
        doc = fitz.open(file_path)
        return ' '.join(page.get_text() for page in doc)
    elif file_path.endswith('.txt'):
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    else:
        raise ValueError('Unsupported file format.')
