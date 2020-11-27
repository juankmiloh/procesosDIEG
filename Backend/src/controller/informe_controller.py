import json

from flask import request

from ..controller import controller
from ..service import InformeService
from ..repository import InformeRepository
from ..util.constants import API_ROOT_PATH

@controller.route(API_ROOT_PATH + 'procesos_empresa', methods=['GET'])
def procesosEmpresa(informe_service: InformeService, informe_repository: InformeRepository):
    return json.dumps(informe_service.get_procesos_empresa(informe_repository))

@controller.route(API_ROOT_PATH + 'procesos_causal', methods=['GET'])
def procesosCausas(informe_service: InformeService, informe_repository: InformeRepository):
    return json.dumps(informe_service.get_procesos_causal(informe_repository))

@controller.route(API_ROOT_PATH + 'procesos_estado', methods=['GET'])
def procesosEstado(informe_service: InformeService, informe_repository: InformeRepository):
    return json.dumps(informe_service.get_procesos_estado(informe_repository))

@controller.route(API_ROOT_PATH + 'cantidad_procesos', methods=['GET'])
def procesosCantidad(informe_service: InformeService, informe_repository: InformeRepository):
    return json.dumps(informe_service.get_cantidad_procesos(informe_repository))
