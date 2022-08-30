from abc import ABC, abstractmethod
from .FileModel import File


class IFileRepo(ABC):

    @abstractmethod
    def create(self, filename: str):
        pass

    @abstractmethod
    def update(self, file: File, filename: str):
        pass

    @abstractmethod
    def delete(self, file: File):
        pass

    @abstractmethod
    def get_by_id(self, file_id: int, creator_id: int or None = None) -> File:
        pass

    @abstractmethod
    def get_all(self, page: int, per_page: int) -> dict:
        pass
