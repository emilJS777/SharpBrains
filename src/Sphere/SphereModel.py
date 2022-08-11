from src import db
from src.__Parents.Model import Model


class Sphere(Model, db.Model):
    title = db.Column(db.String(60), unique=True)
    description = db.Column(db.String(120))
