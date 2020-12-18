import json

from flask import request

from ..controller import controller
from ..service import CausalService
from ..repository import CausalRepository
from ..util.constants import API_ROOT_PATH

@controller.route(API_ROOT_PATH + 'causal', methods=['GET'])
def causal(causal_service: CausalService, causal_repository: CausalRepository):
    return json.dumps(causal_service.get_causal(causal_repository))

# Obtener detalle de los causal de un proceso
@controller.route(API_ROOT_PATH + 'causal_proceso', methods=['GET'])
def getCausalProceso(causal_service: CausalService, causal_repository: CausalRepository):
    # Id proceso
    idProceso = request.args.get('idProceso', default='', type=str)
    return json.dumps(causal_service.get_causal_proceso(causal_repository, idProceso))

# Crear un causal
@controller.route(API_ROOT_PATH + 'causal', methods=['POST'])
def createCausal(causal_service: CausalService, causal_repository: CausalRepository):
    causal = request.json
    return json.dumps(causal_service.causal_insert(causal_repository, causal))

# Actualizar causal
@controller.route(API_ROOT_PATH + 'causal', methods=['PUT'])
def updateCausal(causal_service: CausalService, causal_repository: CausalRepository):
    # Datos causal
    datacausal = request.json
    return json.dumps(causal_service.causal_update(causal_repository, datacausal))

# Eliminar un causal
@controller.route(API_ROOT_PATH + 'causal', methods=['DELETE'])
def deleteCausal(causal_service: CausalService, causal_repository: CausalRepository):
    # Datos causal
    causal = request.json
    return json.dumps(causal_service.causal_delete(causal_repository, causal))