from flask import Blueprint, request, jsonify
import json
import os

dashboard_bp = Blueprint("dashboard", __name__)

USER_PROFILE_PATH = os.path.join("database", "user_profiles.json")


def load_user_profiles():
    if not os.path.exists(USER_PROFILE_PATH):
        return []

    with open(USER_PROFILE_PATH, "r") as f:
        return json.load(f)


@dashboard_bp.route("/dashboard/<user_id>", methods=["GET"])
def get_user_dashboard(user_id):
    try:
        users = load_user_profiles()
        user_data = next((user for user in users if user["user_id"] == user_id), None)

        if not user_data:
            return jsonify({"error": f"No data found for user_id: {user_id}"}), 404

        dashboard_data = {
            "user_id": user_id,
            "name": user_data.get("name", "N/A"),
            "email": user_data.get("email", "N/A"),
            "analyzed_roles": user_data.get("roles_analyzed", []),
            "last_analysis": user_data.get("last_analysis", {}),
            "recommended_skills": user_data.get("recommended_skills", []),
            "strengths": user_data.get("strengths", [])
        }

        return jsonify(dashboard_data), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
