import json
import pandas as pd
import numpy as np
import datetime
from flask import abort
from ..repository import UsuariosRepository
from ..util.web_util import to_date
from ..util.web_util import add_wrapper

class UsuariosService:

    def login_usuario(self, usuarios_repository: UsuariosRepository, usuario):
        response = {}
        data = usuarios_repository.autenticar_usuario(usuario)
        for result in data:
            response = { 'code': 20000, 'data': { 'token': result[0] } }
        return response

    def info_usuario(self, usuarios_repository: UsuariosRepository, token):
        responseGetInfo = {}
        data = usuarios_repository.getData_usuario(token)
        for result in data:
            responseGetInfo = {
                "code": 20000,
                "data": {
                    "roles": [result[0]],
                    "introduction": result[1],
                    "avatar": result[2],
                    "name": result[3]
                }
            }
        return responseGetInfo

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

    def get_nicknames(self, usuarios_repository: UsuariosRepository):
        nicknames = []
        data = usuarios_repository.get_nicknames_bd()
        for result in data:
            nicknames.append(result[0])
        return nicknames

    def prueba_insert(self, prueba_repository: UsuariosRepository, nombre_estado):
        prueba_repository.prueba_insert_bd(nombre_estado)
        return add_wrapper(['Insertado con nami'])
