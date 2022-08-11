from sqlalchemy.orm import relationship
from src import db
from src.__Parents.Model import Model
import time


class Chat(db.Model, Model):
    user1_id = db.Column(db.Integer, nullable=False)
    user2_id = db.Column(db.Integer, nullable=False)

    last_update = db.Column(db.DateTime, default=time.localtime())
    message = relationship("Message", order_by="-Message.creation_date", uselist=False)
