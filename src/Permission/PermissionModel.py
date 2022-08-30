from sqlalchemy.orm import relationship
from src import db
from src.__Parents.Model import Model


class Permission(db.Model, Model):
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120))

    roles = relationship("Role", secondary="role_permission", backref=db.backref('permission'))
