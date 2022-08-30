from .IFileRepo import IFileRepo
from .FileModel import File
from flask import g


class FileRepository(IFileRepo):

    def create(self, filename: str):
        file: File = File()
        file.filename = filename
        file.creator_id = g.user.id
        file.save_db()
        return file

    def update(self, file: File, filename: str):
        file.filename = filename
        file.update_db()

    def delete(self, file: File):
        file.delete_db()

    def get_by_id(self, file_id: int, creator_id: int or None = None) -> File:
        file: File = File.query.filter(File.id == file_id,
                                       File.creator_id == creator_id
                                       if creator_id else
                                       File.creator_id.isnot(None)).first()
        return file

    def get_all(self, page: int, per_page: int) -> dict:
        files = File.query.paginate(page=page, per_page=per_page)
        return files
