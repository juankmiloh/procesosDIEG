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
                U.NICKNAME,
                U.NOMBRE||' '||U.APELLIDO AS USUARIO,
                U.IDUSUARIO,
                CASE WHEN (U.GENERO = 1 AND U.ROL = 1) THEN 'Administrador'
                ELSE CASE WHEN (U.GENERO = 2 AND U.ROL = 1) THEN 'Administradora'
                ELSE CASE WHEN (U.GENERO = 1 AND U.ROL = 2) THEN 'Abogado'
                ELSE CASE WHEN (U.GENERO = 2 AND U.ROL = 2) THEN 'Abogada'
                ELSE 'Consulta' END END END END AS PRIVILEGIO,
                U.AVATAR
            FROM USUARIOS U, ROL R
            WHERE 
                U.ROL = R.IDROL
                AND TOKEN = :TOKEN_ARG;
        '''
        return self.db.engine.execute(text(sql), TOKEN_ARG=token).fetchall()

    def get_usuarios_bd(self):
        sql = '''
            SELECT * FROM USUARIOS WHERE ROL <> 3 ORDER BY NOMBRE ASC;
        '''
        return self.db.engine.execute(text(sql)).fetchall()

    def get_lista_usuarios_bd(self):
        sql = '''
            SELECT
                CASE WHEN (U.GENERO = 1 AND U.ROL = 1) THEN 'Administrador'
                ELSE CASE WHEN (U.GENERO = 2 AND U.ROL = 1) THEN 'Administradora'
                ELSE CASE WHEN (U.GENERO = 1 AND U.ROL = 2) THEN 'Abogado'
                ELSE CASE WHEN (U.GENERO = 2 AND U.ROL = 2) THEN 'Abogada'
                ELSE 'Consulta' END END END END AS PRIVILEGIO,
                U.*,
                G.NOMBRE
            FROM USUARIOS U, ROL R, GENERO G
            WHERE 
                U.ROL = R.IDROL
                AND U.GENERO = G.IDGENERO
            ORDER BY U.NOMBRE ASC;
        '''
        return self.db.engine.execute(text(sql)).fetchall()
    
    def get_rol_bd(self):
        sql = '''
            SELECT * FROM ROL;
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
    
    def usuarios_create_bd(self, usuario):
        sql = '''
            INSERT INTO USUARIOS
            (NOMBRE, APELLIDO, GENERO, NICKNAME, DESCRIPCION, ROL, AVATAR, CONTRASENA, TOKEN) 
            VALUES (:NOMBRE_ARG, :APELLIDO_ARG, :GENERO_ARG, :NICKNAME_ARG, :DESCRIPCION_ARG, :ROL_ARG, :AVATAR_ARG, :CONTRASENA_ARG, :TOKEN_ARG);
        '''
        return self.db.engine.execute(text(sql), NOMBRE_ARG=usuario['nombre'], APELLIDO_ARG=usuario['apellido'], GENERO_ARG=usuario['genero'], NICKNAME_ARG=usuario['nickname'], DESCRIPCION_ARG=usuario['descripcion'], ROL_ARG=usuario['rol'], AVATAR_ARG=usuario['avatar'], CONTRASENA_ARG=usuario['contrasena'], TOKEN_ARG=usuario['token'])
    
    def usuario_update_bd(self, usuario):
        print('-------------------------------------')
        print('* USUARIO A ACTUALIZAR -> ', usuario['contrasena'])
        print('-------------------------------------')
        if usuario['contrasena'] != '':    
            sql = '''
                UPDATE USUARIOS SET
                    NOMBRE = :NOMBRE_ARG,
                    APELLIDO = :APELLIDO_ARG,
                    GENERO = :GENERO_ARG,
                    NICKNAME = :NICKNAME_ARG,
                    DESCRIPCION = :DESCRIPCION_ARG,
                    ROL = :ROL_ARG,
                    AVATAR = :AVATAR_ARG,
                    CONTRASENA = :CONTRASENA_ARG,
                    TOKEN = :TOKEN_ARG
                WHERE IDUSUARIO = :IDUSUARIO_ARG;
            '''
        else:
            sql = '''
                UPDATE USUARIOS SET
                    NOMBRE = :NOMBRE_ARG,
                    APELLIDO = :APELLIDO_ARG,
                    GENERO = :GENERO_ARG,
                    NICKNAME = :NICKNAME_ARG,
                    DESCRIPCION = :DESCRIPCION_ARG,
                    ROL = :ROL_ARG,
                    AVATAR = :AVATAR_ARG,
                    TOKEN = :TOKEN_ARG
                WHERE IDUSUARIO = :IDUSUARIO_ARG;
            '''
            
        return self.db.engine.execute(text(sql), IDUSUARIO_ARG=usuario['idusuario'], NOMBRE_ARG=usuario['nombre'], APELLIDO_ARG=usuario['apellido'], GENERO_ARG=usuario['genero'], NICKNAME_ARG=usuario['nickname'], DESCRIPCION_ARG=usuario['descripcion'], ROL_ARG=usuario['rol'], AVATAR_ARG=usuario['avatar'], CONTRASENA_ARG=usuario['contrasena'], TOKEN_ARG=usuario['token'])

    def usuario_delete_bd(self, idusuario):
        print('-------------------------------------')
        print('* USUARIO A ELIMINAR -> ', idusuario)
        print('-------------------------------------')
        sql = '''
            DELETE FROM USUARIOS
	        WHERE IDUSUARIO = :IDUSUARIO_ARG;
        '''
        resultsql = self.db.engine.execute(text(sql), IDUSUARIO_ARG=idusuario)

        return resultsql
