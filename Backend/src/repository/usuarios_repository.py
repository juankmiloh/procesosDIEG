from sqlalchemy.sql import text


class UsuariosRepository:
    def __init__(self, db):
        self.db = db

    def autenticar_usuario(self, usuario):
        print('LOGIN USUARIO - >', usuario)
        sql = '''
            SELECT TOKEN FROM USUARIOS
            WHERE 
                NICKNAME = :USER_ARG
            AND CONTRASENA = :PASS_ARG;
        '''
        return self.db.engine.execute(text(sql), USER_ARG=usuario["username"].lower(), PASS_ARG=usuario["password"]).fetchall()

    def getData_usuario(self, token):
        print('TOKEN USUARIO -> ', token)
        sql = '''
            SELECT 
                R.DESCRIPCION,
                U.DESCRIPCION,
                U.AVATAR,
                U.NICKNAME,
                U.NOMBRE AS USUARIO
            FROM USUARIOS U, ROL R
            WHERE 
                U.ROL = R.IDROL
                AND TOKEN = :TOKEN_ARG;
        '''
        return self.db.engine.execute(text(sql), TOKEN_ARG=token).fetchall()

    def get_usuarios_bd(self):
        sql = '''
            SELECT * FROM USUARIOS;
        '''
        return self.db.engine.execute(text(sql)).fetchall()
    
    def get_nicknames_bd(self):
        sql = '''
            SELECT NOMBRE, APELLIDO, NICKNAME FROM USUARIOS;
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
