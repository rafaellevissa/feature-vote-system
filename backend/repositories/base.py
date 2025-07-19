from database import db
from typing import List, Optional, Type, TypeVar

T = TypeVar('T')

class BaseRepository:
    def __init__(self, model: Type[T]):
        self.model = model
    
    def create(self, **kwargs) -> T:
        """Create a new instance"""
        instance = self.model(**kwargs)
        db.session.add(instance)
        db.session.commit()
        return instance
    
    def get_by_id(self, id: int) -> Optional[T]:
        """Get instance by ID"""
        return self.model.query.get(id)
    
    def get_all(self) -> List[T]:
        """Get all instances"""
        return self.model.query.all()
    
    def update(self, instance: T, **kwargs) -> T:
        """Update an instance"""
        for key, value in kwargs.items():
            setattr(instance, key, value)
        db.session.commit()
        return instance
    
    def delete(self, instance: T) -> bool:
        """Delete an instance"""
        db.session.delete(instance)
        db.session.commit()
        return True
    
    def save(self, instance: T) -> T:
        """Save an instance"""
        db.session.add(instance)
        db.session.commit()
        return instance