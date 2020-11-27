import pandas as pd
import numpy as np
import datetime
from flask import abort
from ..repository import InformeRepository
from ..util.web_util import to_date
from ..util.web_util import add_wrapper

class InformeService:

    def get_cantidad_procesos(self, informe_repository: InformeRepository):
        procesos = []
        data = informe_repository.get_cantidad_procesos_bd()
        for result in data:
            procesos.append(
                {
                    'cantidad': result[0],
                    'fase': result[1]
                }
            )
        return procesos

    def get_procesos_empresa(self, informe_repository: InformeRepository):
        pieChartData = {}

        empPactivos = []
        pactivos = []
        empPterminados = []
        pterminados = []
        empPeliminados = []
        peliminados = []

        data = informe_repository.get_procesos_empresa_bd(1)
        for result in data:
            empPactivos.append(result[1])
            pactivos.append(
                {
                    'value': result[0],
                    'name': result[1]
                }
            )

        data = informe_repository.get_procesos_empresa_bd(2)
        for result in data:
            empPterminados.append(result[1])
            pterminados.append(
                {
                    'value': result[0],
                    'name': result[1]
                }
            )

        data = informe_repository.get_procesos_empresa_bd(3)
        for result in data:
            empPeliminados.append(result[1])
            peliminados.append(
                {
                    'value': result[0],
                    'name': result[1]
                }
            )
        
        pieChartData = {
            'activos': {
                'title': 'Procesos activos',
                'leyenda': empPactivos,
                'datos': pactivos
            },
            'terminados': {
                'title': 'Procesos terminados',
                'leyenda': empPterminados,
                'datos': pterminados
            },
            'eliminados': {
                'title': 'Procesos eliminados',
                'leyenda': empPeliminados,
                'datos': peliminados
            }
        }
        return pieChartData

    def get_procesos_causal(self, informe_repository: InformeRepository):
        pieChartData = {}

        empPactivos = []
        pactivos = []
        empPterminados = []
        pterminados = []
        empPeliminados = []
        peliminados = []

        data = informe_repository.get_procesos_causal_bd(1)
        for result in data:
            empPactivos.append(result[1])
            pactivos.append(
                {
                    'value': result[0],
                    'name': result[1]
                }
            )

        data = informe_repository.get_procesos_causal_bd(2)
        for result in data:
            empPterminados.append(result[1])
            pterminados.append(
                {
                    'value': result[0],
                    'name': result[1]
                }
            )

        data = informe_repository.get_procesos_causal_bd(3)
        for result in data:
            empPeliminados.append(result[1])
            peliminados.append(
                {
                    'value': result[0],
                    'name': result[1]
                }
            )
        
        pieChartData = {
            'activos': {
                'title': 'Procesos activos',
                'leyenda': empPactivos,
                'datos': pactivos
            },
            'terminados': {
                'title': 'Procesos terminados',
                'leyenda': empPterminados,
                'datos': pterminados
            },
            'eliminados': {
                'title': 'Procesos eliminados',
                'leyenda': empPeliminados,
                'datos': peliminados
            }
        }
        return pieChartData
    
    def get_procesos_estado(self, informe_repository: InformeRepository):
        pieChartData = {}

        empPactivos = []
        pactivos = []
        empPterminados = []
        pterminados = []
        empPeliminados = []
        peliminados = []

        data = informe_repository.get_procesos_estado_bd(1)
        for result in data:
            empPactivos.append(result[1])
            pactivos.append(
                {
                    'value': result[0],
                    'name': result[1]
                }
            )

        data = informe_repository.get_procesos_estado_bd(2)
        for result in data:
            empPterminados.append(result[1])
            pterminados.append(
                {
                    'value': result[0],
                    'name': result[1]
                }
            )

        data = informe_repository.get_procesos_estado_bd(3)
        for result in data:
            empPeliminados.append(result[1])
            peliminados.append(
                {
                    'value': result[0],
                    'name': result[1]
                }
            )
        
        pieChartData = {
            'activos': {
                'title': 'Procesos activos',
                'leyenda': empPactivos,
                'datos': pactivos
            },
            'terminados': {
                'title': 'Procesos terminados',
                'leyenda': empPterminados,
                'datos': pterminados
            },
            'eliminados': {
                'title': 'Procesos eliminados',
                'leyenda': empPeliminados,
                'datos': peliminados
            }
        }
        return pieChartData