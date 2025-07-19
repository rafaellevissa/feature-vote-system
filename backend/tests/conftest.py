import pytest
import os
import tempfile
from app import create_app
from database import db
from models.feature import Feature
from models.vote import Vote

@pytest.fixture
def app():
    """Create application for testing"""
    # Create a temporary file for the test database
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
        yield app
        db.drop_all()
    
    os.close(db_fd)
    os.unlink(db_path)

@pytest.fixture
def client(app):
    """Test client for making requests"""
    return app.test_client()

@pytest.fixture
def runner(app):
    """Test runner for CLI commands"""
    return app.test_cli_runner()

@pytest.fixture
def sample_feature_data():
    """Sample feature data for testing"""
    return {
        'title': 'Test Feature',
        'description': 'This is a test feature description',
        'author': 'Test Author'
    }

@pytest.fixture
def sample_feature(app):
    """Create a sample feature in the database"""
    with app.app_context():
        feature = Feature(
            title='Sample Feature',
            description='Sample description',
            author='Sample Author',
            upvotes=5
        )
        db.session.add(feature)
        db.session.commit()
        return feature