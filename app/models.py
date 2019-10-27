from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
class User(UserMixin,db.Model):
    __tablename__= 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(60),index = True,unique=True)
    email = db.Column(db.String(100),index = True,unique=True)
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitches.id'))
    pass_secure = db.Column(db.String(255))
    pitch= db.relationship('Pitch', backref='users',lazy="dynamic")
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)



    def __repr__(self):
        return f'User {self.username}'

class Pitch(db.Model):
    __tablename__='pitch'

    id = db.Column(db.Integer,primary_key=True)
    pitch = db.Column(db.String)
    category_id = db.Column(db.Integer)
    upvote = db.Column(db.Integer)
    downvote = db.Column(db.Integer)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))

    
    
    def __repr__(self):
        return f'User {self.name}' 
