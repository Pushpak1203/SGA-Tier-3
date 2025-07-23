import os
import re
import docx2txt
import pdfplumber

def extract_text_from_pdf(pdf_path: str) -> str:
    """
    Extracts text from a PDF file.
    """
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text


def extract_text_from_docx(docx_path: str) -> str:
    """
    Extracts text from a DOCX file.
    """
    return docx2txt.process(docx_path)


def extract_email(text: str) -> str:
    match = re.search(r"[\w\.-]+@[\w\.-]+\.\w+", text)
    return match.group(0) if match else None


def extract_phone(text: str) -> str:
    match = re.search(r"(\+?\d{1,3}[-.\s]?)?(\(?\d{3,5}\)?[-.\s]?)?[\d\s]{6,15}", text)
    return match.group(0).strip() if match else None


def extract_name(text: str) -> str:
    # Naive assumption: name is the first non-empty line with only alphabets
    for line in text.split("\n"):
        line = line.strip()
        if line and all(word.isalpha() for word in line.split()):
            return line
    return "Unknown"


def extract_skills(text: str) -> list:
    # Basic keyword-based skill matcher (improve with NLP later)
    common_skills = [
        "python", "java", "c++", "sql", "html", "css", "javascript", "react", "node",
        "spring", "flask", "django", "machine learning", "data analysis", "git",
        "docker", "kubernetes", "aws", "azure", "rest api", "tensorflow", "pandas",
        "numpy", "scikit-learn", "nlp", "fastapi", "kafka", "mongodb", "firebase"
    ]
    text_lower = text.lower()
    extracted = [skill for skill in common_skills if skill in text_lower]
    return sorted(list(set(extracted)))


def parse_resume(file_path: str) -> dict:
    """
    Parses the resume file and extracts basic candidate information.
    """
    ext = os.path.splitext(file_path)[-1].lower()

    if ext == ".pdf":
        raw_text = extract_text_from_pdf(file_path)
    elif ext == ".docx":
        raw_text = extract_text_from_docx(file_path)
    else:
        raise ValueError("Unsupported file format. Only PDF and DOCX are allowed.")

    parsed_data = {
        "name": extract_name(raw_text),
        "email": extract_email(raw_text),
        "phone": extract_phone(raw_text),
        "skills": extract_skills(raw_text),
        "raw_text": raw_text  # Optional: for advanced analysis
    }

    return parsed_data
