from abc import ABC, abstractmethod
from .UserImageModel import UserImage


class IUserImageRepo(ABC):

    @abstractmethod
    def create(self, filename: str, main: bool):
        pass

    @abstractmethod
    def update(self, user_image: UserImage, main: bool):
        pass

    @abstractmethod
    def delete(self, user_image: UserImage):
        pass

    @abstractmethod
    def get_by_main(self) -> UserImage:
        pass

    @abstractmethod
    def get_by_id(self, user_image_id: int) -> UserImage:
        pass

    @abstractmethod
    def get_all(self) -> list[UserImage]:
        pass
