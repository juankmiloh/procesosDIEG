from sqlalchemy.sql import text
from sqlalchemy.sql.elements import Null


class EtapaRepository:
    def __init__(self, db):
        self.db = db

    def get_etapa_bd(self):
        sql = '''
            SELECT * FROM ETAPA ORDER BY IDETAPA DESC;
        '''
        return self.db.engine.execute(text(sql)).fetchall()
    
    def get_etapa_proceso_bd(self, idProceso):
        sql = '''
            SELECT 
                EP.RADICADOETAPA,
                E.NOMBRE,
                EP.FECHAINICIOETAPA,
                EP.FECHAFINETAPA,
                EP.OBSERVACIONETAPA 
            FROM ETAPA_PROCESO EP, ETAPA E
            WHERE
                EP.ETAPA = E.IDETAPA
                AND PROCESO = :IDPROCESO_ARG
            ORDER BY EP.ETAPA;
        '''
        return self.db.engine.execute(text(sql), IDPROCESO_ARG=idProceso).fetchall()

    def etapa_insert_bd(self, etapa):
        print('-------------------------------------')
        print('OBJ ETAPA -> ', etapa)
        print('-------------------------------------')
        sql = '''
            INSERT INTO ETAPA_PROCESO(ETAPA, PROCESO, FECHAINICIOETAPA, FECHAFINETAPA, RADICADOETAPA, OBSERVACIONETAPA)
            VALUES (:ETAPA_ARG, :IDPROCESO_ARG, :FECHAINICIO_ARG, :FECHAFIN_ARG, :RADICADO_ARG, :OBSERVACION_ARG);

        '''
        resultsql = self.db.engine.execute(text(sql), ETAPA_ARG=etapa["etapa"], IDPROCESO_ARG=etapa["idproceso"], FECHAINICIO_ARG=etapa["fechaInicioEtapa"], FECHAFIN_ARG=etapa["fechaFinEtapa"], RADICADO_ARG=etapa["radicadoEtapa"], OBSERVACION_ARG=etapa["observacionEtapa"])

        return resultsql

    def etapa_update_bd(self, etapa):
        print('-------------------------------------')
        print('* ETAPA A ACTUALIZAR -> ', etapa)
        print('-------------------------------------')

        if etapa["fechaFinEtapa"] == 'Invalid date':
            etapa["fechaFinEtapa"] = None

        sql = '''
            UPDATE 
                ETAPA_PROCESO
	        SET 
                FECHAINICIOETAPA= :FECHAINICIO_ARG,
                FECHAFINETAPA = :FECHAFIN_ARG,
                RADICADOETAPA = :RADICADO_ARG,
                OBSERVACIONETAPA = :OBSERVACION_ARG
	        WHERE RADICADOETAPA = :RADICADO_ARG;
        '''
        resultsql = self.db.engine.execute(text(sql), FECHAINICIO_ARG=etapa["fechaInicioEtapa"], FECHAFIN_ARG=etapa["fechaFinEtapa"], RADICADO_ARG=etapa["radicadoEtapa"], OBSERVACION_ARG=etapa["observacionEtapa"])

        return resultsql

    def etapa_delete_bd(self, radicadoEtapa):
        print('-------------------------------------')
        print('* ETAPA A ELIMINAR -> ', radicadoEtapa)
        print('-------------------------------------')
        sql = '''
            DELETE FROM ETAPA_PROCESO
            WHERE RADICADOETAPA = :RADICADO_ARG;
        '''
        resultsql = self.db.engine.execute(text(sql), RADICADO_ARG=radicadoEtapa)

        return resultsql