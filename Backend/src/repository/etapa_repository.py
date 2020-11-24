from sqlalchemy.sql import text


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
                AND PROCESO = :IDPROCESO_ARG;
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
        resultsql = self.db.engine.execute(text(sql), ETAPA_ARG=etapa["etapa"], IDPROCESO_ARG=etapa["idproceso"], FECHAINICIO_ARG=etapa["fecha_inicio"], FECHAFIN_ARG=etapa["fecha_fin"], RADICADO_ARG=etapa["radicado"], OBSERVACION_ARG=etapa["observacion"])

        return resultsql