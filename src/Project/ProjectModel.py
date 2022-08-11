from src import db
from src.__Parents.Model import Model
from sqlalchemy.orm import relationship


class Project(Model, db.Model):
    title = db.Column(db.String(60), unique=True)
    description = db.Column(db.String(120))
    image_id = db.Column(db.Integer)

    sphere_id = db.Column(db.Integer, db.ForeignKey('sphere.id'))
    sphere = relationship("Sphere")

    project_status_id = db.Column(db.Integer, db.ForeignKey('project_status.id'))
    project_status = relationship("ProjectStatus")
