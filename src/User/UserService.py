from .IUserRepo import IUserRepo
from .. import app
from ..__Parents.Repository import Repository
from ..__Parents.Service import Service
from ..__Parents.Image import Image
from flask import g
from ..Project.IProjectRepo import IProjectRepo


class UserService(Service, Repository, Image):
    def __init__(self, user_repository: IUserRepo, project_repository: IProjectRepo):
        self.user_repository: IUserRepo = user_repository
        self.project_repository: IProjectRepo = project_repository

    @staticmethod
    def get_allowed_projects(project_ids):
        allowed_projects = []
        for project_id in project_ids:
            for project in g.user.projects:
                if project.id == project_id:
                    allowed_projects.append(project)
        return allowed_projects

    def create(self, body: dict) -> dict:
        if self.user_repository.get_by_email_address(body['email_address']):
            return self.response_conflict('user by this email address exist')

        user = self.user_repository.create(
            body=body,
            projects=self.get_allowed_projects(body['project_ids']),
            ticket=self.generate_ticket_code())

        return self.response_ok({"id": user.id, "ticket": user.ticket})

    def update(self, user_id: int, body: dict) -> dict:
        user = self.user_repository.get_by_id(user_id)

        if not user:
            return self.response_not_found('user not found')

        if self.user_repository.get_by_email_address_exclude_id(user_id=user_id, email_address=body['email_address']):
            return self.response_conflict('user by this email address exist')

        self.user_repository.update(user=user, body=body, projects=self.get_allowed_projects(body['project_ids']))
        return self.response_updated('user successfully updated')

    def registration(self, body: dict) -> dict:
        user = self.user_repository.get_by_ticket(ticket=body['ticket'])
        if not user:
            return self.response_not_found('user by this ticket not found')

        self.user_repository.registration(user=user, body=body)
        return self.response_created("user successfully created")

    def delete(self, user_id: int) -> dict:
        user = self.user_repository.get_by_id(user_id)

        if not user:
            return self.response_not_found('user not found')

        self.project_repository.delete_user_projects_by_user_id(user_id)
        self.user_repository.delete(user)
        return self.response_deleted('user successfully deleted')

    def get_by_id(self, user_id: int) -> dict:
        user = self.user_repository.get_by_id(user_id)

        if not user:
            return self.response_not_found('user not found')

        if user.image and user.image.main:
            user.image.b64 = self.get_encode_image(image_path=user.image.filename,
                                                   dir_path=app.config["USER_IMAGE_PATH"])
        else:
            user.image = None

        user.role = user.role
        return self.response_ok(self.get_dict_items(user))

    def get_all(self, page: int, per_page: int) -> dict:
        users = self.user_repository.get_all(page=page, per_page=per_page)

        for user in users.items:
            if user.image and user.image:
                user.image.b64 = self.get_encode_image(image_path=user.image.filename,
                                                       dir_path=app.config["USER_IMAGE_PATH"])
            else:
                user.image = None

        for user in users.items:
            user.role = user.role

        return self.response_ok(self.get_page_items(users))
