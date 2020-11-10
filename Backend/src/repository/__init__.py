from flask_sqlalchemy import SQLAlchemy
from injector import Module, singleton

from .prueba_repository import PruebaRepository
from .empresa_repository import EmpresaRepository
from .procesos_repository import ProcesosRepository
from .servicios_repository import ServiciosRepository
from .usuarios_repository import UsuariosRepository


class RepositoryModule(Module):
    def __init__(self, db):
        self.db = db

    def configure(self, binder):
        prueba_repository = PruebaRepository(self.db)
        empresa_repository = EmpresaRepository(self.db)
        procesos_repository = ProcesosRepository(self.db)
        servicios_repository = ServiciosRepository(self.db)
        usuarios_repository = UsuariosRepository(self.db)

        binder.bind(PruebaRepository, to=prueba_repository, scope=singleton)
        binder.bind(EmpresaRepository, to=empresa_repository, scope=singleton)
        binder.bind(ProcesosRepository, to=procesos_repository, scope=singleton)
        binder.bind(ServiciosRepository, to=servicios_repository, scope=singleton)
        binder.bind(UsuariosRepository, to=usuarios_repository, scope=singleton)
