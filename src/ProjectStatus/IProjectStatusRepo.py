from abc import ABC, abstractmethod
from .ProjectStatusModel import ProjectStatus


class IProjectStatusRepo(ABC):

    @abstractmethod
    def create(self, body: dict):
        pass

    @abstractmethod
    def update(self, project_status: ProjectStatus, body: dict):
        pass

    @abstractmethod
    def delete(self, project_status: ProjectStatus):
        pass

    @abstractmethod
    def get_by_title(self, title: str):
        pass

    @abstractmethod
    def get_by_title_exclude_id(self, project_status_id: int, title: str):
        pass

    @abstractmethod
    def get_by_id(self, project_status_id: int):
        pass

    @abstractmethod
    def get_all(self):
        pass
