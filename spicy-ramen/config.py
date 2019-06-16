import os

from data_store import LocalDataStore
from server import Server

class SRConfig:
  def __init__(self, db, asgi_path, media_path):
    self._db = db
    self._asgi_path = asgi_path
    self._media_path = media_path
    self._server = None

  @property
  def db(self):
    return self._db

  @property
  def asgi_path(self):
    return self._asgi_path

  @property
  def media_path(self):
    return self._media_path
  
  @property
  def server(self):
    if self._server is None:
      raise NotImplemented()
    return self._server

  def set_up(self):
    if not os.path.exists(self._media_path):
      os.mkdir(self._media_path)
    if self._db is None:
      db = LocalDataStore()
    self._server = Server(db, self._media_path)
    self._server.open()