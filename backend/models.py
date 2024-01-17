from flask_sqlalchemy import SQLAlchemy

#initiallize db
db = SQLAlchemy()

class User(db.Model):
    __tablename__='users'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.Text(50), nullable=False)
    last_name = db.Column(db.Text(50), nullable=False)
    phone = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    role = db.Column(db.Text(50), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.TIMESTAMP)

