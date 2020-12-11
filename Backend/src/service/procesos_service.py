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
            # print('-------------------- CADUCIDAD -----------------', result[2])
    
            procesos.append(
                {
                    'idproceso': result[0],
                    'expediente': result[1],
                    'caducidad': str(result[2]),
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
            caducidad = None
            # print('-------------------- CADUCIDAD -----------------', result[2])

            if result[2]:
                caducidad = str(result[2])
    
            proceso.append(
                {
                    'idproceso': result[0],
                    'expediente': result[1],
                    'caducidad': caducidad,
                    'empresa': result[3].capitalize(),
                    'estado': result[4],
                    'etapa': result[5],
                    'proxetapa': result[6],
                    'servicio': result[7],
                    'usuario': result[8]
                }
            )
        return proceso
    
    def proceso_detalle(self, procesos_repository: ProcesosRepository, idProceso):
        proceso = []
        data = procesos_repository.get_proceso_bd(idProceso)
        for result in data:
            caducidad = None
            print('-------------------- DATA PROCESO -----------------', result)

            if result[2]:
                caducidad = str(result[2])
    
            proceso.append(
                {
                    'idproceso': result[0],
                    'expediente': result[1],
                    'caducidad': caducidad,
                    'empresa': result[3].capitalize(),
                    'causa': result[4],
                    'fecha_hechos': str(result[5]),
                    'descripcion': result[6],
                    'estado': result[7],
                    'etapa': result[8],
                    'proxetapa': result[9],
                    'decision': result[10],
                    'tipo_sancion': result[11],
                    'sancion': result[12],
                    'servicio': result[13],
                    'usuario': result[14]
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
