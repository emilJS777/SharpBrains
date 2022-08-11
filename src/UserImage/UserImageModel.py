from sqlalchemy.orm import relationship
from src import db
from src.__Parents.Model import Model


class UserImage(Model, db.Model):
    filename = db.Column(db.String(120), nullable=False)
    main = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = relationship("User", overlaps="image")
