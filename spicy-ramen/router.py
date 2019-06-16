import os

from starlette.responses import FileResponse
from starlette.routing import Router

def SRApplication(server):
  SRRouter = Router()

  @SRRouter.route('/store_photo', methods=['POST'])
  async def on_store_photo(request):
    form_data = await request.form()
    file_path = await server.store_photo(form_data['photo_file'])
    return FileResponse(file_path)

  return SRRouter