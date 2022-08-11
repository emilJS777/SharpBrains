from abc import ABC, abstractmethod
from .ImageModel import Image


class IImageRepo(ABC):

    @abstractmethod
    def create(self, filename: str):
        pass

    # @abstractmethod
    # def update(self, image: Image):
    #     pass

    @abstractmethod
    def delete(self, image: Image):
        pass

    @abstractmethod
    def get_by_id(self, image_id: int) -> Image:
        pass

    @abstractmethod
    def get_all(self) -> list[Image]:
        pass
