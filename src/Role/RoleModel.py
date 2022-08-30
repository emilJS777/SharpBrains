from src import db
from src.__Parents.Model import Model
from sqlalchemy.orm import relationship


class RolePermission(db.Model, Model):
    role_id = db.Column(db.Integer, db.ForeignKey("role.id"))
    permission_id = db.Column(db.Integer, db.ForeignKey("permission.id"))


class Role(db.Model, Model):
    name = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(120))
    creator_id = db.Column(db.Integer)

    permissions = relationship("Permission", secondary="role_permission", backref=db.backref('role'))
