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
    
    def get_proceso_inicial_bd(self, idProceso):
        print('-------------------------------------')
        print('* PROCESO -> ', idProceso)
        print('-------------------------------------')
        sql = '''
            SELECT 
                P.IDPROCESO,
                P.RADICADOPROCESO AS EXPEDIENTE,
                S.NOMBRE AS SERVICIO,
                EMP.NOMBRE AS EMPRESA,
                U.NOMBRE || ' ' || U.APELLIDO AS USUARIO,
                E.NOMBREESTADO AS ESTADO,
                P.MONTOSANCION,
                P.FECHACADUCIDAD AS CADUCIDAD,
                EP.ETAPA AS IDETAPA,
                ET.NOMBRE AS ACTUALETAPA,
                ET.SIGUIENTEETAPA,
                (SELECT NOMBRE FROM ETAPA WHERE IDETAPA=ET.SIGUIENTEETAPA) AS PROXETAPA
            FROM
                EMPRESA EMP, SERVICIO S, PROCESO P, ESTADO E, USUARIOS U, PROCESO_CAUSAL PC, ETAPA_PROCESO EP, ETAPA ET
            WHERE
                P.ESTADO NOT IN (22)
                AND P.EMPRESA = EMP.IDEMPRESA
                AND EMP.SERVICIO = S.IDSERVICIO
                AND P.IDSERVICIO = S.IDSERVICIO
                AND P.ESTADO = E.IDESTADO
                AND P.USUARIOASIGNADO = U.IDUSUARIO
                AND P.IDPROCESO = :IDPROCESO_ARG
                AND P.IDPROCESO = PC.IDPROCESO
                AND P.IDPROCESO = EP.PROCESO
                AND EP.ETAPA = ET.IDETAPA;
        '''
        return self.db.engine.execute(text(sql), IDPROCESO_ARG=idProceso).fetchall()
    
    def get_proceso_bd(self, idProceso):
        print('-------------------------------------')
        print('* PROCESO -> ', idProceso)
        print('-------------------------------------')
        sql = '''
            SELECT 
                P.IDPROCESO,
                P.RADICADOPROCESO AS EXPEDIENTE,
                S.NOMBRE AS SERVICIO,
                EMP.NOMBRE AS EMPRESA,
                U.NOMBRE || ' ' || U.APELLIDO AS USUARIO,
                E.NOMBREESTADO AS ESTADO,
                TS.NOMBRETIPOSANCION AS TIPOSANCION,
                P.MONTOSANCION,
                DR.TIPODESCISIONRECURSO AS DECISION,
                C.NOMBRECAUSAL,
                PC.FECHAHECHOS,
                PC.DESCRIPCION,
                P.FECHACADUCIDAD AS CADUCIDAD,
                EP.ETAPA AS IDETAPA,
                ET.NOMBRE AS ACTUALETAPA,
                ET.SIGUIENTEETAPA,
                (SELECT NOMBRE FROM ETAPA WHERE IDETAPA=ET.SIGUIENTEETAPA) AS PROXETAPA
            FROM
                EMPRESA EMP, SERVICIO S, PROCESO P, ESTADO E, USUARIOS U, PROCESO_CAUSAL PC, ETAPA_PROCESO EP, ETAPA ET, CAUSAL C, TIPOSANCION TS, DESCISIONRECURSO DR
            WHERE
                P.ESTADO NOT IN (22)
                AND P.EMPRESA = EMP.IDEMPRESA
                AND EMP.SERVICIO = S.IDSERVICIO
                AND P.IDSERVICIO = S.IDSERVICIO
                AND P.ESTADO = E.IDESTADO
                AND P.USUARIOASIGNADO = U.IDUSUARIO
                AND P.IDPROCESO = :IDPROCESO_ARG
                AND P.IDPROCESO = PC.IDPROCESO
                AND P.IDPROCESO = EP.PROCESO
                AND EP.ETAPA = ET.IDETAPA
                AND PC.IDCAUSAL = C.IDCAUSAL
                AND P.TIPOSANCION = TS.IDTIPOSANCION
                AND P.DESCISIONRECURSO = DR.IDDESCISIONRECURSO;
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
    
    def proceso_usuario_update_bd(self, dataProceso):
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

    def proceso_update_bd(self, dataProceso):
        print('-------------------------------------')
        print('* PROCESO A ACTUALIZAR -> ', dataProceso)
        print('-------------------------------------')

        sql = '''
            UPDATE PROCESO
	        SET RADICADOPROCESO = :RADICADO_ARG, USUARIOASIGNADO = :USUARIO_ARG, EMPRESA = :EMPRESA_ARG, IDSERVICIO = :SERVICIO_ARG, ESTADO = :ESTADO_ARG, TIPOSANCION = :TIPOSANCION_ARG, 
            DESCISIONRECURSO = :DECISION_ARG, MONTOSANCION = :SANCION_ARG, FECHACADUCIDAD = :CADUCIDAD_ARG
	        WHERE RADICADOPROCESO = :RADICADO_ARG;
        '''
        resultsql = self.db.engine.execute(text(sql), RADICADO_ARG=dataProceso["expediente"], USUARIO_ARG=dataProceso["usuario"], EMPRESA_ARG=dataProceso["empresa"], SERVICIO_ARG=dataProceso["servicio"], ESTADO_ARG=dataProceso["estado"], TIPOSANCION_ARG=dataProceso["tipo_sancion"], DECISION_ARG=dataProceso["decision"], SANCION_ARG=dataProceso["sancion"], CADUCIDAD_ARG=dataProceso["caducidad"])

        sql = '''
            UPDATE PROCESO_CAUSAL
            SET IDCAUSAL = :CAUSAL_ARG, FECHAHECHOS = :FECHAHECHOS_ARG, DESCRIPCION = :DESCRIPCION_ARG
            WHERE IDPROCESO = :IDPROCESO_ARG;
        '''
        resultsql = self.db.engine.execute(text(sql), IDPROCESO_ARG=dataProceso["idproceso"], CAUSAL_ARG=dataProceso["causa"], FECHAHECHOS_ARG=dataProceso["fecha_hechos"], DESCRIPCION_ARG=dataProceso["descripcion"])

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
