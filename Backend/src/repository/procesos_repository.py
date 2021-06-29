from sqlalchemy.sql import text


class ProcesosRepository:
    def __init__(self, db):
        self.db = db

    def get_procesos_bd(self, iddependencia):
        sql = '''
            SELECT PROCESO.*, ESTADO.NOMBREESTADO FROM 
            (
                SELECT 
                    IDPROCESO, EXPEDIENTE, CADUCIDAD, EMPRESA, SERVICIO, IDUSUARIO, USUARIO, IDREVISOR, REVISOR, MAX(IDESTADO) AS IDESTADO
                FROM
                (
                    SELECT 
                        PROCESO.IDPROCESO,
                        PROCESO.RADICADOPROCESO AS EXPEDIENTE,
                        PROCESO.FECHACADUCIDAD AS CADUCIDAD,
                        EMPRESA.NOMBRE AS EMPRESA,
                        ESTADO.IDESTADO,
                        SERVICIO.NOMBRE AS SERVICIO,
                        PROCESO.USUARIOASIGNADO AS IDUSUARIO,
                        PROYECTISTA.NOMBRE || ' ' || PROYECTISTA.APELLIDO AS USUARIO,
                        PROCESO.REVISOR AS IDREVISOR,
                        REVISOR.NOMBRE || ' ' || REVISOR.APELLIDO AS REVISOR
                    FROM
                        PROCESO,
                        EMPRESA,
                        ETAPA_PROCESO ETAPA,
                        ESTADO,
                        SERVICIO,
                        USUARIOS PROYECTISTA,
                        USUARIOS REVISOR
                    WHERE
                        (PROCESO.DEPENDENCIA = :DEPENDENCIA_ARG OR 1 = :DEPENDENCIA_ARG)
                        AND PROCESO.FASE NOT IN (3)
                        AND PROCESO.IDSERVICIO = EMPRESA.SERVICIO
                        AND PROCESO.EMPRESA = EMPRESA.IDEMPRESA
                        AND PROCESO.IDPROCESO = ETAPA.IDPROCESO
                        AND ETAPA.IDESTADO = ESTADO.IDESTADO
                        AND PROCESO.IDSERVICIO = SERVICIO.IDSERVICIO
                        AND PROCESO.USUARIOASIGNADO = PROYECTISTA.IDUSUARIO
                        AND PROCESO.REVISOR = REVISOR.IDUSUARIO
                ) LISTA_PROCESOS
                GROUP BY IDPROCESO, EXPEDIENTE, CADUCIDAD, EMPRESA, SERVICIO, IDUSUARIO, USUARIO, IDREVISOR, REVISOR
            ) PROCESO,
            (
                SELECT * FROM ESTADO
            ) ESTADO
            WHERE PROCESO.IDESTADO = ESTADO.IDESTADO;
        '''
        return self.db.engine.execute(text(sql), DEPENDENCIA_ARG=iddependencia).fetchall()
        
    def get_proceso_bd(self, idProceso):
        print('-------------------------------------')
        print('* PROCESO -> ', idProceso)
        print('-------------------------------------')
        sql = '''
            SELECT PROCESO.*, ESTADOS.NOMBREESTADO AS PROXESTADO FROM 
            (
                SELECT 
                    IDPROCESO, EXPEDIENTE, SERVICIO, EMPRESA, IDUSUARIO, IDSANCION, MONTOSANCION, DECISION, CADUCIDAD, IDREVISOR, MAX(IDESTADO) AS IDESTADO
                FROM
                (
                    SELECT 
                        PROCESO.IDPROCESO,
                        PROCESO.RADICADOPROCESO AS EXPEDIENTE,
                        PROCESO.FECHACADUCIDAD AS CADUCIDAD,
                        EMPRESA.IDEMPRESA AS EMPRESA,
                        ESTADO.IDESTADO,
                        PROCESO.TIPOSANCION IDSANCION,
                        PROCESO.MONTOSANCION,
                        SERVICIO.IDSERVICIO AS SERVICIO,
                        PROCESO.DESCISIONRECURSO AS DECISION,
                        PROCESO.USUARIOASIGNADO AS IDUSUARIO,
                        PROCESO.REVISOR AS IDREVISOR
                    FROM
                        PROCESO,
                        EMPRESA,
                        ETAPA_PROCESO ETAPA,
                        ESTADO,
                        SERVICIO,
                        USUARIOS PROYECTISTA,
                        USUARIOS REVISOR
                    WHERE
                        PROCESO.IDPROCESO = :IDPROCESO_ARG
                        AND PROCESO.IDSERVICIO = EMPRESA.SERVICIO
                        AND PROCESO.EMPRESA = EMPRESA.IDEMPRESA
                        AND PROCESO.IDPROCESO = ETAPA.IDPROCESO
                        AND ETAPA.IDESTADO = ESTADO.IDESTADO
                        AND PROCESO.IDSERVICIO = SERVICIO.IDSERVICIO
                        AND PROCESO.USUARIOASIGNADO = PROYECTISTA.IDUSUARIO
                        AND PROCESO.REVISOR = REVISOR.IDUSUARIO
                ) LISTA_PROCESOS
                GROUP BY IDPROCESO, EXPEDIENTE, SERVICIO, EMPRESA, IDUSUARIO, IDSANCION, MONTOSANCION, DECISION, CADUCIDAD, IDREVISOR
            ) PROCESO,
            (SELECT * FROM ESTADO) ESTADO,
            (SELECT * FROM ESTADO) ESTADOS
            WHERE PROCESO.IDESTADO = ESTADO.IDESTADO
            AND ESTADO.SIGUIENTEESTADO = ESTADOS.IDESTADO;
        '''
        return self.db.engine.execute(text(sql), IDPROCESO_ARG=idProceso).fetchall()

    def proceso_insert_bd(self, proceso):
        if "fecha_caducidad" not in proceso:
            proceso["fecha_caducidad"] = None

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