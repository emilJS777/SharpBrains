from .IImageRepo import IImageRepo
from ..__Parents.Repository import Repository
from ..__Parents.Service import Service
from ..__Parents.Image import Image
from src import app


class ImageService(Service, Image, Repository):

    def __init__(self, image_repository: IImageRepo):
        self.image_repository: IImageRepo = image_repository

    def create(self, image) -> dict:
        if not image:
            return self.response_not_found('image not found')

        filename: str = self.save_image(image_path=app.config["IMAGE_PATH"], image=image)
        self.image_repository.create(filename=filename)
        return self.response_created('image successfully uploaded')

    def delete(self, image_id: int) -> dict:
        image = self.image_repository.get_by_id(image_id)
        if not image:
            return self.response_not_found('image not found')

        self.image_repository.delete(image)
        return self.response_deleted('image successfully deleted')

    def get_by_id(self, image_id: int) -> dict:
        image = self.image_repository.get_by_id(image_id)
        if not image:
            return self.response_not_found('image not found')

        image.b64 = self.get_encode_image(image.filename, dir_path=app.config['IMAGE_PATH'])
        return self.response_ok(self.get_dict_items(image))

    def get_all(self) -> dict:
        images = self.image_repository.get_all()
        for image in images:
            image.b64 = self.get_encode_image(image_path=image.filename, dir_path=app.config['IMAGE_PATH'])
        return self.response_ok(self.get_array_items(images))
