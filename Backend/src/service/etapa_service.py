from ..repository import EtapaRepository
from ..util.web_util import add_wrapper

class EtapaService:

    def get_etapa(self, etapa_repository: EtapaRepository):
        etapa = []
        data = etapa_repository.get_etapa_bd()
        for result in data:
            etapa.append(
                {
                    'id': result[0],
                    'nombre': str(result[0]) + " - " + result[1],
                    'obligatoriedad': result[2],
                    'fecha_final': result[3],
                    'varios_actos': result[4],
                    'observacion': result[5],
                    'siguiente_estado': result[6],
                }
            )
        return etapa

    def get_etapa_proceso(self, etapa_repository: EtapaRepository, idproceso, idEtapa):
        etapas = []
        etapaAnterior = 0
        etapaActual = 0
        index = -1
        data = etapa_repository.get_etapa_proceso_bd(idproceso, idEtapa)
        for result in data:
            etapaActual = result[0]
            fechafin = result[4]
            if fechafin is None: 
                fechafin = None # Se reasigna el valor porque no toma el 'None (null)' desde el front
            else:
                fechafin = str(result[4]) # Se convierte a string para poder retornar la fecha
            fechainicio = result[3]
            if fechainicio is None:
                fechainicio = None
            else:
                fechainicio = str(result[3])
            
            if etapaActual != etapaAnterior:
                etapas.append(
                    {
                        'idetapa': result[0],
                        'nombre': result[6],
                        'obligatoriedad': result[7],
                        'fecha_final': result[8],
                        'varios_actos': result[9],
                        'observacion': result[10],
                        'siguiente_estado': result[11],
                        'actos': [{
                            'etapa': result[0],
                            'numeroacto': result[1],
                            'radicado': result[2],
                            'fechaInicio': fechainicio,
                            'fechaFin': fechafin,
                            'observacion': result[5]
                        }]
                    }
                )
                etapaAnterior = etapaActual
                index = index + 1
            else:
                etapas[index]['actos'].append(
                    {
                        'etapa': result[0],
                        'numeroacto': result[1],
                        'radicado': result[2],
                        'fechaInicio': str(result[3]),
                        'fechaFin': fechafin,
                        'observacion': result[5]
                    }
                )

        return etapas

    def etapa_insert(self, etapa_repository: EtapaRepository, etapa):
        etapa_repository.etapa_insert_bd(etapa)
        return add_wrapper(['Etapa registrada con éxito!'])

    def etapa_update(self, etapa_repository: EtapaRepository, dataEtapa):
        etapa_repository.etapa_update_bd(dataEtapa)
        return add_wrapper(['Etapa actualizada con éxito!'])

    def etapa_delete(self, etapa_repository: EtapaRepository, etapa):
        etapa_repository.etapa_delete_bd(etapa)
        return add_wrapper(['Etapa borrada con éxito!'])