from src import db
from src.__Parents.Model import Model


class AboutUs(db.Model, Model):
    title = db.Column(db.String(80), nullable=False)
    sub_title = db.Column(db.String(120))
    description = db.Column(db.Text)
