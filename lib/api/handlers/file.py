from aiohttp import web
from aiohttp import streamer
import os

from lib.api.handlers.base import BaseHandler

@streamer
async def file_sender(writer, file_path=None):
    """
    Собственно загрузчик.
    """
    with open(file_path, 'rb') as f:
        chunk = f.read(2 ** 16)
        while chunk:
            await writer.write(chunk)
            chunk = f.read(2 ** 16)

class FileHandler(BaseHandler):
    async def get(self):
        """
        Загрузка файла по заданному пути.
        """
        file_path = self.get_path_param('file_path')
        _, file_name = os.path.split(file_path)

        return web.Response(
            body=file_sender(file_path=file_path),
            headers={
                "Content-disposition": "attachment; filename={file_name}".format(file_name=file_name)
            }
        )