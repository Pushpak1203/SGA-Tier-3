from flask import Blueprint, request, jsonify
import uuid
import os
from werkzeug.utils import secure_filename

from services.resume_parser import parse_resume
from services.benchmark_loader import load_benchmark_profiles
from services.skill_matcher import match_skills
from services.gap_analyzer import generate_gap_report

upload_bp = Blueprint('upload', __name__)
UPLOAD_FOLDER = 'uploads/'
ALLOWED_EXTENSIONS = {'pdf', 'doc', 'docx'}

# Ensure uploads folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@upload_bp.route('/api/upload', methods=['POST'])
def upload_resume():
    if 'resume' not in request.files:
        return jsonify({'error': 'No resume file provided'}), 400

    resume_file = request.files['resume']
    user_data = request.form.to_dict()

    if resume_file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if resume_file and allowed_file(resume_file.filename):
        filename = secure_filename(resume_file.filename)
        user_id = str(uuid.uuid4())
        saved_path = os.path.join(UPLOAD_FOLDER, user_id + "_" + filename)
        resume_file.save(saved_path)

        # Parse the resume
        parsed_data = parse_resume(saved_path)

        # Load benchmark profiles
        benchmarks = load_benchmark_profiles()

        # Skill matching and gap analysis
        matched_skills = match_skills(parsed_data, benchmarks)
        report = generate_gap_report(parsed_data, matched_skills)

        # Save report
        report_path = f'reports/{user_id}_gap_report.json'
        os.makedirs('reports', exist_ok=True)
        with open(report_path, 'w') as f:
            import json
            json.dump(report, f, indent=2)

        # Return success
        return jsonify({
            'message': 'Resume uploaded and processed successfully',
            'user_id': user_id,
            'parsed_data': parsed_data,
            'report_url': f'/api/report/{user_id}'
        }), 200

    return jsonify({'error': 'Invalid file format'}), 400
