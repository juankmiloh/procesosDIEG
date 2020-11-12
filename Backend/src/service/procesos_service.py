import pandas as pd
import numpy as np
import datetime
from flask import abort
from ..repository import ProcesosRepository
from ..util.web_util import format_date
from ..util.web_util import add_wrapper


class ProcesosService:

    def get_procesos(self, procesos_repository: ProcesosRepository):
        procesos = []
        data = procesos_repository.get_procesos_bd()
        for result in data:
            procesos.append(
                {
                    'idproceso': result[0],
                    'expediente': result[1],
                    'caducidad': format_date(result[2]),
                    'empresa': result[3],
                    'estado': result[4],
                    'servicio': result[5],
                    'idusuario': result[6],
                    'usuario': result[7],
                }
            )
        return procesos

    def proceso_detalle(self, procesos_repository: ProcesosRepository, idProceso):
        proceso = []
        data = procesos_repository.get_proceso_bd(idProceso)
        for result in data:
            proceso.append(
                {
                    'idproceso': result[0],
                    'expediente': result[1],
                    'caducidad': str(result[2]),
                    'empresa': result[3],
                    'estado': result[4],
                    'servicio': result[5],
                    'idusuario': result[6],
                    'usuario': result[7],
                }
            )
        return proceso

    def proceso_insert(self, procesos_repository: ProcesosRepository, proceso):
        procesos_repository.proceso_insert_bd(proceso)
        return add_wrapper(['Expediente registrado con éxito!'])
    
    def proceso_update(self, procesos_repository: ProcesosRepository, dataProceso):
        procesos_repository.proceso_update_bd(dataProceso)
        return add_wrapper(['Expediente actualizado con éxito!'])

    def proceso_delete(self, procesos_repository: ProcesosRepository, proceso):
        procesos_repository.proceso_delete_bd(proceso)
        return add_wrapper(['Expediente borrado con éxito!'])
