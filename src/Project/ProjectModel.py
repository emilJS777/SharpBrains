from src import db
from src.__Parents.Model import Model
from sqlalchemy.orm import relationship


class UserProject(Model, db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    project_id = db.Column(db.Integer, db.ForeignKey("project.id"))


class Project(Model, db.Model):
    title = db.Column(db.String(60), unique=True)
    description = db.Column(db.String(120))
    image_id = db.Column(db.Integer)

    sphere_id = db.Column(db.Integer, db.ForeignKey('sphere.id'))
    sphere = relationship("Sphere")

    project_status_id = db.Column(db.Integer, db.ForeignKey('project_status.id'))
    project_status = relationship("ProjectStatus")

    progress = db.Column(db.Integer, default=0)

    owner_name = db.Column(db.String(120))
    email_address = db.Column(db.String(120))
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    assigned_from = db.Column(db.String(120))

    users = relationship("User", secondary="user_project", backref=db.backref('Project'))
