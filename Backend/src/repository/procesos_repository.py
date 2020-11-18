from sqlalchemy.sql import text


class ProcesosRepository:
    def __init__(self, db):
        self.db = db

    def get_procesos_bd(self):
        sql = '''
            SELECT 
                P.IDPROCESO,
                P.RADICADOPROCESO AS EXPEDIENTE,
                P.FECHACADUCIDAD AS CADUCIDAD,
                EMP.NOMBRE AS EMPRESA,
                E.NOMBREESTADO AS ESTADO,
                S.NOMBRE AS SERVICIO,
                U.IDUSUARIO AS IDUSUARIO,
                U.NOMBRE || ' ' || U.APELLIDO AS USUARIO
            FROM
                EMPRESA EMP, SERVICIO S, PROCESO P, ESTADO E, USUARIOS U
            WHERE
                P.ESTADO NOT IN (22)
                AND P.EMPRESA = EMP.IDEMPRESA
                AND EMP.SERVICIO = S.IDSERVICIO
                AND P.IDSERVICIO = S.IDSERVICIO
                AND P.ESTADO = E.IDESTADO
                AND P.USUARIOASIGNADO = U.IDUSUARIO
            ORDER BY P.FECHACADUCIDAD ASC;
        '''
        return self.db.engine.execute(text(sql)).fetchall()
    
    def get_proceso_bd(self, idProceso):
        print('-------------------------------------')
        print('* PROCESO -> ', idProceso)
        print('-------------------------------------')
        sql = '''
            SELECT 
                P.IDPROCESO,
                P.RADICADOPROCESO AS EXPEDIENTE,
                P.FECHACADUCIDAD AS CADUCIDAD,
                EMP.NOMBRE AS EMPRESA,
                E.NOMBREESTADO AS ESTADO,
                S.NOMBRE AS SERVICIO,
                U.IDUSUARIO AS IDUSUARIO,
                U.NOMBRE || ' ' || U.APELLIDO AS USUARIO
            FROM
                EMPRESA EMP, SERVICIO S, PROCESO P, ESTADO E, USUARIOS U
            WHERE
                P.ESTADO NOT IN (22)
                AND P.EMPRESA = EMP.IDEMPRESA
                AND EMP.SERVICIO = S.IDSERVICIO
                AND P.IDSERVICIO = S.IDSERVICIO
                AND P.ESTADO = E.IDESTADO
                AND P.USUARIOASIGNADO = U.IDUSUARIO
                AND P.IDPROCESO = :IDPROCESO_ARG;
        '''
        return self.db.engine.execute(text(sql), IDPROCESO_ARG=idProceso).fetchall()

    def proceso_insert_bd(self, proceso):
        print('-------------------------------------')
        print('OBJ PROCESO -> ', proceso)
        print('-------------------------------------')
        sql = '''
            INSERT INTO PROCESO(RADICADOPROCESO, USUARIOASIGNADO, EMPRESA, IDSERVICIO, ESTADO, FECHACADUCIDAD, FECHAREGISTRO)
            VALUES (:RADICADO_ARG, :USUARIO_ARG, :EMPRESA_ARG, :SERVICIO_ARG, :ESTADO_ARG, :CADUCIDAD_ARG, CURRENT_TIMESTAMP);
        '''
        resultsql = self.db.engine.execute(text(sql), RADICADO_ARG=proceso["radicado"], USUARIO_ARG=proceso["usuario"], EMPRESA_ARG=proceso["empresa"], SERVICIO_ARG=proceso["servicio"], ESTADO_ARG=14, CADUCIDAD_ARG=proceso["fecha_caducidad"])

        return resultsql
    
    def proceso_update_bd(self, dataProceso):
        print('-------------------------------------')
        print('* PROCESO A ACTUALIZAR -> ', dataProceso)
        print('-------------------------------------')
        sql = '''
            UPDATE PROCESO
            SET USUARIOASIGNADO = :IDUSUARIO_ARG
            WHERE RADICADOPROCESO = :RADICADO_ARG;
        '''
        resultsql = self.db.engine.execute(text(sql), RADICADO_ARG=dataProceso["expediente"], IDUSUARIO_ARG=dataProceso["usuario"])

        return resultsql
    
    def proceso_delete_bd(self, idProceso):
        print('-------------------------------------')
        print('* PROCESO A ELIMINAR -> ', idProceso)
        print('-------------------------------------')
        sql = '''
            UPDATE PROCESO
            SET ESTADO = 22
            WHERE IDPROCESO = :IDPROCESO_ARG;
        '''
        resultsql = self.db.engine.execute(text(sql), IDPROCESO_ARG=idProceso)

        return resultsql
