import pandas as pd
import numpy as np
import datetime
from flask import abort
from sqlalchemy.sql.elements import Null
from ..repository import EtapaRepository
from ..util.web_util import format_date
from ..util.web_util import add_wrapper

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
            fechafin = result[4]
            if fechafin is None:
                fechafin = 'No registra'
            else:
                fechafin = str(result[4])
                
            etapas.append(
                {
                    'idetapa': result[0],
                    'radicadoEtapa': result[1],
                    'nombreEtapa': result[2],
                    'fechaInicioEtapa': str(result[3]),
                    'fechaFinEtapa': fechafin,
                    'observacionEtapa': result[5],
                }
            )
        return etapas

    def etapa_insert(self, etapa_repository: EtapaRepository, etapa):
        etapa_repository.etapa_insert_bd(etapa)
        return add_wrapper(['Etapa registrada con éxito!'])

    def etapa_update(self, etapa_repository: EtapaRepository, dataEtapa):
        etapa_repository.etapa_update_bd(dataEtapa)
        return add_wrapper(['Etapa actualizada con éxito!'])

    def etapa_delete(self, etapa_repository: EtapaRepository, etapa):
        etapa_repository.etapa_delete_bd(etapa)
        return add_wrapper(['Etapa borrada con éxito!'])