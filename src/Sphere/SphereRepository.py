from .ISphereRepo import ISphereRepo
from .SphereModel import Sphere


class SphereRepository(ISphereRepo):

    def create(self, body: dict):
        sphere: Sphere = Sphere()
        sphere.title = body['title']
        sphere.description = body['description']
        sphere.save_db()

    def update(self, sphere: Sphere, body: dict):
        sphere.title = body['title']
        sphere.description = body['description']
        sphere.update_db()

    def delete(self, sphere: Sphere):
        sphere.delete_db()

    def get_by_id(self, sphere_id: int) -> Sphere:
        sphere: Sphere = Sphere.query.filter_by(id=sphere_id).first()
        return sphere

    def get_by_title(self, title: str) -> Sphere:
        sphere: Sphere = Sphere.query.filter_by(title=title).first()
        return sphere

    def get_by_title_exclude_id(self, sphere_id: int, title: str) -> Sphere:
        sphere: Sphere = Sphere.query.filter(Sphere.id != sphere_id, Sphere.title == title).first()
        return sphere

    def get_all(self) -> list[Sphere]:
        spheres: list[Sphere] = Sphere.query.all()
        return spheres
