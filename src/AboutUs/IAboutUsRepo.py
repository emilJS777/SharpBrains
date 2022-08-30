from abc import ABC, abstractmethod
from .AboutUsModel import AboutUs


class IAboutUsRepo(ABC):

    @abstractmethod
    def create(self, body: dict):
        pass

    @abstractmethod
    def update(self, about_us: AboutUs, body: dict):
        pass

    @abstractmethod
    def delete(self, about_us: AboutUs):
        pass

    @abstractmethod
    def get_by_id(self, about_us_id: int) -> AboutUs:
        pass

    @abstractmethod
    def get_all(self) -> list[AboutUs]:
        pass
