from src import db
from src.__Parents.Model import Model
from sqlalchemy.orm import relationship
import time


class Message(db.Model, Model):
    sender_id = db.Column(db.Integer, nullable=False)
    addressee_id = db.Column(db.Integer, nullable=False)
    text = db.Column(db.Text, nullable=False)
    reading = db.Column(db.Boolean, default=False)

    chat_id = db.Column(db.Integer, db.ForeignKey("chat.id"))
    chat = relationship("Chat", overlaps="message")

    file_id = db.Column(db.Integer, db.ForeignKey("file.id"))
    file = relationship("File")
    creation_date = db.Column(db.DateTime, default=time.localtime())
