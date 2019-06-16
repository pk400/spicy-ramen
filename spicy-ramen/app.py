import os

from starlette.applications import Starlette
import uvicorn

from config import SRConfig
from router import SRApplication
from server import Server

if __name__ == '__main__':
  dirname = os.path.dirname(__file__)
  config = SRConfig(
    db=None,
    asgi_path = '/api/photos',
    media_path=os.path.join(dirname, 'media'))
  config.set_up()
  app = Starlette()
  app.mount(config.asgi_path, SRApplication(config.server))
  uvicorn.run(app)