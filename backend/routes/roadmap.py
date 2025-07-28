from flask import Blueprint, request, jsonify
from services.roadmap_generator import generate_roadmap

roadmap_bp = Blueprint('roadmap_bp', __name__)

@roadmap_bp.route('/generate_roadmap', methods=['POST'])
def generate_learning_roadmap():
    try:
        data = request.get_json()
        user_id = data.get('user_id')
        missing_skills = data.get('missing_skills', [])

        if not user_id or not missing_skills:
            return jsonify({"error": "Missing user_id or missing_skills"}), 400

        # Generate a personalized learning roadmap
        roadmap = generate_roadmap(user_id, missing_skills)

        return jsonify({
            "message": "Roadmap generated successfully",
            "user_id": user_id,
            "roadmap": roadmap
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
