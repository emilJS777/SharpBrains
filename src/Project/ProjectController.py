from .ProjectRepository import ProjectRepository
from .ProjectService import ProjectService
from src.Sphere.SphereRepository import SphereRepository
from ..__Parents.Controller import Controller
from flask_expects_json import expects_json
from .ProjectValidator import project_schema
from src.Auth.AuthMiddleware import AuthMiddleware
from src.ProjectStatus.ProjectStatusRepository import ProjectStatusRepository


class ProjectController(Controller):
    project_service: ProjectService = ProjectService(ProjectRepository(), SphereRepository(), ProjectStatusRepository())

    @expects_json(project_schema)
    @AuthMiddleware.check_authorize
    def post(self) -> dict:
        res: dict = self.project_service.create(self.request.get_json())
        return res

    @expects_json(project_schema)
    @AuthMiddleware.check_authorize
    def put(self) -> dict:
        res: dict = self.project_service.update(project_id=self.id, body=self.request.get_json())
        return res

    @AuthMiddleware.check_authorize
    def delete(self) -> dict:
        res: dict = self.project_service.delete(self.id)
        return res

    def get(self) -> dict:
        if self.id:
            res: dict = self.project_service.get_by_id(self.id)
        else:
            res: dict = self.project_service.get_all(
                page=self.page,
                per_page=self.per_page,
                sphere_id=self.arguments.get('sphere_id'),
                project_status_id=self.arguments.get('project_status_id'))
        return res
