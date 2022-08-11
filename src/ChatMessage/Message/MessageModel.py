from src import db
from src.__Parents.Model import Model
from sqlalchemy.orm import relationship
import time


class Message(db.Model, Model):
    sender_id = db.Column(db.Integer, nullable=False)
    addressee_id = db.Column(db.Integer, nullable=False)
    text = db.Column(db.Text, nullable=False)

    chat_id = db.Column(db.Integer, db.ForeignKey("chat.id"))
    chat = relationship("Chat", overlaps="message")

    creation_date = db.Column(db.DateTime, default=time.localtime())
