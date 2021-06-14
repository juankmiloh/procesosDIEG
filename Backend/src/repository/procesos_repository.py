from sqlalchemy.sql import text


class ProcesosRepository:
    def __init__(self, db):
        self.db = db

    def get_procesos_bd(self, iddependencia):
        sql = '''
            SELECT * FROM
            (
                SELECT 
                    P.IDPROCESO,
                    P.RADICADOPROCESO AS EXPEDIENTE,
                    P.FECHACADUCIDAD AS CADUCIDAD,
                    EMP.NOMBRE AS EMPRESA,
                    ES.NOMBREESTADO AS ESTADO,
                    S.NOMBRE AS SERVICIO,
                    U.IDUSUARIO AS IDUSUARIO,
                    U.NOMBRE || ' ' || U.APELLIDO AS USUARIO,
                    R.IDUSUARIO AS IDREVISOR,
                    R.NOMBRE || ' ' || R.APELLIDO AS REVISOR,
                    EP.ETAPA
                FROM
                    EMPRESA EMP, SERVICIO S, PROCESO P, USUARIOS U, ETAPA_PROCESO EP, ETAPA E, ESTADO ES, USUARIOS R
                WHERE
                    (U.DEPENDENCIA = :DEPENDENCIA_ARG OR 1 = :DEPENDENCIA_ARG)
                    AND P.FASE NOT IN (3)
                    AND P.IDPROCESO = EP.PROCESO
                    AND EP.ETAPA = E.IDETAPA
                    AND E.IDESTADO = ES.IDESTADO
                    AND P.EMPRESA = EMP.IDEMPRESA
                    AND EMP.SERVICIO = S.IDSERVICIO
                    AND P.IDSERVICIO = S.IDSERVICIO
                    AND P.USUARIOASIGNADO = U.IDUSUARIO
                    AND P.REVISOR = R.IDUSUARIO
            ) PROCESO,
            (
                SELECT 
                    P.IDPROCESO,
                    MIN(EP.ETAPA) AS IDETAPA
                FROM PROCESO P, ETAPA_PROCESO EP
                WHERE
                    P.IDPROCESO = EP.PROCESO
                GROUP BY P.IDPROCESO
            ) ETAPA
            WHERE
                PROCESO.IDPROCESO = ETAPA.IDPROCESO
                AND PROCESO.ETAPA = ETAPA.IDETAPA
            ORDER BY PROCESO.CADUCIDAD ASC;
        '''
        return self.db.engine.execute(text(sql), DEPENDENCIA_ARG=iddependencia).fetchall()
    
    def get_proceso_inicial_bd(self, idProceso):
        print('-------------------------------------')
        print('* PROCESO -> ', idProceso)
        print('-------------------------------------')
        sql = '''
            SELECT * FROM
            (
                SELECT 
                    P.IDPROCESO,
                    P.RADICADOPROCESO AS EXPEDIENTE,
                    S.IDSERVICIO AS SERVICIO,
                    EMP.IDEMPRESA AS EMPRESA,
                    U.IDUSUARIO AS IDUSUARIO,
                    ES.IDESTADO AS ESTADO,
                    P.FECHACADUCIDAD AS CADUCIDAD,
                    E.NOMBRE AS ACTUALETAPA,
                    (SELECT NOMBRE FROM ETAPA WHERE IDETAPA=E.SIGUIENTEETAPA) AS PROXETAPA,
                    U.NOMBRE || ' ' || U.APELLIDO AS USUARIO,
                    R.IDUSUARIO AS IDREVISOR,
                    R.NOMBRE || ' ' || R.APELLIDO AS REVISOR,
                    EP.ETAPA
                FROM
                    EMPRESA EMP, SERVICIO S, PROCESO P, USUARIOS U, ETAPA_PROCESO EP, ETAPA E, ESTADO ES, USUARIOS R
                WHERE
                    P.IDPROCESO = EP.PROCESO
                    AND EP.ETAPA = E.IDETAPA
                    AND E.IDESTADO = ES.IDESTADO
                    AND P.EMPRESA = EMP.IDEMPRESA
                    AND EMP.SERVICIO = S.IDSERVICIO
                    AND P.IDSERVICIO = S.IDSERVICIO
                    AND P.USUARIOASIGNADO = U.IDUSUARIO
                    AND P.IDPROCESO = :IDPROCESO_ARG
                    AND P.REVISOR = R.IDUSUARIO
            ) PROCESO,
            (
                SELECT 
                    P.IDPROCESO,
                    MIN(EP.ETAPA) AS IDETAPA
                FROM PROCESO P, ETAPA_PROCESO EP
                WHERE
                    P.IDPROCESO = EP.PROCESO
                    AND P.IDPROCESO = :IDPROCESO_ARG
                GROUP BY P.IDPROCESO
            ) ETAPA
            WHERE
                PROCESO.IDPROCESO = ETAPA.IDPROCESO
                AND PROCESO.ETAPA = ETAPA.IDETAPA;
        '''
        return self.db.engine.execute(text(sql), IDPROCESO_ARG=idProceso).fetchall()
    
    def get_proceso_bd(self, idProceso):
        print('-------------------------------------')
        print('* PROCESO -> ', idProceso)
        print('-------------------------------------')
        sql = '''
            SELECT * FROM
            (
                SELECT 
                    P.IDPROCESO,
                    P.RADICADOPROCESO AS EXPEDIENTE,
                    S.IDSERVICIO AS SERVICIO,
                    EMP.IDEMPRESA AS EMPRESA,
                    U.IDUSUARIO AS IDUSUARIO,
                    ES.IDESTADO AS ESTADO,
                    TS.IDTIPOSANCION AS TIPOSANCION,
                    P.MONTOSANCION,
                    DR.IDDESCISIONRECURSO AS DECISION,
                    P.FECHACADUCIDAD AS CADUCIDAD,
                    E.NOMBRE AS ACTUALETAPA,
                    (SELECT NOMBRE FROM ETAPA WHERE IDETAPA=E.SIGUIENTEETAPA) AS PROXETAPA,
                    EP.ETAPA,
                    R.IDUSUARIO AS IDREVISOR
                FROM
                    EMPRESA EMP, SERVICIO S, PROCESO P, USUARIOS U, ETAPA_PROCESO EP, ETAPA E, ESTADO ES, TIPOSANCION TS, DESCISIONRECURSO DR, USUARIOS R
                WHERE
                    P.IDPROCESO = EP.PROCESO
                    AND EP.ETAPA = E.IDETAPA
                    AND E.IDESTADO = ES.IDESTADO
                    AND P.EMPRESA = EMP.IDEMPRESA
                    AND EMP.SERVICIO = S.IDSERVICIO
                    AND P.IDSERVICIO = S.IDSERVICIO
                    AND P.USUARIOASIGNADO = U.IDUSUARIO
                    AND P.TIPOSANCION = TS.IDTIPOSANCION
                    AND P.DESCISIONRECURSO = DR.IDDESCISIONRECURSO
                    AND P.IDPROCESO = :IDPROCESO_ARG
                    AND P.REVISOR = R.IDUSUARIO
            ) PROCESO,
            (
                SELECT 
                    P.IDPROCESO,
                    MIN(EP.ETAPA) AS IDETAPA
                FROM PROCESO P, ETAPA_PROCESO EP
                WHERE
                    P.IDPROCESO = EP.PROCESO
                    AND P.IDPROCESO = :IDPROCESO_ARG
                GROUP BY P.IDPROCESO
            ) ETAPA
            WHERE
                PROCESO.IDPROCESO = ETAPA.IDPROCESO
                AND PROCESO.ETAPA = ETAPA.IDETAPA;
        '''
        return self.db.engine.execute(text(sql), IDPROCESO_ARG=idProceso).fetchall()

    def proceso_insert_bd(self, proceso):
        print('-------------------------------------')
        print('OBJ PROCESO -> ', proceso)
        print('-------------------------------------')
        sql = '''
            INSERT INTO PROCESO(RADICADOPROCESO, USUARIOASIGNADO, REVISOR, EMPRESA, IDSERVICIO, FASE, DEPENDENCIA, FECHACADUCIDAD, FECHAREGISTRO)
            VALUES (:RADICADO_ARG, :USUARIO_ARG, :REVISOR_ARG, :EMPRESA_ARG, :SERVICIO_ARG, :FASE_ARG, :DEPENDENCIA_ARG, :CADUCIDAD_ARG, CURRENT_TIMESTAMP);
        '''
        resultsql = self.db.engine.execute(text(sql), RADICADO_ARG=proceso["radicado"], USUARIO_ARG=proceso["usuario"], REVISOR_ARG=proceso["revisor"], EMPRESA_ARG=proceso["empresa"], SERVICIO_ARG=proceso["servicio"], FASE_ARG=1, DEPENDENCIA_ARG=proceso["dependencia"], CADUCIDAD_ARG=proceso["fecha_caducidad"])

        return resultsql
    
    def proceso_usuario_update_bd(self, dataProceso):
        print('-------------------------------------')
        print('* PROCESO A ACTUALIZAR -> ', dataProceso)
        print('-------------------------------------')
        sql = '''
            UPDATE PROCESO
            SET
                USUARIOASIGNADO = :IDUSUARIO_ARG,
                REVISOR = :REVISOR_ARG
            WHERE IDPROCESO = :IDPROCESO_ARG;
        '''
        resultsql = self.db.engine.execute(text(sql), IDPROCESO_ARG=dataProceso["idproceso"], IDUSUARIO_ARG=dataProceso["usuario"], REVISOR_ARG=dataProceso["revisor"])

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
                REVISOR = :REVISOR_ARG,
                EMPRESA = :EMPRESA_ARG,
                IDSERVICIO = :SERVICIO_ARG,
                TIPOSANCION = :TIPOSANCION_ARG, 
                DESCISIONRECURSO = :DECISION_ARG,
                MONTOSANCION = :SANCION_ARG,
                FECHACADUCIDAD = :CADUCIDAD_ARG
	        WHERE
                IDPROCESO = :IDPROCESO_ARG;
        '''
        self.db.engine.execute(text(sql), IDPROCESO_ARG=dataProceso["idproceso"], RADICADO_ARG=dataProceso["expediente"], USUARIO_ARG=dataProceso["usuario"], REVISOR_ARG=dataProceso["revisor"], EMPRESA_ARG=dataProceso["empresa"], SERVICIO_ARG=dataProceso["servicio"], TIPOSANCION_ARG=dataProceso["tipo_sancion"], DECISION_ARG=dataProceso["decision"], SANCION_ARG=dataProceso["sancion"], CADUCIDAD_ARG=dataProceso["caducidad"])
    
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