from src.__Parents.Repository import Repository
from src.__Parents.Service import Service
from .ISphereRepo import ISphereRepo


class SphereService(Service, Repository):

    def __init__(self, sphere_repository: ISphereRepo):
        self.sphere_repository: ISphereRepo = sphere_repository

    def create(self, body: dict) -> dict:
        if self.sphere_repository.get_by_title(title=body['title']):
            return self.response_conflict('sphere by this title exist')

        self.sphere_repository.create(body)
        return self.response_created('sphere successfully created')

    def update(self, sphere_id: int, body: dict) -> dict:
        sphere = self.sphere_repository.get_by_id(sphere_id=sphere_id)

        if not sphere:
            return self.response_not_found('sphere not found')

        if self.sphere_repository.get_by_title_exclude_id(sphere_id=sphere_id, title=body['title']):
            return self.response_conflict('sphere by this title exist')

        self.sphere_repository.update(sphere=sphere, body=body)
        return self.response_updated('sphere successfully updated')

    def delete(self, sphere_id: int) -> dict:
        sphere = self.sphere_repository.get_by_id(sphere_id=sphere_id)

        if not sphere:
            return self.response_not_found('sphere not found')

        self.sphere_repository.delete(sphere=sphere)
        return self.response_deleted('sphere successfully deleted')

    def get_by_id(self, sphere_id) -> dict:
        sphere = self.sphere_repository.get_by_id(sphere_id=sphere_id)

        if not sphere:
            return self.response_not_found('sphere not found')

        return self.response_ok(self.get_dict_items(sphere))

    def get_all(self) -> dict:
        spheres = self.sphere_repository.get_all()
        return self.response_ok(self.get_array_items(spheres))
