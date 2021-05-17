from ..repository import ServiciosRepository

class ServiciosService:

    def get_servicios(self, servicios_repository: ServiciosRepository):
        servicios = []
        data = servicios_repository.get_servicios_bd()
        for result in data:
            servicios.append(
                {
                    'idservicio': result[0],
                    'servicio': result[1],
                }
            )
        return servicios