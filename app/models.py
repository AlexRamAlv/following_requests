from os import name
from app import db
from flask import request
from flask_login import UserMixin
from app import login_manager
from werkzeug.security import generate_password_hash, check_password_hash
import hashlib


@login_manager.user_loader
def load_admin(id):
   return Administrator.query.get(int(id))


class Administrator(UserMixin, db.Model):

    def __init__(self, *arg, **kwargs) -> None:
        super().__init__(*arg, **kwargs)
        self.username = f"{self.name}_{self.last_name}"
        if self.username is not None and self.avatar_hash is None:
            self.avatar_hash = self.gravatar_hash()

    # table name and its fieldsdb
    __tablename__ = "administrators"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    username = db.Column(db.String(128), index=True)
    password_hash = db.Column(db.String(128))
    creation_date = db.Column(db.DateTime, default=db.func.now())
    avatar_hash = db.Column(db.String(128))
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

    def gravatar_hash(self):
        return hashlib.md5(self.username.encode("utf-8")).hexdigest()

    def gravatar(self, size = 250):
        if request.is_secure:
            url = "https://secure.gravatar.com/avatar"
        else:
            url = "http://www.gravatar.com/avatar"

        return "{url}/{hash}?d={d}&s={s}&r={r}".format(url = url, hash = self.avatar_hash, d="identicon", s=size, r="g")

    # String object representation
    def __repr__(self) -> str:
        return "<Administrator %r>" %self.username


class Requester(db.Model):
    # constructor
    def __init__(self, *arg, **kwargs) -> None:
        super().__init__(*arg, **kwargs)
        self.username = f"{self.name}_{self.last_name}" 
        if self.username is not None and self.avatar_hash is None:
            self.avatar_hash = self.gravatar_hash()

    # table name and its fields
    __tablename__ = "requesters"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    username = db.Column(db.String(128), index=True)
    avatar_hash = db.Column(db.String(256))
    work_as = db.Column(db.String(64))
    admin_id = db.Column(db.Integer, db.ForeignKey("administrators.id"))
    creation_date = db.Column(db.DateTime, default=db.func.now())
    requests = db.relationship("Request", backref="requester")

    def gravatar_hash(self):
        return hashlib.md5(self.username.encode("utf-8")).hexdigest()

    def gravatar(self, size = 250):
        if request.is_secure:
            url = "https://secure.gravatar.com/avatar"
        else:
            url = "http://www.gravatar.com/avatar"

        return "{url}/{hash}?d={d}&s={s}&r={r}".format(url = url, hash = self.avatar_hash, d="mp", s=size, r="g")

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
    requester_id = db.Column(db.Integer, db.ForeignKey("requesters.id"))

    # String object representation
    def __repr__(self) -> str:
        return "<Request %r>" %self.request_number
