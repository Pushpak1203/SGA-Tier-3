from flask import Flask
from flask_cors import CORS
from config import Config

# Import Blueprints
from routes.upload import upload_bp
from routes.analyze import analyze_bp
from routes.report import report_bp
from routes.dashboard import dashboard_bp

def create_app():
    app = Flask(__name__)
    
    # Load config
    app.config.from_object(Config)

    # Enable CORS
    CORS(app, resources={r"/*": {"origins": Config.CORS_ORIGINS}})

    # Register Blueprints
    app.register_blueprint(upload_bp, url_prefix="/api")
    app.register_blueprint(analyze_bp, url_prefix="/api")
    app.register_blueprint(report_bp, url_prefix="/api")
    app.register_blueprint(dashboard_bp, url_prefix="/api")

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000, debug=Config.DEBUG)
