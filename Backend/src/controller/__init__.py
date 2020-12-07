from flask import Blueprint
from flask_cors import CORS

controller = Blueprint('controller', __name__, url_prefix='/')

# src.controller
from . import front_controller, prueba_controller, empresa_controller, procesos_controller, servicios_controller, usuarios_controller, estados_controller, tiposancion_controller, decision_controller, causal_controller, etapa_controller, informe_controller, terceros_controller
