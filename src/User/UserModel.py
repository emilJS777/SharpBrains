from sqlalchemy.orm import relationship

from src import db
from src.__Parents.Model import Model


class User(Model, db.Model):
    name = db.Column(db.String(60), unique=True)
    first_name = db.Column(db.String(24), nullable=False)
    last_name = db.Column(db.String(24), nullable=False)
    email_address = db.Column(db.String(60), nullable=False)
    password_hash = db.Column(db.String(200))

    image = relationship("UserImage", order_by="-UserImage.main", uselist=False)
