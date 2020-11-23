import json

from flask import request

from ..controller import controller
from ..service import EtapaService
from ..repository import EtapaRepository
from ..util.constants import API_ROOT_PATH

@controller.route(API_ROOT_PATH + 'etapas', methods=['GET'])
def etapa(etapa_service: EtapaService, etapa_repository: EtapaRepository):
    return json.dumps(etapa_service.get_etapa(etapa_repository))

# Obtener detalle de las etapas de un proceso
@controller.route(API_ROOT_PATH + 'etapa_proceso', methods=['GET'])
def getEtapaProceso(etapa_service: EtapaService, etapa_repository: EtapaRepository):
    # Id proceso
    idProceso = request.args.get('idProceso', default='', type=str)
    return json.dumps(etapa_service.get_etapa_proceso(etapa_repository, idProceso))
