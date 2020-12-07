from flask_sqlalchemy import SQLAlchemy
from injector import Module, singleton

from .prueba_service import PruebaService
from .empresa_service import EmpresaService
from .procesos_service import ProcesosService
from .servicios_service import ServiciosService
from .usuarios_service import UsuariosService
from .estados_service import EstadosService
from .tiposancion_service import TiposancionService
from .decision_service import DecisionService
from .causal_service import CausalService
from .etapa_service import EtapaService
from .informe_service import InformeService
from .terceros_service import TercerosService

class ServiceModule(Module):
    def configure(self, binder):
        prueba_service = PruebaService()
        empresa_service = EmpresaService()
        procesos_service = ProcesosService()
        servicios_service = ServiciosService()
        usuarios_service = UsuariosService()
        estados_service = EstadosService()
        tiposancion_service = TiposancionService()
        decision_service = DecisionService()
        causal_service = CausalService()
        etapa_service = EtapaService()
        informe_service = InformeService()
        terceros_service = TercerosService()

        binder.bind(PruebaService, to=prueba_service, scope=singleton)
        binder.bind(EmpresaService, to=empresa_service, scope=singleton)
        binder.bind(ProcesosService, to=procesos_service, scope=singleton)
        binder.bind(ServiciosService, to=servicios_service, scope=singleton)
        binder.bind(UsuariosService, to=usuarios_service, scope=singleton)
        binder.bind(EstadosService, to=estados_service, scope=singleton)
        binder.bind(TiposancionService, to=tiposancion_service, scope=singleton)
        binder.bind(DecisionService, to=decision_service, scope=singleton)
        binder.bind(CausalService, to=causal_service, scope=singleton)
        binder.bind(EtapaService, to=etapa_service, scope=singleton)
        binder.bind(InformeService, to=informe_service, scope=singleton)
        binder.bind(TercerosService, to=terceros_service, scope=singleton)
