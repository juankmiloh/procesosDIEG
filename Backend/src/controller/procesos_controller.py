import json

from flask import request

from ..controller import controller
from ..service import ProcesosService
from ..repository import ProcesosRepository
from ..util.constants import API_ROOT_PATH


@controller.route(API_ROOT_PATH + 'procesos', methods=['GET'])
def procesos(procesos_service: ProcesosService, procesos_repository: ProcesosRepository):
    return json.dumps(procesos_service.get_procesos(procesos_repository))


@controller.route(API_ROOT_PATH + 'procesos', methods=['POST'])
def procesos_insert(procesos_service: ProcesosService, procesos_repository: ProcesosRepository):
    proceso = request.json
    return json.dumps(procesos_service.proceso_insert(procesos_repository, proceso))
