from abc import ABC, abstractmethod
from .ProjectModel import Project


class IProjectRepo(ABC):

    @abstractmethod
    def create(self, body: dict):
        pass

    @abstractmethod
    def update(self, project: Project, body: dict):
        pass

    @abstractmethod
    def delete(self, project: Project):
        pass

    @abstractmethod
    def get_by_id(self, project_id: int) -> Project:
        pass

    @abstractmethod
    def get_by_title(self, title: str) -> Project:
        pass

    @abstractmethod
    def get_by_title_exclude_id(self, project_id: int, title: str) -> Project:
        pass

    @abstractmethod
    def get_all(self, page: int, per_page: int, sphere_id: int or None, project_status_id: int or None):
        pass
