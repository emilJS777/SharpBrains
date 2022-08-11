from .IImageRepo import IImageRepo
from .ImageModel import Image


class ImageRepository(IImageRepo):

    def create(self, filename: str):
        image: Image = Image()
        image.filename = filename
        image.save_db()

    def delete(self, image: Image):
        image.delete_db()

    def get_by_id(self, image_id: int) -> Image:
        image: Image = Image.query.filter_by(id=image_id).first()
        return image

    def get_all(self) -> list[Image]:
        images: list[Image] = Image.query.all()
        return images
