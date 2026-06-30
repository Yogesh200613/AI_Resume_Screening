from docx import Document

def extract_text(filepath):
    text = ""

    # PDF Resume
    if filepath.lower().endswith(".pdf"):
        import pdfplumber

        with pdfplumber.open(filepath) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()

                if page_text:
                    text += page_text + "\n"

    # DOCX Resume
    elif filepath.lower().endswith(".docx"):

        doc = Document(filepath)

        for para in doc.paragraphs:
            text += para.text + "\n"

    return text