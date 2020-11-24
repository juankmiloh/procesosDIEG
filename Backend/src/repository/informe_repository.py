from sqlalchemy.sql import text


class InformeRepository:
    def __init__(self, db):
        self.db = db

    def get_informe_bd(self):
        sql = '''
            SELECT 
                P.EMPRESA,
                EMP.NOMBRE,
                COUNT(*)
            FROM PROCESO P, EMPRESA EMP
            WHERE P.EMPRESA = EMP.IDEMPRESA
            GROUP BY EMPRESA, EMP.NOMBRE;
        '''
        return self.db.engine.execute(text(sql)).fetchall()