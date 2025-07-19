from flask import Flask
from flask_cors import CORS
from database import db, init_db
from routes.feature_routes import feature_bp
from routes.health_routes import health_bp
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Initialize database
    db.init_app(app)
    
    # Enable CORS
    CORS(app)
    
    # Register blueprints
    app.register_blueprint(feature_bp, url_prefix='/api')
    app.register_blueprint(health_bp, url_prefix='/api')
    
    return app

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        init_db()
    app.run(debug=True, host='0.0.0.0', port=5000)
