from flask import Blueprint, request, jsonify
from services import skill_matcher, benchmark_loader, gap_analyzer

analyze_bp = Blueprint("analyze", __name__)

@analyze_bp.route("/analyze", methods=["POST"])
def analyze_skills():
    try:
        data = request.get_json()

        if not data or "parsed_resume" not in data or "job_role" not in data:
            return jsonify({"error": "Missing required fields"}), 400

        parsed_resume = data["parsed_resume"]
        job_role = data["job_role"]

        # Extract skills from resume
        user_skills = skill_matcher.extract_skills(parsed_resume)

        # Load benchmark profile for the given job role
        benchmark = benchmark_loader.get_benchmark_profile(job_role)
        if not benchmark:
            return jsonify({"error": f"No benchmark found for role: {job_role}"}), 404

        required_skills = benchmark.get("required_skills", [])
        optional_skills = benchmark.get("optional_skills", [])

        # Perform gap analysis
        gap_result = gap_analyzer.analyze_gap(user_skills, required_skills, optional_skills)

        return jsonify({
            "user_skills": user_skills,
            "required_skills": required_skills,
            "optional_skills": optional_skills,
            "gap_analysis": gap_result,
            "job_role": job_role
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
