import os

class Server:
  def __init__(self, db):
    self._db = db
  
  def open(self):
    self._is_open = True
  
  def close(self):
    self._is_open = False

  async def store_photo(self, upload_file):
    path = os.path.join('text.png')
    with open(path, 'wb') as file:
      file.write(await upload_file.read())
    return path