from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from flask_login import UserMixin
from . import login_manager

# from API
class Quote:
  def __init__(self,id,author,quote):
    self.id = id
    self.author = author
    self.quote = quote


class User(UserMixin,db.Model):
    __tablename__='users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)
    pass_secure = db.Column(db.String(255))
    user_type = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    blogs = db.relationship('Blogs',backref='user', lazy='dynamic')
    comments = db.relationship('Comment', backref='user', lazy='dynamic')
    
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
        
   
    def set_password(self, password):
        self.pass_secure = generate_password_hash(password)
    def verify_password(self,password):
        return check_password_hash(self.pass_secure, password)
    
    def save_user(self):
        db.session.add(self)
        db.session.commit()
    
    
class Blogs(db.Model):
    __tablename__='blogs'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    title = db.Column(db.String(255))
    blog_description = db.Column(db.String(255))
    blog_category = db.Column(db.String(255))
    time_created = db.Column(db.DateTime,default=datetime.utcnow)
    comments = db.relationship('Comment', backref='blog', lazy='dynamic')
    
    
    def save_posts(self):
        db.session.add(self)
        db.session.commit()

    def delete_posts(self):
        db.session.delete(self)
        db.session.commit()

@classmethod
def get_posts(cls,id):
    posts=Post.query.filter_by(id=id).first()
    return posts
  
@classmethod
def all_posts(cls):
    posts=Post.query.all()
    return posts

@classmethod
def get_user_posts(cls,id):
    posts=Post.query.filter_by(user_id=id).all()
    return   

    
    

class Comment(db.Model):
    __tablename__='comments'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('blogs.id'))
    comment = db.Column(db.String(255))
    
    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    def delete_posts(self):
        db.session.delete(self)
        db.session.commit()


class Subscribe(db.Model):
  __tablename__='subscribers'
  id=db.Column(db.Integer,primary_key=True)
  email=db.Column(db.String(255),unique=True)

  def save_subscriber(self):
    db.session.add(self)
    db.session.commit()

  def __repr__(self):
    return f"Subcribe {self.email}"
