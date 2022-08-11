from .IProjectStatusRepo import IProjectStatusRepo
from ..__Parents.Repository import Repository
from ..__Parents.Service import Service


class ProjectStatusService(Service, Repository):
    def __init__(self, project_status_repository: IProjectStatusRepo):
        self.project_status_repository: IProjectStatusRepo = project_status_repository

    def create(self, body: dict) -> dict:
        if self.project_status_repository.get_by_title(body['title']):
            return self.response_conflict('project status by this title exist')

        self.project_status_repository.create(body)
        return self.response_created('project status successfully created')

    def update(self, project_status_id: int, body: dict) -> dict:
        project_status = self.project_status_repository.get_by_id(project_status_id)
        if not project_status:
            return self.response_not_found('project status not found')

        if self.project_status_repository.get_by_title_exclude_id(project_status_id=project_status_id, title=body['title']):
            return self.response_conflict('project status by this title exist')

        self.project_status_repository.update(project_status=project_status, body=body)
        return self.response_updated('project status successfully created')

    def delete(self, project_status_id: int) -> dict:
        project_status = self.project_status_repository.get_by_id(project_status_id)
        if not project_status:
            return self.response_not_found('project status not found')

        self.project_status_repository.delete(project_status)
        return self.response_deleted('project status successfully deleted')

    def get_by_id(self, project_status_id: int) -> dict:
        project_status = self.project_status_repository.get_by_id(project_status_id)
        if not project_status:
            return self.response_not_found('project status not found')

        return self.response_ok(self.get_dict_items(project_status))

    def get_all(self) -> dict:
        project_statuses = self.project_status_repository.get_all()
        return self.response_ok(self.get_array_items(project_statuses))
