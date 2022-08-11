from src.__Parents.Controller import Controller
from .ProjectStatusService import ProjectStatusService
from .ProjectStatusRepository import ProjectStatusRepository
from src.Auth.AuthMiddleware import AuthMiddleware
from .ProjectStatusValidator import project_status_schema
from flask_expects_json import expects_json


class ProjectStatusController(Controller):
    project_status_service: ProjectStatusService = ProjectStatusService(ProjectStatusRepository())

    @AuthMiddleware.check_authorize
    @expects_json(project_status_schema)
    def post(self) -> dict:
        res: dict = self.project_status_service.create(self.request.get_json())
        return res

    @AuthMiddleware.check_authorize
    @expects_json(project_status_schema)
    def update(self) -> dict:
        res: dict = self.project_status_service.update(project_status_id=self.id, body=self.request.get_json())
        return res

    @AuthMiddleware.check_authorize
    def delete(self) -> dict:
        res: dict = self.project_status_service.delete(project_status_id=self.id)
        return res

    def get(self) -> dict:
        if self.id:
            res: dict = self.project_status_service.get_by_id(self.id)
        else:
            res: dict = self.project_status_service.get_all()
        return res
