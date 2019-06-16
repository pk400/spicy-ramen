import hashlib
import os
import uuid

class Server:
  def __init__(self, db, media_path):
    self._db = db
    self._media_path = media_path
  
  def open(self):
    self._is_open = True
  
  def close(self):
    self._is_open = False

  async def store_photo(self, upload_file):
    file_extension = upload_file.filename.split('.')[1]
    file_id = self._generate_id()
    file_path = os.path.join(self._media_path,
      '.'.join([file_id, file_extension]))
    with open(file_path, 'wb') as file:
      upload_file_data = await upload_file.read()
      file_hash = self._generate_checksum(upload_file_data)
      if self._db.file_exists(file_hash):
        raise OSError
      file.write(upload_file_data)
      self._db.store_image(file_id, file_hash, file_extension)
    return file_id
  
  async def load_photo(self, file_id):
    image = self._db.load_image(file_id)
    return os.path.join(self._media_path,
      '.'.join([file_id, image.extension]))
  
  def _generate_id(self):
    return uuid.uuid4().hex
  
  def _generate_checksum(self, data):
    return hashlib.md5(data).hexdigest()