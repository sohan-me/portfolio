from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

db = SQLAlchemy()


class User(db.Model, UserMixin):
    __tablename__ = 'user'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    is_active = db.Column(db.Boolean, default=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Profile(db.Model):  
    __tablename__ = 'profile'
    
    id = db.Column(db.Integer, primary_key=True)
    image_url = db.Column(db.String(200))
    email = db.Column(db.String(50))
    project_count = db.Column(db.String, nullable=True)
    experience = db.Column(db.String, nullable=True)
    github = db.Column(db.String(255), nullable=True)
    linkedin  = db.Column(db.String(255), nullable=True)
    twitter = db.Column(db.String(255), nullable=True)
    instagram = db.Column(db.String(255), nullable=True)
    
    
class Pricing(db.Model): 
    __tablename__ = 'pricing'
    
    id = db.Column(db.Integer, primary_key=True)
    plan_name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    features = db.Column(db.Text, nullable=False)
    description = db.Column(db.String(255))
    availability = db.Column(db.Boolean, default=True)

class FeaturedProject(db.Model):
    __tablename__ = 'featuredproject'
    
    id = db.Column(db.Integer, primary_key=True)
    project_name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(200), nullable=False)
    project_link = db.Column(db.String(200))
    tags = db.Column(db.String(200), nullable=True)

class EducationalExperience(db.Model):
    __tablename__ = 'educationalexperience'
    
    id = db.Column(db.Integer, primary_key=True)
    degree = db.Column(db.String(100), nullable=False)
    institution = db.Column(db.String(100), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date)
    description = db.Column(db.Text, nullable=True)

class Specialization(db.Model):
    __tablename__ = 'specialization'
    
    id = db.Column(db.Integer, primary_key=True)
    skill_name = db.Column(db.String(100), nullable=False)
    proficiency = db.Column(db.Integer) 
    description = db.Column(db.Text)

class Advantage(db.Model):
    __tablename__ = 'Advantage'
    
    id = db.Column(db.Integer, primary_key=True)
    skill_name = db.Column(db.String(100), nullable=False)
    proficiency = db.Column(db.Integer)
    image_url = db.Column(db.String(200), nullable=True)