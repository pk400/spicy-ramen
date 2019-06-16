import os

from starlette.responses import FileResponse, Response
from starlette.routing import Router

def SRApplication(server):
  app = Router()

  @app.route('/store_photo', methods=['POST'])
  async def on_store_photo(request):
    form_data = await request.form()
    file_id = await server.store_photo(form_data['photo_file'])
    return Response(file_id, status_code=200)
  
  @app.route('/load_photo/{file_id}', methods=['GET'])
  async def on_load_photo(request):
    file_id = request.path_params['file_id']
    image_path = await server.load_photo(file_id)
    return FileResponse(image_path)

  return app