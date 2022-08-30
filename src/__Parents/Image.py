from datetime import datetime
import os, base64


class Image:
    @staticmethod
    def get_encode_image(image_path, dir_path):
        with open(os.path.join(dir_path, image_path), 'rb') as binary_file:
            base64_encoded_data = base64.b64encode(binary_file.read())
            return str(base64_encoded_data.decode('utf-8'))

    @staticmethod
    def save_image(image_path: str, image):
        filename = f"{datetime.utcnow().strftime('%B:%d:%Y:%H:%M:%S')}"
        image.save(os.path.join(image_path, filename))
        return filename

    @staticmethod
    def delete_image(image_path, dir_path):
        os.remove(dir_path + '/' + image_path)
