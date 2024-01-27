from pymongo import MongoClient
from datetime import datetime

# Connect to MongoDB
client = MongoClient("mongodb+srv://Puski:satya%40123@cluster0.quz6u.mongodb.net")
db = client.social_media_db

# Collections
users = db.users
posts = db.posts
comments = db.comments
likes = db.likes

# Functions for Database Operations

def get_user(username):
    return users.find_one({"username": username})

def create_user(username, password_hash, email, full_name):
    users.insert_one({
        "username": username,
        "password_hash": password_hash,
        "email": email,
        "full_name": full_name,
        "created_at": datetime.utcnow()
    })

def create_post(title, content, author):
    post_data = {
        'title': title,
        'content': content,
        'author': author
    }
    posts.insert_one(post_data)

def get_posts():
    return list(posts.find())
