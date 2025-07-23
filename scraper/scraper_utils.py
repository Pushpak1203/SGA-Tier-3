import re
from typing import List, Dict


def clean_text(text: str) -> str:
    """
    Cleans a string by removing excessive whitespace, line breaks, and special characters.
    """
    if not text:
        return ""
    text = re.sub(r'\s+', ' ', text)  # Replace multiple spaces/newlines with single space
    return text.strip()


def extract_skills_from_bio(bio: str) -> List[str]:
    """
    Extract potential skills from a user's bio using simple keyword matching.
    (For improved results, integrate spaCy or ML models.)
    """
    tech_keywords = [
        "python", "java", "javascript", "c++", "flask", "django",
        "spring", "react", "node.js", "express", "git", "docker",
        "kubernetes", "aws", "azure", "sql", "mongodb", "html", "css"
    ]

    bio = bio.lower()
    found_skills = [kw for kw in tech_keywords if kw in bio]
    return list(set(found_skills))  # remove duplicates


def normalize_profile_data(raw_data: Dict) -> Dict:
    """
    Standardizes scraped profile data from various sources (LinkedIn, GitHub).
    """
    return {
        "name": clean_text(raw_data.get("name", "")),
        "headline": clean_text(raw_data.get("headline", "")),
        "location": clean_text(raw_data.get("location", "")),
        "skills": list(set(map(clean_text, raw_data.get("skills", []))))
    }


def merge_profiles(linkedin_data: Dict, github_data: Dict) -> Dict:
    """
    Merge LinkedIn and GitHub profile data into a unified user profile.
    """
    merged_skills = list(set(linkedin_data.get("skills", []) + github_data.get("skills", [])))

    return {
        "name": linkedin_data.get("name") or github_data.get("name") or "Unnamed User",
        "headline": linkedin_data.get("headline", ""),
        "location": linkedin_data.get("location", ""),
        "bio": github_data.get("bio", ""),
        "skills": merged_skills,
        "github": {
            "username": github_data.get("username", ""),
            "repos": github_data.get("repos", []),
        },
        "linkedin": {
            "profile_url": linkedin_data.get("profile_url", "")
        }
    }
