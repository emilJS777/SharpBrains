from .IUserImageRepo import IUserImageRepo
from .UserImageModel import UserImage
from flask import g


class UserImageRepository(IUserImageRepo):

    def create(self, filename: str, main: bool):
        user_image: UserImage = UserImage()
        user_image.user_id = g.user.id
        user_image.main = main
        user_image.filename = filename
        user_image.save_db()

    def update(self, user_image: UserImage, main: bool):
        user_image.main = main
        user_image.update_db()

    def delete(self, user_image: UserImage):
        user_image.delete_db()

    def get_by_main(self) -> UserImage:
        user_image: UserImage = UserImage.query.filter_by(main=True, user_id=g.user.id).first()
        return user_image

    def get_by_id(self, user_image_id: int) -> UserImage:
        user_image: UserImage = UserImage.query.filter_by(id=user_image_id).first()
        return user_image

    def get_all(self) -> list[UserImage]:
        user_images: list[UserImage] = UserImage.query.filter_by(user_id=g.user.id).all()
        return user_images
