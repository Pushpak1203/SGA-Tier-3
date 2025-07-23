import os

class Config:
    """
    Base configuration class for the Flask app.
    """

    # Flask settings
    DEBUG = True
    TESTING = False
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev_secret_key")

    # Uploads
    UPLOAD_FOLDER = os.path.join(os.getcwd(), "uploads")
    ALLOWED_EXTENSIONS = {"pdf", "docx"}
    MAX_CONTENT_LENGTH = 5 * 1024 * 1024  # 5 MB

    # Database / file paths
    BENCHMARK_PROFILE_PATH = os.path.join("database", "benchmark_profiles.json")
    USER_PROFILE_PATH = os.path.join("database", "user_profiles.json")
    REPORTS_DIR = os.path.join(os.getcwd(), "reports")

    # CORS settings
    CORS_ORIGINS = "*"

    # Logging (optional)
    LOGGING_LEVEL = "INFO"


def allowed_file(filename: str) -> bool:
    """
    Checks if the uploaded file has an allowed extension.

    Args:
        filename (str): The name of the uploaded file.

    Returns:
        bool: True if file extension is allowed, else False.
    """
    return "." in filename and filename.rsplit(".", 1)[1].lower() in Config.ALLOWED_EXTENSIONS
