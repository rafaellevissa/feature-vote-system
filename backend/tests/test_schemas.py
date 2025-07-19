import pytest
from schemas.feature_schemas import CreateFeatureRequest, VoteRequest

class TestCreateFeatureRequest:
    """Test CreateFeatureRequest schema"""
    
    def test_valid_request(self):
        """Test valid feature request"""
        data = {
            'title': 'Valid Feature',
            'author': 'Valid Author',
            'description': 'Valid description'
        }
        
        request = CreateFeatureRequest.from_dict(data)
        request.validate()  # Should not raise
        
        assert request.title == 'Valid Feature'
        assert request.author == 'Valid Author'
        assert request.description == 'Valid description'
    
    def test_missing_title(self):
        """Test request with missing title"""
        data = {'author': 'Author', 'description': 'Description'}
        
        request = CreateFeatureRequest.from_dict(data)
        
        with pytest.raises(ValueError, match="Title is required"):
            request.validate()
    
    def test_missing_author(self):
        """Test request with missing author"""
        data = {'title': 'Title', 'description': 'Description'}
        
        request = CreateFeatureRequest.from_dict(data)
        
        with pytest.raises(ValueError, match="Author is required"):
            request.validate()
    
    def test_empty_strings(self):
        """Test request with empty strings"""
        data = {'title': '   ', 'author': '   '}
        
        request = CreateFeatureRequest.from_dict(data)
        
        with pytest.raises(ValueError):
            request.validate()
    
    def test_optional_description(self):
        """Test request without description"""
        data = {'title': 'Title', 'author': 'Author'}
        
        request = CreateFeatureRequest.from_dict(data)
        request.validate()  # Should not raise
        
        assert request.description is None

class TestVoteRequest:
    """Test VoteRequest schema"""
    
    def test_valid_request(self):
        """Test valid vote request"""
        data = {'user_id': 'test_user_123'}
        
        request = VoteRequest.from_dict(data)
        request.validate()  # Should not raise
        
        assert request.user_id == 'test_user_123'
    
    def test_missing_user_id(self):
        """Test request with missing user ID"""
        data = {}
        
        request = VoteRequest.from_dict(data)
        
        with pytest.raises(ValueError, match="User ID is required"):
            request.validate()
    
    def test_empty_user_id(self):
        """Test request with empty user ID"""
        data = {'user_id': '   '}
        
        request = VoteRequest.from_dict(data)
        
        with pytest.raises(ValueError, match="User ID is required"):
            request.validate()