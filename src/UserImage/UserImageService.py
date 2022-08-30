from src.__Parents.Service import Service
from .IUserImageRepo import IUserImageRepo
from src import app
from ..__Parents.Repository import Repository
from ..__Parents.Image import Image


class UserImageService(Service, Image, Repository):
    def __init__(self, user_image_repository: IUserImageRepo):
        self.user_image_repository: IUserImageRepo = user_image_repository

    # RESET MAIN USER IMAGE
    def reset_main_image(self):
        main_user_image = self.user_image_repository.get_by_main()
        if main_user_image:
            self.user_image_repository.update(user_image=main_user_image, main=False)

    def create(self, image, main: bool) -> dict:
        if not image:
            return self.response_not_found('image not found')

        if main:
            self.reset_main_image()

        filename: str = self.save_image(image_path=app.config["USER_IMAGE_PATH"], image=image)
        self.user_image_repository.create(filename=filename, main=main)
        return self.response_created('image successfully created')

    def update(self, image_id: int, main: bool) -> dict:
        user_image = self.user_image_repository.get_by_id(image_id)
        if not user_image:
            return self.response_not_found('image not found')

        if main:
            self.reset_main_image()

        self.user_image_repository.update(user_image=user_image, main=main)
        return self.response_updated('image successfully updated')

    def delete(self, image_id: int) -> dict:
        user_image = self.user_image_repository.get_by_id(image_id)
        if not user_image:
            return self.response_not_found('image not found')

        self.delete_image(image_path=user_image.filename, dir_path=app.config["USER_IMAGE_PATH"])
        self.user_image_repository.delete(user_image)
        return self.response_deleted('image successfully deleted')

    def get_all(self) -> dict:
        user_images = self.user_image_repository.get_all()

        for image in user_images:
            image.b64 = self.get_encode_image(image_path=image.filename, dir_path=app.config["USER_IMAGE_PATH"])

        return self.response_ok(self.get_array_items(user_images))
