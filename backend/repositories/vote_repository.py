from typing import List, Optional
from repositories.base import BaseRepository
from models.vote import Vote

class VoteRepository(BaseRepository):
    def __init__(self):
        super().__init__(Vote)
    
    def get_user_votes(self, user_id: str) -> List[Vote]:
        """Get all votes by a user"""
        return Vote.query.filter_by(user_id=user_id).all()
    
    def get_user_feature_vote(self, user_id: str, feature_id: int) -> Optional[Vote]:
        """Get a specific vote by user and feature"""
        return Vote.query.filter_by(user_id=user_id, feature_id=feature_id).first()
    
    def get_user_voted_feature_ids(self, user_id: str) -> List[int]:
        """Get list of feature IDs that user has voted for"""
        votes = self.get_user_votes(user_id)
        return [vote.feature_id for vote in votes]