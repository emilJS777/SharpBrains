from .IAboutUsRepo import IAboutUsRepo
from .AboutUsModel import AboutUs


class AboutUsRepository(IAboutUsRepo):

    def create(self, body: dict):
        about_us: AboutUs = AboutUs()
        about_us.title = body['title']
        about_us.sub_title = body['sub_title']
        about_us.description = body['description']
        about_us.save_db()

    def update(self, about_us: AboutUs, body: dict):
        about_us.title = body['title']
        about_us.sub_title = body['sub_title']
        about_us.description = body['description']
        about_us.update_db()

    def delete(self, about_us: AboutUs):
        about_us.delete_db()

    def get_by_id(self, about_us_id: int) -> AboutUs:
        about_us: AboutUs = AboutUs.query.filter_by(id=about_us_id).first()
        return about_us

    def get_all(self) -> list[AboutUs]:
        about_uses: list[AboutUs] = AboutUs.query.all()
        return about_uses
