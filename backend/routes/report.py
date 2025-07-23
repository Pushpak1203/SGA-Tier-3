from flask import Blueprint, request, jsonify, send_file
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import os
import uuid
import datetime
import json

report_bp = Blueprint("report", __name__)

REPORTS_DIR = "reports"
if not os.path.exists(REPORTS_DIR):
    os.makedirs(REPORTS_DIR)

@report_bp.route("/generate_report", methods=["POST"])
def generate_report():
    try:
        data = request.get_json()

        required_fields = ["user_id", "user_name", "job_role", "user_skills", "required_skills", "optional_skills", "gap_analysis"]
        if not all(field in data for field in required_fields):
            return jsonify({"error": "Missing required fields in request"}), 400

        # Prepare filename and path
        report_id = str(uuid.uuid4())
        filename = f"{report_id}_{data['user_id']}.pdf"
        filepath = os.path.join(REPORTS_DIR, filename)

        # Generate PDF using reportlab
        c = canvas.Canvas(filepath, pagesize=A4)
        width, height = A4
        y = height - 50

        def draw_line(text, step=20):
            nonlocal y
            if y < 60:
                c.showPage()
                y = height - 50
            c.drawString(50, y, text)
            y -= step

        # Report content
        draw_line(f"Skill Gap Analysis Report", step=30)
        draw_line(f"Generated for: {data['user_name']} ({data['user_id']})")
        draw_line(f"Job Role: {data['job_role']}")
        draw_line(f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        draw_line("")

        draw_line("User Skills:")
        for skill in data["user_skills"]:
            draw_line(f"  - {skill}")

        draw_line("")
        draw_line("Required Skills:")
        for skill in data["required_skills"]:
            draw_line(f"  - {skill}")

        draw_line("")
        draw_line("Optional Skills:")
        for skill in data["optional_skills"]:
            draw_line(f"  - {skill}")

        draw_line("")
        draw_line("Gap Analysis:")
        draw_line(f"  Missing Skills: {', '.join(data['gap_analysis'].get('missing_skills', []))}")
        draw_line(f"  Matched Skills: {', '.join(data['gap_analysis'].get('matched_skills', []))}")

        c.save()

        return jsonify({"message": "Report generated successfully", "report_path": filepath, "download_url": f"/download_report/{filename}"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@report_bp.route("/download_report/<filename>", methods=["GET"])
def download_report(filename):
    try:
        filepath = os.path.join(REPORTS_DIR, filename)
        if not os.path.exists(filepath):
            return jsonify({"error": "Report not found"}), 404
        return send_file(filepath, as_attachment=True)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
