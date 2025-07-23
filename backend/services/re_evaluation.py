from services import benchmark_loader, gap_analyzer
from typing import List, Dict, Any

def re_evaluate(user_skills: List[str], job_role: str) -> Dict[str, Any]:
    """
    Re-evaluates the user's skill gaps based on updated skills or a new job role.

    Args:
        user_skills (List[str]): The updated list of user skills.
        job_role (str): The job role to re-analyze.

    Returns:
        Dict[str, Any]: Result of gap analysis, including job benchmark details and stats.
    """
    benchmark = benchmark_loader.get_benchmark_profile(job_role)
    if not benchmark:
        raise ValueError(f"No benchmark found for job role: {job_role}")

    required_skills = benchmark.get("required_skills", [])
    optional_skills = benchmark.get("optional_skills", [])

    gap_result = gap_analyzer.analyze_gap(user_skills, required_skills, optional_skills)

    return {
        "job_role": job_role,
        "user_skills": user_skills,
        "required_skills": required_skills,
        "optional_skills": optional_skills,
        "gap_analysis": gap_result
    }
