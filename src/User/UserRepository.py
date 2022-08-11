from flask_bcrypt import generate_password_hash
from .IUserRepo import IUserRepo
from .UserModel import User
from src.UserImage.UserImageModel import UserImage


class UserRepository(IUserRepo):
    def create(self, body: dict):
        user: User = User()
        user.name = body['name']
        user.password_hash = generate_password_hash(body['password'])
        user.email_address = body['email_address']
        user.first_name = body['first_name'].title()
        user.last_name = body['last_name'].title()
        user.save_db()

    def update(self, user: User, body: dict):
        user.name = body['name']
        user.password_hash = generate_password_hash(body['password'])
        user.email_address = body['email_address']
        user.first_name = body['first_name'].title()
        user.last_name = body['last_name'].title()
        user.update_db()

    def delete(self, user: User):
        user.delete_db()

    def get_all(self, page: int, per_page: int):
        users = User.query.paginate(page=page, per_page=per_page)
        return users

    def get_by_id(self, user_id: int):
        user = User.query.filter_by(id=user_id).first()
        return user

    def get_by_name(self, name: str):
        user = User.query.filter_by(name=name).first()
        return user

    def get_by_email_address(self, email_address: str):
        user = User.query.filter_by(email_address=email_address).first()
        return user

    def get_by_name_exclude_id(self, user_id: int, name: str):
        user = User.query.filter(User.id != user_id, User.name == name).first()
        return user

    def get_by_email_address_exclude_id(self, user_id: int, email_address: str):
        user = User.query.filter(User.id != user_id, User.email_address == email_address).first()
        return user

