import pandas as pd
import numpy as np
import datetime
from flask import abort
from ..repository import UsuariosRepository
from ..util.web_util import to_date
from ..util.web_util import add_wrapper

class UsuariosService:

    def get_usuarios(self, usuarios_repository: UsuariosRepository):
        usuarios = []
        data = usuarios_repository.get_usuarios_bd()
        for result in data:
            usuarios.append(
                {
                    'idusuario': result[0],
                    'nombre': result[1],
                    'apellido': str(result[2]),
                    'rol': result[3],
                    'password': result[4],
                }
            )
        return usuarios

    def prueba_insert(self, prueba_repository: UsuariosRepository, nombre_estado):
        prueba_repository.prueba_insert_bd(nombre_estado)
        return add_wrapper(['Insertado con nami'])
