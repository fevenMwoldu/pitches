from . import db

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))
    fullname = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)

    def __repr__(self):
        return f'User {self.username}'

class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer,primary_key = True)
    category_name = db.Column(db.String(255))

    def __repr__(self):
        return f'User {self.category_name}'

class Pitch(db.Model):
    __tablename__ = 'pitch'
    id = db.Column(db.Integer,primary_key = True)
    content = db.Column(db.String(255))
    category_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer)
    upvotes = db.Column(db.Integer)
    downvotes = db.Column(db.Integer)

    def __repr__(self):
        return f'User {self.content}'

class Comment(db.Model):
    __tablename__ = 'comment'
    id = db.Column(db.Integer,primary_key = True)
    content = db.Column(db.String(255))
    user_id = db.Column(db.Integer)
    pitch_id = db.Column(db.Integer)
    
    def __repr__(self):
        return f'User {self.content}'

