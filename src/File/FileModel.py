from src import db
from src.__Parents.Model import Model


class File(db.Model, Model):
    filename = db.Column(db.String(120), nullable=False)
    creator_id = db.Column(db.Integer, nullable=False)
