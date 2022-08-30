from .IAboutUsRepo import IAboutUsRepo
from ..__Parents.Repository import Repository
from ..__Parents.Service import Service


class AboutUsService(Service, Repository):
    def __init__(self, about_us_repository: IAboutUsRepo):
        self.about_us_repository: IAboutUsRepo = about_us_repository

    def create(self, body: dict) -> dict:
        self.about_us_repository.create(body)
        return self.response_created("about us successfully created")

    def update(self, about_us_id: int, body: dict) -> dict:
        about_us = self.about_us_repository.get_by_id(about_us_id)
        if not about_us:
            return self.response_not_found('about us not found')

        self.about_us_repository.update(about_us=about_us, body=body)
        return self.response_updated('about us successfully updated')

    def delete(self, about_us_id: int) -> dict:
        about_us = self.about_us_repository.get_by_id(about_us_id)
        if not about_us:
            return self.response_not_found('about us not found')

        self.about_us_repository.delete(about_us)
        return self.response_deleted('about us successfully deleted')

    def get_by_id(self, about_us_id: int) -> dict:
        about_us = self.about_us_repository.get_by_id(about_us_id)
        if not about_us:
            return self.response_not_found('about us not found')
        return self.response_ok(self.get_dict_items(about_us))

    def get_all(self) -> dict:
        about_uses = self.about_us_repository.get_all()
        return self.response_ok(self.get_array_items(about_uses))
