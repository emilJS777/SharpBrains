from .IAuthRepo import IAuthRepo
from src.User.IUserRepo import IUserRepo
from flask_bcrypt import check_password_hash
from ..__Parents.Repository import Repository
from ..__Parents.Service import Service
from flask_jwt_extended import get_jwt_identity
from flask import request, g


class AuthService(Service, Repository):
    def __init__(self, auth_repository: IAuthRepo, user_repository: IUserRepo):
        self.__auth_repository = auth_repository
        self.__user_repository = user_repository

    def login(self, body: dict) -> dict:
        user = self.__user_repository.get_by_email_address(body['email_address'])

        if not user or not check_password_hash(user.password_hash, body['password']):
            return self.response_invalid_login()

        auth = self.__auth_repository.generate_tokens(user.id)
        return self.response_ok(auth)

    def refresh(self) -> dict:
        auth = self.__auth_repository.get_by_user_id(user_id=get_jwt_identity())
        if auth['refresh_token'] == request.headers['authorization'].split(' ')[1]:

            auth = self.__auth_repository.generate_tokens(get_jwt_identity())
            self.response_ok(auth)

        return self.response_invalid_login()

    def get_profile(self) -> dict:
        return self.response_ok({
            "email_address": g.user.email_address,
            "first_name": g.user.first_name,
            "last_name": g.user.last_name,
            "image" : self.get_encode_image(image_path=g.user.image.filename, dir_path=app.config["USER_IMAGE_PATH"]) if g.user.image else None,
            "role": self.get_dict_items(g.user.role) if g.user.role else None,
            "permissions": self.get_array_items(g.user.role.permissions) if g.user.role else [],
            "projects": self.get_array_items(g.user.projects)
        })
