from .IProjectStatusRepo import IProjectStatusRepo
from .ProjectStatusModel import ProjectStatus


class ProjectStatusRepository(IProjectStatusRepo):

    def create(self, body: dict):
        project_status: ProjectStatus = ProjectStatus()
        project_status.title = body['title']
        project_status.description = body['description']
        project_status.color = body['color']
        project_status.save_db()

    def update(self, project_status: ProjectStatus, body: dict):
        project_status.title = body['title']
        project_status.description = body['description']
        project_status.color = body['color']
        project_status.update_db()

    def delete(self, project_status: ProjectStatus):
        project_status.delete_db()

    def get_by_title(self, title: str):
        project_status: ProjectStatus = ProjectStatus.query.filter_by(title=title).first()
        return project_status

    def get_by_title_exclude_id(self, project_status_id: int, title: str):
        project_status: ProjectStatus = ProjectStatus.query.filter(ProjectStatus.id != project_status_id,
                                                                   ProjectStatus.title == title).first()
        return project_status

    def get_by_id(self, project_status_id: int):
        project_status: ProjectStatus = ProjectStatus.query.filter_by(id=project_status_id).first()
        return project_status

    def get_all(self):
        project_statuses: ProjectStatus = ProjectStatus.query.all()
        return project_statuses
