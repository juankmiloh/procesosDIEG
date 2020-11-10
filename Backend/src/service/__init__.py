from flask_sqlalchemy import SQLAlchemy
from injector import Module, singleton

from .prueba_service import PruebaService
from .empresa_service import EmpresaService
from .procesos_service import ProcesosService
from .servicios_service import ServiciosService
from .usuarios_service import UsuariosService

class ServiceModule(Module):
    def configure(self, binder):
        prueba_service = PruebaService()
        empresa_service = EmpresaService()
        procesos_service = ProcesosService()
        servicios_service = ServiciosService()
        usuarios_service = UsuariosService()

        binder.bind(PruebaService, to=prueba_service, scope=singleton)
        binder.bind(EmpresaService, to=empresa_service, scope=singleton)
        binder.bind(ProcesosService, to=procesos_service, scope=singleton)
        binder.bind(ServiciosService, to=servicios_service, scope=singleton)
        binder.bind(UsuariosService, to=usuarios_service, scope=singleton)
