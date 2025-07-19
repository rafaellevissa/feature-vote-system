import pytest
from repositories.feature_repository import FeatureRepository
from repositories.vote_repository import VoteRepository
from models.feature import Feature
from models.vote import Vote
from database import db

class TestFeatureRepository:
    """Test Feature repository"""
    
    def test_create_feature(self, app):
        """Test creating a feature through repository"""
        with app.app_context():
            repo = FeatureRepository()
            feature = repo.create(
                title='Repo Test Feature',
                description='Created via repository',
                author='Repo Author'
            )
            
            assert feature.id is not None
            assert feature.title == 'Repo Test Feature'
            assert feature.description == 'Created via repository'
            assert feature.author == 'Repo Author'
    
    def test_get_all_ordered_by_votes(self, app):
        """Test getting features ordered by votes"""
        with app.app_context():
            repo = FeatureRepository()
            
            # Create features with different vote counts
            feature1 = repo.create(title='Feature 1', author='Author 1')
            feature2 = repo.create(title='Feature 2', author='Author 2')
            feature3 = repo.create(title='Feature 3', author='Author 3')
            
            # Set different upvote counts
            feature1.upvotes = 10
            feature2.upvotes = 5
            feature3.upvotes = 15
            db.session.commit()
            
            # Get ordered features
            features = repo.get_all_ordered_by_votes()
            
            assert len(features) == 3
            assert features[0].upvotes == 15  # Highest first
            assert features[1].upvotes == 10
            assert features[2].upvotes == 5   # Lowest last
    
    def test_increment_upvotes(self, app):
        """Test incrementing feature upvotes"""
        with app.app_context():
            repo = FeatureRepository()
            feature = repo.create(title='Test Feature', author='Test Author')
            
            initial_upvotes = feature.upvotes
            updated_feature = repo.increment_upvotes(feature)
            
            assert updated_feature.upvotes == initial_upvotes + 1
    
    def test_decrement_upvotes(self, app):
        """Test decrementing feature upvotes"""
        with app.app_context():
            repo = FeatureRepository()
            feature = repo.create(title='Test Feature', author='Test Author')
            feature.upvotes = 5
            db.session.commit()
            
            updated_feature = repo.decrement_upvotes(feature)
            
            assert updated_feature.upvotes == 4
    
    def test_decrement_upvotes_minimum_zero(self, app):
        """Test that upvotes don't go below zero"""
        with app.app_context():
            repo = FeatureRepository()
            feature = repo.create(title='Test Feature', author='Test Author')
            
            # Feature starts with 0 upvotes
            updated_feature = repo.decrement_upvotes(feature)
            
            assert updated_feature.upvotes == 0  # Should stay at 0

class TestVoteRepository:
    """Test Vote repository"""
    
    def test_get_user_votes(self, app, sample_feature):
        """Test getting user votes"""
        with app.app_context():
            repo = VoteRepository()
            
            # Create votes for user
            vote1 = repo.create(feature_id=sample_feature.id, user_id='test_user')
            
            # Create another feature and vote
            feature2 = Feature(title='Feature 2', author='Author 2')
            db.session.add(feature2)
            db.session.commit()
            
            vote2 = repo.create(feature_id=feature2.id, user_id='test_user')
            
            # Get user votes
            user_votes = repo.get_user_votes('test_user')
            
            assert len(user_votes) == 2
            assert vote1 in user_votes
            assert vote2 in user_votes
    
    def test_get_user_feature_vote(self, app, sample_feature):
        """Test getting specific user-feature vote"""
        with app.app_context():
            repo = VoteRepository()
            
            # Create vote
            vote = repo.create(feature_id=sample_feature.id, user_id='test_user')
            
            # Get specific vote
            found_vote = repo.get_user_feature_vote('test_user', sample_feature.id)
            
            assert found_vote is not None
            assert found_vote.id == vote.id
            assert found_vote.user_id == 'test_user'
            assert found_vote.feature_id == sample_feature.id
    
    def test_get_user_voted_feature_ids(self, app):
        """Test getting feature IDs user has voted for"""
        with app.app_context():
            repo = VoteRepository()
            
            # Create features
            feature1 = Feature(title='Feature 1', author='Author 1')
            feature2 = Feature(title='Feature 2', author='Author 2')
            db.session.add_all([feature1, feature2])
            db.session.commit()
            
            # Create votes
            repo.create(feature_id=feature1.id, user_id='test_user')
            repo.create(feature_id=feature2.id, user_id='test_user')
            
            # Get voted feature IDs
            feature_ids = repo.get_user_voted_feature_ids('test_user')
            
            assert len(feature_ids) == 2
            assert feature1.id in feature_ids
            assert feature2.id in feature_ids