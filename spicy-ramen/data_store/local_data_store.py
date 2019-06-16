from .data_store import DataStore

class ImageData:
  def __init__(self, file_id, file_hash, extension):
    self.file_id = file_id
    self.file_hash = file_hash
    self.extension = extension

class LocalDataStore(DataStore):
  def __init__(self):
    self._store = []

  def store_image(self, file_id, file_hash, extension):
    image_data = ImageData(file_id, file_hash, extension)
    self._store.append(image_data)
  
  def load_image(self, file_id):
    for image in self._store:
      print(file_id, vars(image))
      if file_id == image.file_id:
        return image
    return None
  
  def file_exists(self, file_hash):
    return any(file_hash == image.file_hash for image in self._store)