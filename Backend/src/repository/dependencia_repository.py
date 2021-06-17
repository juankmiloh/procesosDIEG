from sqlalchemy.sql import text


class DependenciaRepository:
    def __init__(self, db):
        self.db = db

    def get_dependencia_bd(self, iddependencia):
        sql = '''
            SELECT * FROM DEPENDENCIA
            WHERE IDDEPENDENCIA = :IDDEPENDENCIA_ARG OR 0 = :IDDEPENDENCIA_ARG;
        '''
        return self.db.engine.execute(text(sql), IDDEPENDENCIA_ARG=iddependencia).fetchall()