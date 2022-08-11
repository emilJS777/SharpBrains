from src import db
from src.__Parents.Model import Model


class Image(Model, db.Model):
    filename = db.Column(db.String(120), nullable=False, unique=True)
