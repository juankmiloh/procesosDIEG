from sqlalchemy.sql import text


class CausalRepository:
    def __init__(self, db):
        self.db = db

    def get_causal_bd(self):
        sql = '''
            SELECT * FROM CAUSAL;
        '''
        return self.db.engine.execute(text(sql)).fetchall()

    def get_causal_proceso_bd(self, idProceso):
        sql = '''
            SELECT PC.*, C.NOMBRECAUSAL FROM PROCESO_CAUSAL PC, CAUSAL C WHERE IDPROCESO = :IDPROCESO_ARG AND PC.IDCAUSAL = C.IDCAUSAL;
        '''
        return self.db.engine.execute(text(sql), IDPROCESO_ARG=idProceso).fetchall()

    def causal_insert_bd(self, causal):
        print('-------------------------------------')
        print('OBJ CAUSAL -> ', causal)
        print('-------------------------------------')
        sql = '''
            INSERT INTO PROCESO_CAUSAL(IDPROCESO, IDCAUSAL, FECHAHECHOS, DESCRIPCION)
            VALUES (:IDPROCESO_ARG, :IDCAUSAL_ARG, :FECHAHECHOS_ARG, :DESCRIPCION_ARG);
        '''
        self.db.engine.execute(text(sql), IDPROCESO_ARG=causal["idproceso"], IDCAUSAL_ARG=causal["idcausal"], FECHAHECHOS_ARG=causal["f_hechos"], DESCRIPCION_ARG=causal["descripcion"])

    def causal_update_bd(self, causal):
        print('-------------------------------------')
        print('* CAUSAL A ACTUALIZAR -> ', causal)
        print('-------------------------------------')

        sql = '''
            UPDATE 
                PROCESO_CAUSAL
	        SET 
                FECHAHECHOS = :FECHAHECHOS_ARG,
                DESCRIPCION = :DESCRIPCION_ARG
	        WHERE IDPROCESO = :IDPROCESO_ARG
            AND IDCAUSAL = :IDCAUSAL_ARG;
        '''
        self.db.engine.execute(text(sql), IDPROCESO_ARG=causal["idproceso"], IDCAUSAL_ARG=causal["codcausal"], FECHAHECHOS_ARG=causal["f_hechos"], DESCRIPCION_ARG=causal["descripcion"])
            
                        
    def causal_delete_bd(self, causal):
        print('-------------------------------------')
        print('* CAUSAL A ELIMINAR -> ', causal)
        print('-------------------------------------')
        sql = '''
            DELETE FROM PROCESO_CAUSAL
            WHERE IDPROCESO = :IDPROCESO_ARG
            AND IDCAUSAL = :IDCAUSAL_ARG;
        '''
        self.db.engine.execute(text(sql), IDPROCESO_ARG=causal["idproceso"], IDCAUSAL_ARG=causal["idcausal"])