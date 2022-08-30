from datetime import datetime
import os


class File:

    @staticmethod
    def save_file(file_path: str, file):
        filename = file.filename
        file.save(os.path.join(file_path, filename))
        return filename

    @staticmethod
    def delete_file(file_path, dir_path):
        os.remove(dir_path + '/' + file_path)
