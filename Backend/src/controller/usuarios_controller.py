import json

from flask import request

from ..controller import controller
from ..service import UsuariosService
from ..repository import UsuariosRepository
from ..util.constants import API_ROOT_PATH

@controller.route(API_ROOT_PATH + 'usuarios', methods=['GET'])
def usuarios(usuarios_service: UsuariosService, usuarios_repository: UsuariosRepository):
    return json.dumps(usuarios_service.get_usuarios(usuarios_repository))
