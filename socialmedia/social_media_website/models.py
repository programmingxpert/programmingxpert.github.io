from flask_login import UserMixin
from database import get_user

class User(UserMixin):
    def __init__(self, id, username):
        self.id = id
        self.username = username

    @staticmethod
    def get(username):
        user_data = get_user(username)
        if user_data:
            return User(id=user_data['_id'], username=user_data['username'])
        return None

    def get_id(self):
        return str(self.id)
    
class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

