import json

from flask import request

from ..controller import controller
from ..service import InformeService
from ..repository import InformeRepository
from ..util.constants import API_ROOT_PATH

@controller.route(API_ROOT_PATH + 'informe', methods=['GET'])
def informe(informe_service: InformeService, informe_repository: InformeRepository):
    return json.dumps(informe_service.get_informe(informe_repository))
