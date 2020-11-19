import json

from flask import request

from ..controller import controller
from ..service import CausalService
from ..repository import CausalRepository
from ..util.constants import API_ROOT_PATH

@controller.route(API_ROOT_PATH + 'causal', methods=['GET'])
def causal(causal_service: CausalService, causal_repository: CausalRepository):
    return json.dumps(causal_service.get_causal(causal_repository))
