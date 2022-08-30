from abc import ABC, abstractmethod
from .PermissionModel import Permission


class IPermissionRepo(ABC):
    @abstractmethod
    def create(self, name: str, description: str):
        pass

    @abstractmethod
    def update(self, permission: Permission, name: str, description: str):
        pass

    @abstractmethod
    def delete(self, permission: Permission):
        pass

    @abstractmethod
    def get_by_id(self, permission_id: int) -> Permission:
        pass

    @abstractmethod
    def get_by_name(self, name: str) -> Permission:
        pass

    @abstractmethod
    def get_all(self) -> list[Permission]:
        pass
