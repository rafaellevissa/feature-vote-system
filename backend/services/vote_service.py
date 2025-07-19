from typing import List, Dict, Any
from repositories.feature_repository import FeatureRepository
from repositories.vote_repository import VoteRepository
from sqlalchemy.exc import IntegrityError

class VoteService:
    def __init__(self):
        self.feature_repo = FeatureRepository()
        self.vote_repo = VoteRepository()
    
    def upvote_feature(self, feature_id: int, user_id: str) -> Dict[str, Any]:
        """Upvote a feature"""
        if not user_id:
            raise ValueError("User ID is required")
        
        # Check if feature exists
        feature = self.feature_repo.get_by_id(feature_id)
        if not feature:
            raise ValueError("Feature not found")
        
        # Check if user already voted
        existing_vote = self.vote_repo.get_user_feature_vote(user_id, feature_id)
        if existing_vote:
            raise ValueError("User already voted for this feature")
        
        try:
            # Create vote
            self.vote_repo.create(feature_id=feature_id, user_id=user_id)
            # Increment feature upvotes
            feature = self.feature_repo.increment_upvotes(feature)
            return feature.to_dict()
        
        except IntegrityError:
            raise ValueError("User already voted for this feature")
    
    def remove_vote(self, feature_id: int, user_id: str) -> Dict[str, Any]:
        """Remove a user's vote from a feature"""
        if not user_id:
            raise ValueError("User ID is required")
        
        # Check if feature exists
        feature = self.feature_repo.get_by_id(feature_id)
        if not feature:
            raise ValueError("Feature not found")
        
        # Check if vote exists
        vote = self.vote_repo.get_user_feature_vote(user_id, feature_id)
        if not vote:
            raise ValueError("Vote not found")
        
        # Remove vote
        self.vote_repo.delete(vote)
        # Decrement feature upvotes
        feature = self.feature_repo.decrement_upvotes(feature)
        return feature.to_dict()
    
    def get_user_votes(self, user_id: str) -> List[int]:
        """Get list of feature IDs that user has voted for"""
        return self.vote_repo.get_user_voted_feature_ids(user_id)