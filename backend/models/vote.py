from database import db
from models.base import BaseModel

class Vote(BaseModel):
    __tablename__ = 'votes'
    
    feature_id = db.Column(db.Integer, db.ForeignKey('features.id'), nullable=False)
    user_id = db.Column(db.String(100), nullable=False)
    
    # Unique constraint to prevent duplicate votes
    __table_args__ = (db.UniqueConstraint('feature_id', 'user_id', name='unique_user_feature_vote'),)
    
    def __repr__(self):
        return f'<Vote user:{self.user_id} feature:{self.feature_id}>'