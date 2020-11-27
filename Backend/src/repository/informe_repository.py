from sqlalchemy.sql import text


class InformeRepository:
    def __init__(self, db):
        self.db = db

    def get_cantidad_procesos_bd(self):
        sql = '''
            SELECT COUNT(*), F.NOMBRE FROM PROCESO P, FASE F WHERE P.FASE = F.IDFASE GROUP BY F.NOMBRE ORDER BY F.NOMBRE ASC;
        '''
        return self.db.engine.execute(text(sql)).fetchall()
    
    def get_procesos_empresa_bd(self, fase):
        sql = '''
            SELECT COUNT(*), EMP.NOMBRE FROM PROCESO P, EMPRESA EMP
            WHERE 
                P.FASE = :FASE_ARG
                AND P.EMPRESA = EMP.IDEMPRESA
            GROUP BY EMP.NOMBRE;
        '''
        return self.db.engine.execute(text(sql), FASE_ARG=fase).fetchall()
    
    def get_procesos_causal_bd(self, fase):
        sql = '''
            SELECT COUNT(*), C.NOMBRECAUSAL FROM PROCESO P, PROCESO_CAUSAL PC, CAUSAL C
            WHERE 
                P.FASE = :FASE_ARG
                AND P.IDPROCESO = PC.IDPROCESO
                AND PC.IDCAUSAL = C.IDCAUSAL
            GROUP BY 
                PC.IDCAUSAL,
                C.NOMBRECAUSAL;
        '''
        return self.db.engine.execute(text(sql), FASE_ARG=fase).fetchall()
    
    def get_procesos_estado_bd(self, fase):
        sql = '''
            SELECT COUNT(*), ESTADO FROM
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
                    EP.ETAPA
                FROM
                    EMPRESA EMP, SERVICIO S, PROCESO P, USUARIOS U, ETAPA_PROCESO EP, ETAPA E, ESTADO ES
                WHERE
                    P.FASE = :FASE_ARG
                    AND P.IDPROCESO = EP.PROCESO
                    AND EP.ETAPA = E.IDETAPA
                    AND E.IDESTADO = ES.IDESTADO
                    AND P.EMPRESA = EMP.IDEMPRESA
                    AND EMP.SERVICIO = S.IDSERVICIO
                    AND P.IDSERVICIO = S.IDSERVICIO
                    AND P.USUARIOASIGNADO = U.IDUSUARIO
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
            GROUP BY ESTADO;
        '''
        return self.db.engine.execute(text(sql), FASE_ARG=fase).fetchall()