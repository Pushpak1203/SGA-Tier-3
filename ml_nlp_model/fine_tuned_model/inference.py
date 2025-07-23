import os
import json
import spacy
from typing import List, Dict

# Load the NLP model
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'fine_tuned_model')
try:
    nlp = spacy.load(MODEL_PATH)
except Exception as e:
    print(f"[ERROR] Could not load NLP model from {MODEL_PATH}")
    raise e

# Predefined skill keywords (can be replaced with vector-based similarity)
with open(os.path.join(MODEL_PATH, "skill_list.json"), "r") as f:
    KNOWN_SKILLS = set(json.load(f))  # List like ["Python", "Java", "Docker", ...]

def extract_entities(text: str) -> Dict[str, List[str]]:
    """
    Extract named entities such as NAME, ORG, DEGREE from the resume text.
    """
    doc = nlp(text)
    entities = {"NAME": [], "ORG": [], "DEGREE": []}

    for ent in doc.ents:
        if ent.label_ in entities:
            entities[ent.label_].append(ent.text.strip())

    return entities

def extract_skills(text: str) -> List[str]:
    """
    Extract known skills from resume text using keyword matching.
    (Future: use embedding similarity here)
    """
    found_skills = []
    text_lower = text.lower()

    for skill in KNOWN_SKILLS:
        if skill.lower() in text_lower:
            found_skills.append(skill)

    return list(set(found_skills))

def parse_resume(text: str) -> Dict:
    """
    End-to-end resume parsing: entities + skills.
    """
    return {
        "entities": extract_entities(text),
        "skills": extract_skills(text)
    }

# For CLI testing
if __name__ == "__main__":
    test_file = os.path.join(os.path.dirname(__file__), "sample_resume.txt")
    with open(test_file, "r", encoding="utf-8") as f:
        resume_text = f.read()

    parsed = parse_resume(resume_text)
    print(json.dumps(parsed, indent=2))
