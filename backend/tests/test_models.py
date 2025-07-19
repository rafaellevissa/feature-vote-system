import pytest
from datetime import datetime
from models.feature import Feature
from models.vote import Vote
from database import db

class TestFeatureModel:
    """Test Feature model"""
    
    def test_create_feature(self, app):
        """Test creating a feature"""
        with app.app_context():
            feature = Feature(
                title='Test Feature',
                description='Test description',
                author='Test Author'
            )
            db.session.add(feature)
            db.session.commit()
            
            assert feature.id is not None
            assert feature.title == 'Test Feature'
            assert feature.description == 'Test description'
            assert feature.author == 'Test Author'
            assert feature.upvotes == 0
            assert isinstance(feature.created_at, datetime)
            assert isinstance(feature.updated_at, datetime)
    
    def test_feature_representation(self, app):
        """Test feature string representation"""
        with app.app_context():
            feature = Feature(title='Test Feature', author='Test Author')
            assert str(feature) == '<Feature Test Feature>'
    
    def test_feature_to_dict(self, app):
        """Test feature to dictionary conversion"""
        with app.app_context():
            feature = Feature(
                title='Test Feature',
                description='Test description',
                author='Test Author'
            )
            db.session.add(feature)
            db.session.commit()
            
            feature_dict = feature.to_dict()
            
            assert 'id' in feature_dict
            assert feature_dict['title'] == 'Test Feature'
            assert feature_dict['description'] == 'Test description'
            assert feature_dict['author'] == 'Test Author'
            assert feature_dict['upvotes'] == 0
            assert 'created_at' in feature_dict
            assert 'updated_at' in feature_dict
            assert 'votes_count' in feature_dict

class TestVoteModel:
    """Test Vote model"""
    
    def test_create_vote(self, app, sample_feature):
        """Test creating a vote"""
        with app.app_context():
            vote = Vote(
                feature_id=sample_feature.id,
                user_id='test_user_123'
            )
            db.session.add(vote)
            db.session.commit()
            
            assert vote.id is not None
            assert vote.feature_id == sample_feature.id
            assert vote.user_id == 'test_user_123'
            assert isinstance(vote.created_at, datetime)
    
    def test_vote_representation(self, app, sample_feature):
        """Test vote string representation"""
        with app.app_context():
            vote = Vote(feature_id=sample_feature.id, user_id='test_user')
            expected = f'<Vote user:test_user feature:{sample_feature.id}>'
            assert str(vote) == expected
    
    def test_unique_constraint(self, app, sample_feature):
        """Test unique constraint on user-feature voting"""
        with app.app_context():
            # Create first vote
            vote1 = Vote(feature_id=sample_feature.id, user_id='test_user')
            db.session.add(vote1)
            db.session.commit()
            
            # Try to create duplicate vote
            vote2 = Vote(feature_id=sample_feature.id, user_id='test_user')
            db.session.add(vote2)
            
            with pytest.raises(Exception):  # Should raise IntegrityError
                db.session.commit()
