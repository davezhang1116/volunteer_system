from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    role = db.Column(db.String(10), index=True, default='user')
    is_active = db.Column(db.Boolean, default=True)
    linked_status = db.Column(db.String(256), nullable=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class Volunteer(User):
    __tablename__ = 'volunteer'
    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    major = db.Column(db.String(64))
    minor = db.Column(db.String(64))
    year_of_study = db.Column(db.String(64))
    career_goals = db.Column(db.String(256))
    skills = db.Column(db.String(256))
    interest_keywords = db.Column(db.String(256))
    availability = db.Column(db.String(256))

class Doctor(User):
    __tablename__ = 'doctor'
    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    specialty = db.Column(db.String(128))
    current_projects = db.Column(db.String(512))
    required_skills = db.Column(db.String(256))

class CareCoordinator(User):
    __tablename__ = 'care_coordinator'
    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    facility_programs = db.Column(db.String(256))
    shift_requirements = db.Column(db.String(256))

class Resident(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    life_history = db.Column(db.String(512))
    hobbies = db.Column(db.String(256))
    cognitive_profile = db.Column(db.String(256))
    is_active = db.Column(db.Boolean, default=True)
    linked_status = db.Column(db.String(256), nullable=True)
