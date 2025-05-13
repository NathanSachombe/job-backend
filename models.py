from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class UserModel(db.Model):
    __tablename__='users'

    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(50), nullable=False)
    lastName = db.Column(db.String(50), nullable=False)
    userName = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    phoneNumber = db.Column(db.Integer, unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    verified = db.Column(db.Boolean, default=False)

class JobModel(db.Model):
    __tablename__='jobs'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    created_at = db.Column(db.TIMESTAMP, server_default=db.func.now())
    duration = db.Column(db.Integer, nullable=False)
    expired = db.Column(db.Boolean, default=False)