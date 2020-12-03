from itertools import count
from sqlalchemy.sql import text
from sqlalchemy.sql.elements import Null


class EtapaRepository:
    def __init__(self, db):
        self.db = db

    def get_etapa_bd(self):
        sql = '''
            SELECT * FROM ETAPA ORDER BY IDETAPA DESC;
        '''
        return self.db.engine.execute(text(sql)).fetchall()
    
    def get_etapa_proceso_bd(self, idProceso):
        sql = '''
            SELECT 
                EP.ETAPA,
                EP.RADICADOETAPA,
                E.NOMBRE,
                EP.FECHAINICIOETAPA,
                EP.FECHAFINETAPA,
                EP.OBSERVACIONETAPA 
            FROM ETAPA_PROCESO EP, ETAPA E
            WHERE
                EP.ETAPA = E.IDETAPA
                AND PROCESO = :IDPROCESO_ARG
            ORDER BY EP.ETAPA;
        '''
        return self.db.engine.execute(text(sql), IDPROCESO_ARG=idProceso).fetchall()

    def etapa_insert_bd(self, etapa):
        print('-------------------------------------')
        print('OBJ ETAPA -> ', etapa)
        print('-------------------------------------')
        sql = '''
            INSERT INTO ETAPA_PROCESO(ETAPA, PROCESO, FECHAINICIOETAPA, FECHAFINETAPA, RADICADOETAPA, OBSERVACIONETAPA)
            VALUES (:ETAPA_ARG, :IDPROCESO_ARG, :FECHAINICIO_ARG, :FECHAFIN_ARG, :RADICADO_ARG, :OBSERVACION_ARG);
        '''
        self.db.engine.execute(text(sql), ETAPA_ARG=etapa["etapa"], IDPROCESO_ARG=etapa["idproceso"], FECHAINICIO_ARG=etapa["fechaInicioEtapa"], FECHAFIN_ARG=etapa["fechaFinEtapa"], RADICADO_ARG=etapa["radicadoEtapa"], OBSERVACION_ARG=etapa["observacionEtapa"])

        self.update_fase_proceso(etapa["idproceso"])

    def etapa_update_bd(self, etapa):
        print('-------------------------------------')
        print('* ETAPA A ACTUALIZAR -> ', etapa)
        print('-------------------------------------')

        if etapa["fechaFinEtapa"] == 'Invalid date':
            etapa["fechaFinEtapa"] = None

        sql = '''
            UPDATE 
                ETAPA_PROCESO
	        SET 
                FECHAINICIOETAPA= :FECHAINICIO_ARG,
                FECHAFINETAPA = :FECHAFIN_ARG,
                RADICADOETAPA = :RADICADO_ARG,
                OBSERVACIONETAPA = :OBSERVACION_ARG
	        WHERE RADICADOETAPA = :RADICADO_ARG;
        '''
        self.db.engine.execute(text(sql), FECHAINICIO_ARG=etapa["fechaInicioEtapa"], FECHAFIN_ARG=etapa["fechaFinEtapa"], RADICADO_ARG=etapa["radicadoEtapa"], OBSERVACION_ARG=etapa["observacionEtapa"])

        self.update_fase_proceso(etapa["idproceso"])
            
                        
    def etapa_delete_bd(self, etapa):
        print('-------------------------------------')
        print('* ETAPA A ELIMINAR -> ', etapa)
        print('-------------------------------------')
        sql = '''
            DELETE FROM ETAPA_PROCESO
            WHERE RADICADOETAPA = :RADICADO_ARG;
        '''
        self.db.engine.execute(text(sql), RADICADO_ARG=etapa["radicadoEtapa"])

        self.update_fase_proceso(etapa["idproceso"])

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