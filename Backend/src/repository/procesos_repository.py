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
                ES.NOMBREESTADO AS ESTADO,
                S.NOMBRE AS SERVICIO,
                U.IDUSUARIO AS IDUSUARIO,
                U.NOMBRE || ' ' || U.APELLIDO AS USUARIO
            FROM
                EMPRESA EMP, SERVICIO S, PROCESO P, USUARIOS U, ETAPA_PROCESO EP, ETAPA E, ESTADO ES
            WHERE
                P.FASE NOT IN (3)
                AND P.IDPROCESO = EP.PROCESO
                AND EP.ETAPA = E.IDETAPA
                AND E.IDESTADO = ES.IDESTADO
                AND P.EMPRESA = EMP.IDEMPRESA
                AND EMP.SERVICIO = S.IDSERVICIO
                AND P.IDSERVICIO = S.IDSERVICIO
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
                P.FECHACADUCIDAD AS CADUCIDAD,
                EMP.NOMBRE AS EMPRESA,
                ES.NOMBREESTADO AS ESTADO,
                E.NOMBRE AS ACTUALETAPA,
                (SELECT NOMBRE FROM ETAPA WHERE IDETAPA=E.SIGUIENTEETAPA) AS PROXETAPA,
                S.NOMBRE AS SERVICIO,
                U.IDUSUARIO AS IDUSUARIO,
                U.NOMBRE || ' ' || U.APELLIDO AS USUARIO
            FROM
                EMPRESA EMP, SERVICIO S, PROCESO P, USUARIOS U, ETAPA_PROCESO EP, ETAPA E, ESTADO ES
            WHERE
                P.FASE NOT IN (3)
                AND P.IDPROCESO = EP.PROCESO
                AND EP.ETAPA = E.IDETAPA
                AND E.IDESTADO = ES.IDESTADO
                AND P.EMPRESA = EMP.IDEMPRESA
                AND EMP.SERVICIO = S.IDSERVICIO
                AND P.IDSERVICIO = S.IDSERVICIO
                AND P.USUARIOASIGNADO = U.IDUSUARIO
                AND P.IDPROCESO = :IDPROCESO_ARG;
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
                P.FECHACADUCIDAD AS CADUCIDAD,
                EMP.NOMBRE AS EMPRESA,
                C.NOMBRECAUSAL,
                PC.FECHAHECHOS,
                PC.DESCRIPCION,
                ES.NOMBREESTADO AS ESTADO,
                E.NOMBRE AS ACTUALETAPA,
                (SELECT NOMBRE FROM ETAPA WHERE IDETAPA=E.SIGUIENTEETAPA) AS PROXETAPA,
                DR.TIPODESCISIONRECURSO AS DECISION,
                TS.NOMBRETIPOSANCION AS TIPOSANCION,
                P.MONTOSANCION,
                S.NOMBRE AS SERVICIO,
                U.IDUSUARIO AS IDUSUARIO
            FROM
                EMPRESA EMP, SERVICIO S, PROCESO P, USUARIOS U, ETAPA_PROCESO EP, ETAPA E, ESTADO ES, PROCESO_CAUSAL PC, CAUSAL C, TIPOSANCION TS, DESCISIONRECURSO DR
            WHERE
                P.FASE NOT IN (3)
                AND P.IDPROCESO = EP.PROCESO
                AND EP.ETAPA = E.IDETAPA
                AND E.IDESTADO = ES.IDESTADO
                AND P.EMPRESA = EMP.IDEMPRESA
                AND EMP.SERVICIO = S.IDSERVICIO
                AND P.IDSERVICIO = S.IDSERVICIO
                AND P.IDPROCESO = PC.IDPROCESO
                AND PC.IDCAUSAL = C.IDCAUSAL
                AND P.USUARIOASIGNADO = U.IDUSUARIO
                AND P.TIPOSANCION = TS.IDTIPOSANCION
                AND P.DESCISIONRECURSO = DR.IDDESCISIONRECURSO
                AND P.IDPROCESO = :IDPROCESO_ARG;
        '''
        return self.db.engine.execute(text(sql), IDPROCESO_ARG=idProceso).fetchall()

    def proceso_insert_bd(self, proceso):
        print('-------------------------------------')
        print('OBJ PROCESO -> ', proceso)
        print('-------------------------------------')
        sql = '''
            INSERT INTO PROCESO(RADICADOPROCESO, USUARIOASIGNADO, EMPRESA, IDSERVICIO, FASE, FECHACADUCIDAD, FECHAREGISTRO)
            VALUES (:RADICADO_ARG, :USUARIO_ARG, :EMPRESA_ARG, :SERVICIO_ARG, :FASE_ARG, :CADUCIDAD_ARG, CURRENT_TIMESTAMP);
        '''
        resultsql = self.db.engine.execute(text(sql), RADICADO_ARG=proceso["radicado"], USUARIO_ARG=proceso["usuario"], EMPRESA_ARG=proceso["empresa"], SERVICIO_ARG=proceso["servicio"], FASE_ARG=1, CADUCIDAD_ARG=proceso["fecha_caducidad"])

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
            UPDATE 
                PROCESO
	        SET 
                RADICADOPROCESO = :RADICADO_ARG,
                USUARIOASIGNADO = :USUARIO_ARG,
                EMPRESA = :EMPRESA_ARG,
                IDSERVICIO = :SERVICIO_ARG,
                TIPOSANCION = :TIPOSANCION_ARG, 
                DESCISIONRECURSO = :DECISION_ARG,
                MONTOSANCION = :SANCION_ARG,
                FECHACADUCIDAD = :CADUCIDAD_ARG
	        WHERE
                IDPROCESO = :IDPROCESO_ARG;
        '''
        resultsql = self.db.engine.execute(text(sql), IDPROCESO_ARG=dataProceso["idproceso"], RADICADO_ARG=dataProceso["expediente"], USUARIO_ARG=dataProceso["usuario"], EMPRESA_ARG=dataProceso["empresa"], SERVICIO_ARG=dataProceso["servicio"], TIPOSANCION_ARG=dataProceso["tipo_sancion"], DECISION_ARG=dataProceso["decision"], SANCION_ARG=dataProceso["sancion"], CADUCIDAD_ARG=dataProceso["caducidad"])

        sql = '''
            UPDATE 
                PROCESO_CAUSAL
            SET
                IDCAUSAL = :CAUSAL_ARG,
                FECHAHECHOS = :FECHAHECHOS_ARG,
                DESCRIPCION = :DESCRIPCION_ARG
            WHERE
                IDPROCESO = :IDPROCESO_ARG;
        '''
        resultsql = self.db.engine.execute(text(sql), IDPROCESO_ARG=dataProceso["idproceso"], CAUSAL_ARG=dataProceso["causa"], FECHAHECHOS_ARG=dataProceso["fecha_hechos"], DESCRIPCION_ARG=dataProceso["descripcion"])

        return resultsql
    
    def proceso_delete_bd(self, idProceso):
        print('-------------------------------------')
        print('* PROCESO A ELIMINAR -> ', idProceso)
        print('-------------------------------------')
        sql = '''
            UPDATE PROCESO
            SET FASE = 3
            WHERE IDPROCESO = :IDPROCESO_ARG;
        '''
        resultsql = self.db.engine.execute(text(sql), IDPROCESO_ARG=idProceso)

        return resultsql