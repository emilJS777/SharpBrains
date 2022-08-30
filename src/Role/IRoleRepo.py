from abc import ABC, abstractmethod
from .RoleModel import Role


class IRoleRepo(ABC):

    @abstractmethod
    def create(self, name: str, description: str, permissions: list, creator_id: int or None):
        pass

    @abstractmethod
    def update(self, role: Role, name: str, description: str, permissions: list):
        pass

    @abstractmethod
    def delete(self, role: Role):
        pass

    @abstractmethod
    def get_by_id(self, role_id: int) -> Role:
        pass

    @abstractmethod
    def get_by_name(self, name: str) -> Role:
        pass

    @abstractmethod
    def get_by_name_exclude_id(self, role_id: int, name: str) -> Role:
        pass

    @abstractmethod
    def get_all(self) -> list[Role]:
        pass

    @abstractmethod
    def delete_role_permission_binds_by_role_id(self, role_id: int):
        pass
