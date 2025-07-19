from typing import List
from repositories.base import BaseRepository
from models.feature import Feature
from database import db

class FeatureRepository(BaseRepository):
    def __init__(self):
        super().__init__(Feature)
    
    def get_all_ordered_by_votes(self) -> List[Feature]:
        """Get all features ordered by upvotes (descending) and creation date"""
        return Feature.query.order_by(Feature.upvotes.desc(), Feature.created_at.desc()).all()
    
    def increment_upvotes(self, feature: Feature) -> Feature:
        """Increment upvotes for a feature"""
        feature.upvotes += 1
        db.session.commit()
        return feature
    
    def decrement_upvotes(self, feature: Feature) -> Feature:
        """Decrement upvotes for a feature"""
        if feature.upvotes > 0:
            feature.upvotes -= 1
            db.session.commit()
        return feature