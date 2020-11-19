import pandas as pd
import numpy as np
import datetime
from flask import abort
from sqlalchemy.sql.elements import Null
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
                    'empresa': result[3].capitalize(),
                    'estado': result[4],
                    'servicio': result[5],
                    'idusuario': result[6],
                    'usuario': result[7],
                }
            )
        return procesos

    def proceso_detalle_inicial(self, procesos_repository: ProcesosRepository, idProceso):
        proceso = []
        data = procesos_repository.get_proceso_inicial_bd(idProceso)
        for result in data:

            proceso.append(
                {
                    'idproceso': result[0],
                    'expediente': result[1],
                    'servicio': result[2],
                    'empresa': result[3].capitalize(),
                    'usuario': result[4],
                    'estado': result[5],
                    'sancion': result[6],
                    'caducidad': str(result[7]),
                    'etapa': result[9].capitalize(),
                    'proxetapa': result[11].capitalize()
                }
            )
        return proceso
    
    def proceso_detalle(self, procesos_repository: ProcesosRepository, idProceso):
        proceso = []
        data = procesos_repository.get_proceso_bd(idProceso)
        for result in data:
            fechahechos = result[10]
            if fechahechos:
                fechahechos = format_date(result[10])

            proceso.append(
                {
                    'idproceso': result[0],
                    'expediente': result[1],
                    'servicio': result[2],
                    'empresa': result[3].capitalize(),
                    'usuario': result[4],
                    'estado': result[5],
                    'tipo_sancion': result[6],
                    'sancion': result[7],
                    'decision': result[8],
                    'causa': result[9],
                    'fecha_hechos': str(result[10]),
                    'descripcion': result[11],
                    'caducidad': str(result[12]),
                    'etapa': result[14].capitalize(),
                    'proxetapa': result[16].capitalize()
                }
            )
        return proceso

    def proceso_insert(self, procesos_repository: ProcesosRepository, proceso):
        procesos_repository.proceso_insert_bd(proceso)
        return add_wrapper(['Expediente registrado con éxito!'])
    
    def proceso_usuario_update(self, procesos_repository: ProcesosRepository, dataProceso):
        procesos_repository.proceso_usuario_update_bd(dataProceso)
        return add_wrapper(['Expediente actualizado con éxito!'])
    
    def proceso_update(self, procesos_repository: ProcesosRepository, dataProceso):
        procesos_repository.proceso_update_bd(dataProceso)
        return add_wrapper(['Expediente actualizado con éxito!'])

    def proceso_delete(self, procesos_repository: ProcesosRepository, proceso):
        procesos_repository.proceso_delete_bd(proceso)
        return add_wrapper(['Expediente borrado con éxito!'])
