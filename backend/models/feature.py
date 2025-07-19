from database import db
from models.base import BaseModel

class Feature(BaseModel):
    __tablename__ = 'features'
    
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    author = db.Column(db.String(100), nullable=False)
    upvotes = db.Column(db.Integer, default=0, nullable=False)
    
    # Relationship with votes
    votes = db.relationship('Vote', backref='feature', lazy='dynamic', cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<Feature {self.title}>'
    
    def to_dict(self):
        data = super().to_dict()
        data['votes_count'] = self.votes.count()
        return data