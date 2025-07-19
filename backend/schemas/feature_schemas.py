from typing import Optional

class CreateFeatureRequest:
    def __init__(self, title: str, author: str, description: Optional[str] = None):
        self.title = title
        self.author = author
        self.description = description
    
    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            title=data.get('title', '').strip(),
            author=data.get('author', '').strip(),
            description=data.get('description', '').strip() if data.get('description') else None
        )
    
    def validate(self):
        if not self.title:
            raise ValueError("Title is required")
        if not self.author:
            raise ValueError("Author is required")

class VoteRequest:
    def __init__(self, user_id: str):
        self.user_id = user_id
    
    @classmethod
    def from_dict(cls, data: dict):
        return cls(user_id=data.get('user_id', '').strip())
    
    def validate(self):
        if not self.user_id:
            raise ValueError("User ID is required")