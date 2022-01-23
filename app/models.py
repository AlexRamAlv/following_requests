from app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class Administrator(UserMixin, db.Model):
    # table name and its fields
    __tablename__ = "administrators"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    username = db.Column(db.String(128), index=True)
    password_hash = db.Column(db.String(128))
    creation_date = db.Column(db.DateTime)
    last_seen = db.Column(db.DateTime)
    requesters = db.relationship("Requester", backref ="administrator")
    # Declaring password as a property
    @property
    def password(self):
        raise AttributeError("This attribute is not accesible!")
    # Using setter decorator to asign password hash value to store it in the database
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)
    # validaiting password given by the administrator
    def validate_password(self, password):
        return check_password_hash(self.password_hash, password)

    # String object representation
    def __repr__(self) -> str:
        return "<Administrator %r>" %self.username


class Requester(db.Model):
    # table name and its fields
    __tablename__ = "requesters"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    username = db.Column(db.String(128), index=True)
    work_as = db.Column(db.String(64))
    create_by = db.Column(db.Integer, db.ForeignKey("administrators.id"))
    creation_date = db.Column(db.DateTime)
    requests = db.relationship("Request", backref="requester")

    # String object representation
    def __repr__(self) -> str:
        return "<Requester %r>" %self.username


class Request(db.Model):
    # table name and its fields
    __tablename__ = "requests"
    id = db.Column(db.Integer, primary_key=True)
    request_number = db.Column(db.String(20), unique=True)
    creation_date_at_AX365 = db.Column(db.DateTime)
    description = db.Column(db.Text)
    purchase_order = db.Column(db.String(20), unique=True)
    recived_date = db.Column(db.DateTime)
    comments = db.Column(db.Text)
    comments_update = db.Column(db.DateTime)
    created_by_in_AX365 = db.Column(db.Integer, db.ForeignKey("requesters.id"))

    # String object representation
    def __repr__(self) -> str:
        return "<Request %r>" %self.request_number
