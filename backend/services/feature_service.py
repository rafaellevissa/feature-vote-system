from typing import List, Optional, Dict, Any
from repositories.feature_repository import FeatureRepository
from repositories.vote_repository import VoteRepository

class FeatureService:
    def __init__(self):
        self.feature_repo = FeatureRepository()
        self.vote_repo = VoteRepository()
    
    def get_all_features(self) -> List[Dict[str, Any]]:
        """Get all features ordered by votes"""
        features = self.feature_repo.get_all_ordered_by_votes()
        return [feature.to_dict() for feature in features]
    
    def create_feature(self, title: str, author: str, description: str = None) -> Dict[str, Any]:
        """Create a new feature"""
        if not title or not author:
            raise ValueError("Title and author are required")
        
        feature = self.feature_repo.create(
            title=title.strip(),
            author=author.strip(),
            description=description.strip() if description else None
        )
        return feature.to_dict()
    
    def get_feature_by_id(self, feature_id: int) -> Optional[Dict[str, Any]]:
        """Get a feature by ID"""
        feature = self.feature_repo.get_by_id(feature_id)
        return feature.to_dict() if feature else None
    
    def delete_feature(self, feature_id: int) -> bool:
        """Delete a feature"""
        feature = self.feature_repo.get_by_id(feature_id)
        if not feature:
            return False
        
        self.feature_repo.delete(feature)
        return True