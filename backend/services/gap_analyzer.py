from typing import List, Dict, Any

def analyze_gap(user_skills: List[str], required_skills: List[str], optional_skills: List[str]) -> Dict[str, Any]:
    """
    Analyze the user's skills to determine matched, missing, and optional overlaps.

    Args:
        user_skills (List[str]): Skills extracted from the user's resume.
        required_skills (List[str]): Skills required for the benchmark job role.
        optional_skills (List[str]): Optional skills for that job role.

    Returns:
        Dict[str, Any]: A dictionary containing:
            - matched_skills: skills both in user and required
            - missing_skills: required skills not in user
            - matched_optional: skills both in user and optional
            - remaining_optional: optional skills not in user
    """

    # Normalize to lowercase for case-insensitive comparison
    user_set = set(skill.strip().lower() for skill in user_skills)
    required_set = set(skill.strip().lower() for skill in required_skills)
    optional_set = set(skill.strip().lower() for skill in optional_skills)

    matched_skills = sorted([skill for skill in required_set if skill in user_set])
    missing_skills = sorted([skill for skill in required_set if skill not in user_set])

    matched_optional = sorted([skill for skill in optional_set if skill in user_set])
    remaining_optional = sorted([skill for skill in optional_set if skill not in user_set])

    return {
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "matched_optional": matched_optional,
        "remaining_optional": remaining_optional,
        "coverage_required": len(matched_skills) / len(required_set) if required_set else 0.0,
        "coverage_optional": len(matched_optional) / len(optional_set) if optional_set else 0.0
    }
