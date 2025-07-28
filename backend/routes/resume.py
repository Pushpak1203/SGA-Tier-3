from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename
import os

from services.parser_engine import parse_resume

resume_bp = Blueprint('resume_bp', __name__)

# Directory to temporarily save uploaded resumes
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
ALLOWED_EXTENSIONS = {'pdf', 'docx'}

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@resume_bp.route('/upload_resume', methods=['POST'])
def upload_resume():
    try:
        if 'file' not in request.files:
            return jsonify({"error": "No file part in the request"}), 400

        file = request.files['file']
        user_id = request.form.get('user_id', 'anonymous')

        if file.filename == '':
            return jsonify({"error": "No selected file"}), 400

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(UPLOAD_FOLDER, filename)
            file.save(filepath)

            # Call resume parser
            parsed_data = parse_resume(filepath, user_id)

            # Optional: remove the file after parsing
            os.remove(filepath)

            return jsonify({
                "message": "Resume parsed successfully",
                "user_id": user_id,
                "parsed_data": parsed_data
            }), 200
        else:
            return jsonify({"error": "Invalid file format. Only PDF and DOCX allowed."}), 400

    except Exception as e:
        return jsonify({"error": str(e)}), 500
