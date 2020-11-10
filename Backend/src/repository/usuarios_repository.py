from sqlalchemy.sql import text


class UsuariosRepository:
    def __init__(self, db):
        self.db = db

    def get_usuarios_bd(self):
        sql = '''
            SELECT * FROM USUARIOS;
        '''
        return self.db.engine.execute(text(sql)).fetchall()

    def usuarios_insert_bd(self, nombre_estado):
        # sql = '''
        #     INSERT INTO public.estado(nombreestado)
        #     VALUES (:nombre_estado_sql)
        # '''
        sql = '''
            INSERT INTO public.servicio(nombre)
            VALUES (:nombre_estado_sql);
        '''
        return self.db.engine.execute(text(sql), nombre_estado_sql=nombre_estado)
