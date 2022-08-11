from sqlalchemy.orm import relationship
from src import db
from src.__Parents.Model import Model


class Meeting(db.Model, Model):
    title = db.Column(db.String(60), nullable=False)
    description = db.Column(db.String(120))

    date = db.Column(db.Date, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    user = relationship("User", uselist=False)
