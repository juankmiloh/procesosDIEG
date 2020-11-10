import pandas as pd
import numpy as np
import datetime
from flask import abort
from ..repository import ProcesosRepository
from ..util.web_util import to_date
from ..util.web_util import add_wrapper


class ProcesosService:

    def get_procesos(self, procesos_repository: ProcesosRepository):
        procesos = []
        data = procesos_repository.get_procesos_bd()
        for result in data:
            procesos.append(
                {
                    'idproceso': result[0],
                    'radicado': result[1],
                    'fecha': str(result[2]),
                    'empresa': result[3],
                    'estado': result[4],
                    'servicio': result[5],
                    'usuario': result[6],
                }
            )
        return procesos

    def proceso_insert(self, procesos_repository: ProcesosRepository, proceso):
        procesos_repository.proceso_insert_bd(proceso)
        return add_wrapper(['Proceso insertado con éxito!'])
