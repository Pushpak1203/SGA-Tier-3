from typing import List

# Predefined common technical and soft skills (can be expanded or dynamically loaded later)
COMMON_SKILLS = [
    # Programming Languages
    "python", "java", "c++", "javascript", "typescript", "go", "ruby", "rust",
    # Web
    "html", "css", "react", "angular", "vue", "node", "express", "flask", "django",
    # Database & DevOps
    "sql", "mysql", "postgresql", "mongodb", "firebase", "docker", "kubernetes", "aws", "azure", "gcp",
    # Data Science & ML
    "pandas", "numpy", "matplotlib", "seaborn", "scikit-learn", "tensorflow", "pytorch", "machine learning", "nlp",
    # Tools & Frameworks
    "git", "github", "linux", "jira", "ci/cd", "rest api", "graphql", "fastapi", "spring", "spring boot",
    # Soft Skills
    "communication", "teamwork", "problem solving", "leadership", "critical thinking", "time management"
]

def extract_skills(parsed_resume: dict) -> List[str]:
    """
    Extracts relevant skills from the parsed resume dictionary.

    Args:
        parsed_resume (dict): Parsed resume data containing 'skills' and/or 'raw_text'.

    Returns:
        List[str]: A list of detected skills from the resume.
    """
    skills = set()

    # Use provided skill list if available
    if "skills" in parsed_resume and isinstance(parsed_resume["skills"], list):
        for skill in parsed_resume["skills"]:
            if skill.lower() in COMMON_SKILLS:
                skills.add(skill.lower())

    # Also scan raw text for other matches
    if "raw_text" in parsed_resume:
        text = parsed_resume["raw_text"].lower()
        for skill in COMMON_SKILLS:
            if skill in text:
                skills.add(skill)

    return sorted(list(skills))
