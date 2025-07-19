import pytest
from services.feature_service import FeatureService
from services.vote_service import VoteService
from models.feature import Feature
from models.vote import Vote
from database import db

class TestFeatureService:
    """Test Feature service"""
    
    def test_create_feature_success(self, app):
        """Test successful feature creation"""
        with app.app_context():
            service = FeatureService()
            
            feature_data = service.create_feature(
                title='Service Test Feature',
                author='Service Author',
                description='Service test description'
            )
            
            assert 'id' in feature_data
            assert feature_data['title'] == 'Service Test Feature'
            assert feature_data['author'] == 'Service Author'
            assert feature_data['description'] == 'Service test description'
            assert feature_data['upvotes'] == 0
    
    def test_create_feature_validation_error(self, app):
        """Test feature creation with missing required fields"""
        with app.app_context():
            service = FeatureService()
            
            # Missing title
            with pytest.raises(ValueError, match="Title and author are required"):
                service.create_feature(title='', author='Author')
            
            # Missing author
            with pytest.raises(ValueError, match="Title and author are required"):
                service.create_feature(title='Title', author='')
    
    def test_get_all_features(self, app):
        """Test getting all features"""
        with app.app_context():
            service = FeatureService()
            
            # Create test features
            service.create_feature('Feature 1', 'Author 1')
            service.create_feature('Feature 2', 'Author 2')
            
            features = service.get_all_features()
            
            assert len(features) == 2
            assert all('id' in feature for feature in features)
            assert all('title' in feature for feature in features)
    
    def test_get_feature_by_id(self, app):
        """Test getting feature by ID"""
        with app.app_context():
            service = FeatureService()
            
            # Create feature
            created_feature = service.create_feature('Test Feature', 'Test Author')
            feature_id = created_feature['id']
            
            # Get feature by ID
            found_feature = service.get_feature_by_id(feature_id)
            
            assert found_feature is not None
            assert found_feature['id'] == feature_id
            assert found_feature['title'] == 'Test Feature'
            assert found_feature['author'] == 'Test Author'
    
    def test_get_feature_by_id_not_found(self, app):
        """Test getting non-existent feature"""
        with app.app_context():
            service = FeatureService()
            
            feature = service.get_feature_by_id(999)
            
            assert feature is None
    
    def test_delete_feature_success(self, app):
        """Test successful feature deletion"""
        with app.app_context():
            service = FeatureService()
            
            # Create feature
            created_feature = service.create_feature('Delete Me', 'Author')
            feature_id = created_feature['id']
            
            # Delete feature
            result = service.delete_feature(feature_id)
            
            assert result is True
            
            # Verify deletion
            deleted_feature = service.get_feature_by_id(feature_id)
            assert deleted_feature is None
    
    def test_delete_feature_not_found(self, app):
        """Test deleting non-existent feature"""
        with app.app_context():
            service = FeatureService()
            
            result = service.delete_feature(999)
            
            assert result is False

class TestVoteService:
    """Test Vote service"""
    
    def test_upvote_feature_success(self, app, sample_feature):
        """Test successful feature upvoting"""
        with app.app_context():
            service = VoteService()
            
            initial_upvotes = sample_feature.upvotes
            
            result = service.upvote_feature(sample_feature.id, 'test_user')
            
            assert 'id' in result
            assert result['upvotes'] == initial_upvotes + 1
    
    def test_upvote_feature_not_found(self, app):
        """Test upvoting non-existent feature"""
        with app.app_context():
            service = VoteService()
            
            with pytest.raises(ValueError, match="Feature not found"):
                service.upvote_feature(999, 'test_user')
    
    def test_upvote_feature_duplicate_vote(self, app, sample_feature):
        """Test upvoting feature twice by same user"""
        with app.app_context():
            service = VoteService()
            
            # First upvote
            service.upvote_feature(sample_feature.id, 'test_user')
            
            # Second upvote should fail
            with pytest.raises(ValueError, match="User already voted"):
                service.upvote_feature(sample_feature.id, 'test_user')
    
    def test_upvote_feature_missing_user_id(self, app, sample_feature):
        """Test upvoting without user ID"""
        with app.app_context():
            service = VoteService()
            
            with pytest.raises(ValueError, match="User ID is required"):
                service.upvote_feature(sample_feature.id, '')
    
    def test_remove_vote_success(self, app, sample_feature):
        """Test successful vote removal"""
        with app.app_context():
            service = VoteService()
            
            # First upvote
            service.upvote_feature(sample_feature.id, 'test_user')
            upvotes_after_vote = sample_feature.upvotes + 1
            
            # Remove vote
            result = service.remove_vote(sample_feature.id, 'test_user')
            
            assert result['upvotes'] == upvotes_after_vote - 1
    
    def test_remove_vote_not_found(self, app, sample_feature):
        """Test removing non-existent vote"""
        with app.app_context():
            service = VoteService()
            
            with pytest.raises(ValueError, match="Vote not found"):
                service.remove_vote(sample_feature.id, 'test_user')
    
    def test_get_user_votes(self, app):
        """Test getting user votes"""
        with app.app_context():
            service = VoteService()
            
            # Create features
            feature1 = Feature(title='Feature 1', author='Author 1')
            feature2 = Feature(title='Feature 2', author='Author 2')
            db.session.add_all([feature1, feature2])
            db.session.commit()
            
            # Upvote features
            service.upvote_feature(feature1.id, 'test_user')
            service.upvote_feature(feature2.id, 'test_user')
            
            # Get user votes
            user_votes = service.get_user_votes('test_user')
            
            assert len(user_votes) == 2
            assert feature1.id in user_votes
            assert feature2.id in user_votes