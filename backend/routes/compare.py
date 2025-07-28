from flask import Blueprint, request, jsonify

from services.skill_matcher import compare_skills_with_benchmark

compare_bp = Blueprint('compare_bp', __name__)

@compare_bp.route('/compare_skills', methods=['POST'])
def compare_skills():
    try:
        data = request.get_json()
        user_id = data.get('user_id')
        user_skills = data.get('skills', [])

        if not user_id or not user_skills:
            return jsonify({"error": "Missing user_id or skills in request body"}), 400

        # Call the service to compare user skills with benchmark
        comparison_result = compare_skills_with_benchmark(user_skills)

        return jsonify({
            "message": "Skill comparison completed successfully",
            "user_id": user_id,
            "comparison_result": comparison_result
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
