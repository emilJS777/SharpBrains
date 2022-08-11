from abc import ABC, abstractmethod
from .SphereModel import Sphere


class ISphereRepo(ABC):

    @abstractmethod
    def create(self, body: dict):
        pass

    @abstractmethod
    def update(self, sphere: Sphere, body: dict):
        pass

    @abstractmethod
    def delete(self, sphere: Sphere):
        pass

    @abstractmethod
    def get_by_id(self, sphere_id: int) -> Sphere:
        pass

    @abstractmethod
    def get_by_title(self, title: str) -> Sphere:
        pass

    @abstractmethod
    def get_by_title_exclude_id(self, sphere_id: int, title: str) -> Sphere:
        pass

    @abstractmethod
    def get_all(self) -> list[Sphere]:
        pass
