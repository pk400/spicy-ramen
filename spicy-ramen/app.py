from starlette.applications import Starlette
import uvicorn

from router import SRApplication
from server import Server

if __name__ == '__main__':
  server = Server(None)
  server.open()
  app = Starlette()
  app.mount('/api/photos', SRApplication(server))
  uvicorn.run(app)