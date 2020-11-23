import pandas as pd
import numpy as np
import datetime
from flask import abort
from sqlalchemy.sql.elements import Null
from ..repository import EtapaRepository
from ..util.web_util import format_date

class EtapaService:

    def get_etapa(self, etapa_repository: EtapaRepository):
        etapa = []
        data = etapa_repository.get_etapa_bd()
        for result in data:
            etapa.append(
                {
                    'idetapa': result[0],
                    'idestado': result[1],
                    'nombre': result[2],
                    'prox_etapa': result[3],
                    'estampilla': result[4],
                }
            )
        return etapa

    def get_etapa_proceso(self, etapa_repository: EtapaRepository, idproceso):
        etapas = []
        fechafin = ''
        data = etapa_repository.get_etapa_proceso_bd(idproceso)
        for result in data:
            fechafin = result[3]
            if fechafin is None:
                fechafin = 'No registra'
            else:
                fechafin = format_date(result[2])
                
            etapas.append(
                {
                    'radicadoEtapa': result[0],
                    'nombreEtapa': result[1],
                    'fechaInicioEtapa': format_date(result[2]),
                    'fechaFinEtapa': fechafin,
                    'observacionEtapa': result[4],
                }
            )
        return etapas