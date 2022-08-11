from src import db
from src.__Parents.Model import Model


class ProjectStatus(db.Model, Model):
    title = db.Column(db.String(60), nullable=False)
    description = db.Column(db.String(120))
    color = db.Column(db.String(10))
