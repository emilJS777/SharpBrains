from .IProjectRepo import IProjectRepo
from src.ProjectStatus.IProjectStatusRepo import IProjectStatusRepo
from src.Sphere.ISphereRepo import ISphereRepo
from ..__Parents.Repository import Repository
from ..__Parents.Service import Service


class ProjectService(Service, Repository):
    def __init__(self,
                 project_repository: IProjectRepo,
                 sphere_repository: ISphereRepo,
                 project_status_repository: IProjectStatusRepo):
        self.project_repository: IProjectRepo = project_repository
        self.sphere_repository: ISphereRepo = sphere_repository
        self.project_status_repository: IProjectStatusRepo = project_status_repository

    def create(self, body: dict) -> dict:
        if not self.sphere_repository.get_by_id(sphere_id=body['sphere_id']):
            return self.response_not_found('sphere not found')

        if not self.project_status_repository.get_by_id(body['project_status_id']):
            return self.response_not_found('project status not found')

        if self.project_repository.get_by_title(body['title']):
            return self.response_conflict('project by this title exist')

        self.project_repository.create(body)
        return self.response_created('project successfully created')

    def update(self, project_id: int, body: dict) -> dict:
        project = self.project_repository.get_by_id(project_id)

        if not project:
            return self.response_not_found('project not found')

        if not self.sphere_repository.get_by_id(sphere_id=body['sphere_id']):
            return self.response_not_found('sphere not found')

        if not self.project_status_repository.get_by_id(body['project_status_id']):
            return self.response_not_found('project status not found')

        if self.project_repository.get_by_title_exclude_id(project_id=project_id, title=body['title']):
            return self.response_conflict('project by this title exist')

        self.project_repository.update(project=project, body=body)
        return self.response_updated('project successfully updated')

    def delete(self, project_id: int) -> dict:
        project = self.project_repository.get_by_id(project_id)
        if not project:
            return self.response_not_found('project not found')

        self.project_repository.delete_user_projects_by_project_id(project_id)
        self.project_repository.delete(project)
        return self.response_deleted('project successfully deleted')

    def get_by_id(self, project_id: int) -> dict:
        project = self.project_repository.get_by_id(project_id)

        if not project:
            return self.response_not_found('project not found')

        return self.response_ok(self.get_dict_items(project))

    def get_all(self, page: int, per_page: int, sphere_id: int or None, project_status_id: int or None) -> dict:
        projects = self.project_repository.get_all(
            page=page,
            per_page=per_page,
            sphere_id=sphere_id,
            project_status_id=project_status_id)

        for project in projects.items:
            project.project_status = project.project_status

        return self.response_ok(self.get_page_items(projects))
