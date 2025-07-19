import pytest
import json
from models.feature import Feature
from models.vote import Vote
from database import db

class TestFeatureRoutes:
    """Test Feature API routes"""
    
    def test_get_features_empty(self, client):
        """Test getting features when none exist"""
        response = client.get('/api/features')
        
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data == []
    
    def test_get_features_with_data(self, client, app):
        """Test getting features with data"""
        with app.app_context():
            # Create test features
            feature1 = Feature(title='Feature 1', author='Author 1', upvotes=5)
            feature2 = Feature(title='Feature 2', author='Author 2', upvotes=10)
            db.session.add_all([feature1, feature2])
            db.session.commit()
        
        response = client.get('/api/features')
        
        assert response.status_code == 200
        data = json.loads(response.data)
        assert len(data) == 2
        # Should be ordered by upvotes (descending)
        assert data[0]['upvotes'] == 10
        assert data[1]['upvotes'] == 5
    
    def test_create_feature_success(self, client):
        """Test successful feature creation"""
        feature_data = {
            'title': 'API Test Feature',
            'description': 'Created via API',
            'author': 'API Author'
        }
        
        response = client.post('/api/features', 
                             data=json.dumps(feature_data),
                             content_type='application/json')
        
        assert response.status_code == 201
        data = json.loads(response.data)
        assert data['title'] == 'API Test Feature'
        assert data['description'] == 'Created via API'
        assert data['author'] == 'API Author'
        assert data['upvotes'] == 0
    
    def test_create_feature_missing_data(self, client):
        """Test feature creation with missing data"""
        # Missing title
        feature_data = {'author': 'Author'}
        
        response = client.post('/api/features',
                             data=json.dumps(feature_data),
                             content_type='application/json')
        
        assert response.status_code == 400
        data = json.loads(response.data)
        assert 'error' in data
    
    def test_create_feature_no_data(self, client):
        """Test feature creation with no data"""
        response = client.post('/api/features')
        
        assert response.status_code == 400
        data = json.loads(response.data)
        assert data['error'] == 'No data provided'
    
    def test_get_feature_success(self, client, app):
        """Test getting specific feature"""
        with app.app_context():
            feature = Feature(title='Test Feature', author='Test Author')
            db.session.add(feature)
            db.session.commit()
            feature_id = feature.id
        
        response = client.get(f'/api/features/{feature_id}')
        
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['id'] == feature_id
        assert data['title'] == 'Test Feature'
    
    def test_get_feature_not_found(self, client):
        """Test getting non-existent feature"""
        response = client.get('/api/features/999')
        
        assert response.status_code == 404
        data = json.loads(response.data)
        assert data['error'] == 'Feature not found'
    
    def test_delete_feature_success(self, client, app):
        """Test successful feature deletion"""
        with app.app_context():
            feature = Feature(title='Delete Me', author='Author')
            db.session.add(feature)
            db.session.commit()
            feature_id = feature.id
        
        response = client.delete(f'/api/features/{feature_id}')
        
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['message'] == 'Feature deleted successfully'
    
    def test_delete_feature_not_found(self, client):
        """Test deleting non-existent feature"""
        response = client.delete('/api/features/999')
        
        assert response.status_code == 404
        data = json.loads(response.data)
        assert data['error'] == 'Feature not found'
    
    def test_upvote_feature_success(self, client, app):
        """Test successful feature upvoting"""
        with app.app_context():
            feature = Feature(title='Upvote Me', author='Author', upvotes=0)
            db.session.add(feature)
            db.session.commit()
            feature_id = feature.id
        
        vote_data = {'user_id': 'test_user_123'}
        
        response = client.post(f'/api/features/{feature_id}/upvote',
                             data=json.dumps(vote_data),
                             content_type='application/json')
        
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['upvotes'] == 1
    
    def test_upvote_feature_missing_user_id(self, client, app):
        """Test upvoting without user ID"""
        with app.app_context():
            feature = Feature(title='Feature', author='Author')
            db.session.add(feature)
            db.session.commit()
            feature_id = feature.id
        
        response = client.post(f'/api/features/{feature_id}/upvote',
                             data=json.dumps({}),
                             content_type='application/json')
        
        assert response.status_code == 400
        data = json.loads(response.data)
        assert 'error' in data
    
    def test_remove_vote_success(self, client, app):
        """Test successful vote removal"""
        with app.app_context():
            feature = Feature(title='Feature', author='Author', upvotes=1)
            vote = Vote(feature_id=1, user_id='test_user')
            db.session.add_all([feature, vote])
            db.session.commit()
            feature_id = feature.id
        
        vote_data = {'user_id': 'test_user'}
        
        response = client.delete(f'/api/features/{feature_id}/remove-vote',
                               data=json.dumps(vote_data),
                               content_type='application/json')
        
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['upvotes'] == 0
    
    def test_get_user_votes(self, client, app):
        """Test getting user votes"""
        with app.app_context():
            feature1 = Feature(title='Feature 1', author='Author 1')
            feature2 = Feature(title='Feature 2', author='Author 2')
            db.session.add_all([feature1, feature2])
            db.session.commit()
            
            vote1 = Vote(feature_id=feature1.id, user_id='test_user')
            vote2 = Vote(feature_id=feature2.id, user_id='test_user')
            db.session.add_all([vote1, vote2])
            db.session.commit()
        
        response = client.get('/api/user/test_user/votes')
        
        assert response.status_code == 200
        data = json.loads(response.data)
        assert len(data) == 2
        assert feature1.id in data
        assert feature2.id in data

class TestHealthRoutes:
    """Test Health check routes"""
    
    def test_health_check(self, client):
        """Test health check endpoint"""
        response = client.get('/api/health')
        
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['status'] == 'healthy'
        assert 'timestamp' in data
        assert data['service'] == 'feature-voting-api'