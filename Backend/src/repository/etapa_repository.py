from sqlalchemy.sql import text


class EtapaRepository:
    def __init__(self, db):
        self.db = db

    def get_etapa_bd(self):
        sql = '''
            SELECT * FROM ETAPA;
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