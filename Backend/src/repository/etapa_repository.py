from itertools import count
from sqlalchemy.sql import text
from sqlalchemy.sql.elements import Null


class EtapaRepository:
    def __init__(self, db):
        self.db = db

    def get_etapa_bd(self):
        sql = '''
            SELECT * FROM ESTADO ORDER BY IDESTADO ASC;
        '''
        return self.db.engine.execute(text(sql)).fetchall()
    
    def get_etapa_proceso_bd(self, idProceso, idEtapa):
        sql = '''
            SELECT
                ETAPA.IDESTADO,
                ETAPA.NUMEROACTO,
                ETAPA.RADICADO,
                ETAPA.FECHAINICIO,
                ETAPA.FECHAFIN,
                ETAPA.OBSERVACION,
                ESTADO.NOMBREESTADO,
                ESTADO.OBLIGATORIEDAD,
                ESTADO.FECHA_FINAL,
                ESTADO.VARIOS_ACTOS,
                ESTADO.OBSERVACION,
                ESTADO.SIGUIENTEESTADO
            FROM ETAPA_PROCESO ETAPA, ESTADO
            WHERE IDPROCESO = :IDPROCESO_ARG
            AND (ETAPA.IDESTADO = :IDESTADO_ARG OR 0 = :IDESTADO_ARG)
            AND ETAPA.IDESTADO = ESTADO.IDESTADO
            ORDER BY 1, 2;
        '''
        return self.db.engine.execute(text(sql), IDPROCESO_ARG=idProceso, IDESTADO_ARG=idEtapa).fetchall()

    def etapa_insert_bd(self, etapa):
        print('-------------------------------------')
        print('OBJ ETAPA -> ', etapa)
        print('-------------------------------------')
        if "fechaInicio" not in etapa:
            etapa["fechaInicio"] = None
        if "fechaFin" not in etapa:
            etapa["fechaFin"] = None
        if "observacion" not in etapa:
            etapa["observacion"] = None

        sql = '''
            INSERT INTO ETAPA_PROCESO(IDPROCESO, IDESTADO, NUMEROACTO, RADICADO, FECHAINICIO, FECHAFIN, OBSERVACION, FECHAREGISTRO)
            VALUES (:IDPROCESO_ARG, :IDESTADO_ARG, :NUMEROACTO_ARG, :RADICADO_ARG, :FECHAINICIO_ARG, :FECHAFIN_ARG, :OBSERVACION_ARG, CURRENT_TIMESTAMP);
        '''
        self.db.engine.execute(text(sql), IDPROCESO_ARG=etapa["idproceso"], IDESTADO_ARG=etapa["etapa"], NUMEROACTO_ARG=etapa["numeroacto"], RADICADO_ARG=etapa["radicado"], FECHAINICIO_ARG=etapa["fechaInicio"], FECHAFIN_ARG=etapa["fechaFin"], OBSERVACION_ARG=etapa["observacion"])

        # self.update_fase_proceso(etapa["idproceso"])

    def etapa_update_bd(self, etapa):
        print('-------------------------------------')
        print('* ETAPA A ACTUALIZAR -> ', etapa)
        print('-------------------------------------')

        if etapa["fechaFin"] == 'No registra':
            etapa["fechaFin"] = None

        sql = '''
            UPDATE 
                ETAPA_PROCESO
	        SET 
                RADICADO = :RADICADO_ARG,
                FECHAINICIO = :FECHAINICIO_ARG,
                FECHAFIN = :FECHAFIN_ARG,
                OBSERVACION = :OBSERVACION_ARG
	        WHERE 
                IDPROCESO = :IDPROCESO_ARG
                AND IDESTADO = :IDESTADO_ARG;
        '''
        self.db.engine.execute(text(sql), IDPROCESO_ARG=etapa["idproceso"], IDESTADO_ARG=etapa["etapa"], FECHAINICIO_ARG=etapa["fechaInicio"], FECHAFIN_ARG=etapa["fechaFin"], RADICADO_ARG=etapa["radicado"], OBSERVACION_ARG=etapa["observacion"])

        # self.update_fase_proceso(etapa["idproceso"])
            
                        
    def etapa_delete_bd(self, etapa):
        print('-------------------------------------')
        print('* ETAPA A ELIMINAR -> ', etapa)
        print('-------------------------------------')
        sql = '''
            DELETE FROM
                ETAPA_PROCESO
            WHERE
                IDPROCESO = :IDPROCESO_ARG
                AND IDESTADO = :IDESTADO_ARG;
        '''
        self.db.engine.execute(text(sql), IDPROCESO_ARG=etapa["idproceso"], IDESTADO_ARG=etapa["idetapa"])

        # self.update_fase_proceso(etapa["idproceso"])
    
    def acto_delete_bd(self, acto):
        print('-------------------------------------')
        print('* ACTO A ELIMINAR -> ', acto)
        print('-------------------------------------')
        sql = '''
            DELETE FROM
                ETAPA_PROCESO
            WHERE
                IDPROCESO = :IDPROCESO_ARG
                AND IDESTADO = :IDESTADO_ARG
                AND NUMEROACTO = :ACTO_ARG;
        '''
        self.db.engine.execute(text(sql), IDPROCESO_ARG=acto["idproceso"], IDESTADO_ARG=acto["etapa"], ACTO_ARG=acto["numeroacto"])

    def update_fase_proceso(self, idproceso):
        sql = '''
            SELECT E.NOMBRE FROM ETAPA_PROCESO EP, ETAPA E WHERE PROCESO=:IDPROCESO_ARG AND EP.ETAPA=E.IDETAPA;
        '''
        resultsql = self.db.engine.execute(text(sql), IDPROCESO_ARG=idproceso).fetchall()

        countEtapas = 0
        terminado = False
        fase = 0
        
        for result in resultsql:
            etapa = result[0]
            if etapa != 'Memorando de devolución':
                if etapa != 'Memorando de alcance':
                    print('------------ ETAPA ----', etapa, '----------------')
                    countEtapas = countEtapas + 1
                    if etapa == 'Archivo':
                        terminado = True

        print('------------ CANTIDAD ETAPAS ----', countEtapas, '----------------')
        print('------------ TERMINADO ----', terminado, '----------------')

        if countEtapas >= 13 and terminado:
            print('------------ PROCESO TERMINADO ----------------')
            fase = 2 # Proceso terminado
        else:
            fase = 1 # Proceso En curso

        sql = '''
                UPDATE PROCESO SET FASE=:FASE_ARG WHERE IDPROCESO=:IDPROCESO_ARG;
            '''
        self.db.engine.execute(text(sql), IDPROCESO_ARG=idproceso, FASE_ARG=fase)