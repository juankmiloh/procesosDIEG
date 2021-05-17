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

            if result[6]:
                caducidad = str(result[6])
    
            proceso.append(
                {
                    'idproceso': result[0],
                    'expediente': result[1],
                    'servicio': result[2],
                    'empresa': result[3],
                    'usuario': result[4],
                    'estado': result[5],
                    'caducidad': caducidad,
                    'etapa': result[7],
                    'proxetapa': result[8],
                }
            )
        return proceso
    
    def proceso_detalle(self, procesos_repository: ProcesosRepository, idProceso):
        proceso = []
        data = procesos_repository.get_proceso_bd(idProceso)
        for result in data:
            caducidad = None
            print('-------------------- DATA PROCESO -----------------', result)

            if result[9]:
                caducidad = str(result[9])
    
            proceso.append(
                {
                    'idproceso': result[0],
                    'expediente': result[1],
                    'servicio': result[2],
                    'empresa': result[3],
                    'usuario': result[4],
                    'estado': result[5],
                    'tipo_sancion': result[6],
                    'sancion': result[7],
                    'decision': result[8],
                    'caducidad': caducidad,
                    'etapa': result[10],
                    'proxetapa': result[11],
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
