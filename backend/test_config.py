"""Test configuration and utilities"""

import os
import tempfile
from app import create_app
from database import db

class TestConfig:
    """Test configuration class"""
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'test-secret-key-not-for-production'
    
    @staticmethod
    def init_app(app):
        """Initialize test app"""
        pass

def create_test_app():
    """Create test application"""
    # Create temporary database
    db_fd, db_path = tempfile.mkstemp()
    
    app = create_app()
    app.config.update({
        'TESTING': True,
        'SQLALCHEMY_DATABASE_URI': f'sqlite:///{db_path}',
        'SQLALCHEMY_TRACK_MODIFICATIONS': False,
        'SECRET_KEY': 'test-secret-key',
        'WTF_CSRF_ENABLED': False
    })
    
    with app.app_context():
        db.create_all()
    
    return app, db_fd, db_path

def cleanup_test_app(db_fd, db_path):
    """Cleanup test application"""
    os.close(db_fd)
    os.unlink(db_path)