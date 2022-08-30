from sqlalchemy.orm import relationship

from src import db
from src.__Parents.Model import Model


class User(Model, db.Model):
    first_name = db.Column(db.String(24), nullable=False)
    last_name = db.Column(db.String(24), nullable=False)
    email_address = db.Column(db.String(60), nullable=False)
    password_hash = db.Column(db.String(200))
    ticket = db.Column(db.String(120))

    image = relationship("UserImage", order_by="-UserImage.main", uselist=False)

    role_id = db.Column(db.Integer, db.ForeignKey("role.id"))
    role = relationship("Role", uselist=False)

    projects = relationship("Project", secondary="user_project", backref=db.backref('User'))
