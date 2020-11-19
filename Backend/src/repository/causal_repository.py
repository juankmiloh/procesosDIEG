from sqlalchemy.sql import text


class CausalRepository:
    def __init__(self, db):
        self.db = db

    def get_causal_bd(self):
        sql = '''
            SELECT * FROM CAUSAL;
        '''
        return self.db.engine.execute(text(sql)).fetchall()