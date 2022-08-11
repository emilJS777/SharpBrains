from .IUserRepo import IUserRepo
from .. import app
from ..__Parents.Repository import Repository
from ..__Parents.Service import Service


class UserService(Service, Repository):
    def __init__(self, user_repository: IUserRepo):
        self.user_repository: IUserRepo = user_repository

    def create(self, body: dict) -> dict:
        if self.user_repository.get_by_name(body['name']):
            return self.response_conflict('user by this name exist')

        if self.user_repository.get_by_email_address(body['email_address']):
            return self.response_conflict('user by this email address exist')

        self.user_repository.create(body)
        return self.response_created('user successfully created')

    def update(self, user_id: int, body: dict) -> dict:
        user = self.user_repository.get_by_id(user_id)

        if not user:
            return self.response_not_found('user not found')

        if self.user_repository.get_by_name_exclude_id(user_id=user_id, name=body['name']):
            return self.response_conflict('user by this name exist')

        if self.user_repository.get_by_email_address_exclude_id(user_id=user_id, email_address=body['email_address']):
            return self.response_conflict('user by this email address exist')

        self.user_repository.update(user=user, body=body)
        return self.response_updated('user successfully updated')

    def delete(self, user_id: int) -> dict:
        user = self.user_repository.get_by_id(user_id)

        if not user:
            return self.response_not_found('user not found')

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

        return self.response_ok(self.get_dict_items(user))

    def get_all(self, page: int, per_page: int) -> dict:
        users = self.user_repository.get_all(page=page, per_page=per_page)

        for user in users.items:
            if user.image and user.image.main:
                user.image.b64 = self.get_encode_image(image_path=user.image.filename,
                                                       dir_path=app.config["USER_IMAGE_PATH"])
            else:
                user.image = None

        return self.response_ok(self.get_page_items(users))
