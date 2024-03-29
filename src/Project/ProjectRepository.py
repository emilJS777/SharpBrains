from .IProjectRepo import IProjectRepo
from .ProjectModel import Project, UserProject
from flask import g


class ProjectRepository(IProjectRepo):

    def create(self, body: dict) -> Project:
        project: Project = Project()
        project.title = body['title']
        project.description = body['description']
        project.sphere_id = body['sphere_id']
        project.image_id = body['image_id']
        project.project_status_id = body['project_status_id']
        project.progress = body['progress']

        project.owner_name = body['owner_name']
        project.email_address = body['email_address']
        project.start_date = body['start_date'].split("T")[0]
        project.end_date = body['end_date'].split("T")[0]
        project.assigned_from = body['assigned_from']

        project.users = [g.user]
        project.save_db()
        return project

    def update(self, project: Project, body: dict):
        project.title = body['title']
        project.description = body['description']
        project.sphere_id = body['sphere_id']
        project.image_id = body['image_id']
        project.project_status_id = body['project_status_id']
        project.progress = body['progress']

        project.owner_name = body['owner_name']
        project.email_address = body['email_address']
        project.start_date = body['start_date'].split("T")[0]
        project.end_date = body['end_date'].split("T")[0]
        project.assigned_from = body['assigned_from']

        project.update_db()

    def delete(self, project: Project):
        project.delete_db()

    def get_by_id(self, project_id: int) -> Project:
        project: Project = Project.query.filter(Project.id.in_([project.id for project in g.user.projects]))\
            .filter_by(id=project_id).first()
        return project

    def get_by_title(self, title: str) -> Project:
        project: Project = Project.query.filter_by(title=title).first()
        return project

    def get_by_title_exclude_id(self, project_id: int, title: str) -> Project:
        project: Project = Project.query.filter(Project.id != project_id, Project.title == title).first()
        return project

    def get_all(self, page: int, per_page: int, sphere_id: int or None, project_status_id: int or None):
        projects = Project.query.filter(
            Project.id.in_([project.id for project in g.user.projects]),
            Project.sphere_id == sphere_id if sphere_id else Project.sphere_id.isnot(None),
            Project.project_status_id == project_status_id if project_status_id else Project.project_status_id.isnot(None)
        ).paginate(page=page, per_page=per_page)
        return projects

    def delete_user_projects_by_user_id(self, user_id: int):
        UserProject.query.filter_by(user_id=user_id).delete()

    def delete_user_projects_by_project_id(self, project_id: int):
        UserProject.query.filter_by(project_id=project_id).delete()
