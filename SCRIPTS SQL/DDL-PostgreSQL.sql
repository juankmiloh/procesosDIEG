-- DROP TABLE ETAPA CASCADE;
-- DROP TABLE TIPOSANCION CASCADE;
-- DROP TABLE DEPENDENCIA CASCADE;
-- DROP TABLE SERVICIO CASCADE;
-- DROP TABLE GENERO CASCADE;
-- DROP TABLE ROL CASCADE;
-- DROP TABLE USUARIOS CASCADE;
-- DROP TABLE ESTADO CASCADE;
-- DROP TABLE CAUSAL CASCADE;
-- DROP TABLE DESCISIONRECURSO CASCADE;
-- DROP TABLE EMPRESA CASCADE;
-- DROP TABLE FASE CASCADE;
-- DROP TABLE PROCESO CASCADE;
-- DROP TABLE PROCESO_CAUSAL CASCADE;
-- DROP TABLE ETAPA_PROCESO CASCADE;
-- DROP TABLE TIPOPERSONA CASCADE;
-- DROP TABLE TERCEROS CASCADE;
-- DROP FUNCTION SP_PROCESO() CASCADE;

----------------------------
-- DDL TABLA TIPOSANCION
----------------------------
CREATE TABLE TIPOSANCION (
  IDTIPOSANCION SERIAL NOT NULL,
  NOMBRETIPOSANCION TEXT,
PRIMARY KEY(IDTIPOSANCION));

----------------------------
-- DDL TABLA DEPENDENCIA
----------------------------
CREATE TABLE DEPENDENCIA (
  IDDEPENDENCIA SERIAL NOT NULL,
  NOMBRE TEXT NULL,
  DESCRIPCION TEXT NULL,
PRIMARY KEY(IDDEPENDENCIA));

----------------------------
-- DDL TABLA SERVICIO
----------------------------
CREATE TABLE SERVICIO (
  IDSERVICIO SERIAL NOT NULL,
  NOMBRE TEXT NULL,
  DEPENDENCIA INTEGER,
PRIMARY KEY(IDSERVICIO),
FOREIGN KEY(DEPENDENCIA) REFERENCES DEPENDENCIA(IDDEPENDENCIA));

----------------------------
-- DDL TABLA GENERO
----------------------------
CREATE TABLE GENERO (
  IDGENERO SERIAL NOT NULL,
  NOMBRE TEXT,
PRIMARY KEY(IDGENERO));

----------------------------
-- DDL TABLA ROL
----------------------------
CREATE TABLE ROL (
  IDROL SERIAL NOT NULL,
  DESCRIPCION TEXT NULL,
PRIMARY KEY(IDROL));

----------------------------
-- DDL TABLA USUARIO
----------------------------
CREATE TABLE USUARIOS (
  IDUSUARIO SERIAL NOT NULL,
  NOMBRE TEXT,
  APELLIDO TEXT,
  GENERO INTEGER,
  NICKNAME TEXT, 
  DESCRIPCION TEXT,
  ROL INTEGER,
  AVATAR TEXT,
  CONTRASENA TEXT,
  TOKEN TEXT,
  EMAIL TEXT NULL,
  DEPENDENCIA INTEGER,
PRIMARY KEY(IDUSUARIO),
FOREIGN KEY(ROL) REFERENCES ROL(IDROL),
FOREIGN KEY(GENERO) REFERENCES GENERO(IDGENERO),
FOREIGN KEY(DEPENDENCIA) REFERENCES DEPENDENCIA(IDDEPENDENCIA));

----------------------------
-- DDL TABLA ESTADO V2.0
----------------------------
CREATE TABLE ESTADO (
  IDESTADO SERIAL NOT NULL,
  NOMBREESTADO TEXT,
  OBLIGATORIEDAD TEXT,
  FECHA_FINAL TEXT,
  VARIOS_ACTOS TEXT,
  OBSERVACION TEXT,
  SIGUIENTEESTADO INTEGER,
PRIMARY KEY(IDESTADO));

----------------------------
-- DDL TABLA CAUSAL
----------------------------
CREATE TABLE CAUSAL (
  IDCAUSAL SERIAL NOT NULL,
  NOMBRECAUSAL TEXT,
PRIMARY KEY(IDCAUSAL));

----------------------------
-- DDL TABLA DESCISIONRECURSO
----------------------------
CREATE TABLE DESCISIONRECURSO (
  IDDESCISIONRECURSO SERIAL NOT NULL,
  TIPODESCISIONRECURSO TEXT,
PRIMARY KEY(IDDESCISIONRECURSO));

----------------------------
-- DDL TABLA EMPRESA
----------------------------
CREATE TABLE EMPRESA (
  CONSECUTIVO SERIAL NOT NULL,
  IDEMPRESA INTEGER,
  NOMBRE TEXT,
  SIGLA text,
  NIT BIGINT,
  SERVICIO INTEGER,
PRIMARY KEY(CONSECUTIVO));

----------------------------
-- DDL TABLA FASES (FASES DEL PROCESO / EN CURSO / FINALIZADO / ELIMINADO)
----------------------------
CREATE TABLE FASE (
  IDFASE SERIAL NOT NULL,
  NOMBRE TEXT NOT NULL,
PRIMARY KEY(IDFASE));

----------------------------
-- DDL TABLA PROCESO v2.0
----------------------------
CREATE TABLE PROCESO (
  IDPROCESO SERIAL NOT NULL,
  RADICADOPROCESO TEXT NOT NULL,
  USUARIOASIGNADO INTEGER NOT NULL,
  REVISOR INTEGER NOT NULL,
  EMPRESA INTEGER NOT NULL,
  IDSERVICIO INTEGER NOT NULL,
  FASE INTEGER NOT NULL,
  TIPOSANCION INTEGER,
  DESCISIONRECURSO INTEGER,
  MONTOSANCION DOUBLE PRECISION,
  DEPENDENCIA INTEGER,
  FECHACADUCIDAD DATE,
  FECHAREGISTRO TIMESTAMP WITH TIME ZONE,
PRIMARY KEY(IDPROCESO),
UNIQUE (RADICADOPROCESO),
FOREIGN KEY(USUARIOASIGNADO) REFERENCES USUARIOS(IDUSUARIO),
FOREIGN KEY(REVISOR) REFERENCES USUARIOS(IDUSUARIO),
FOREIGN KEY(DESCISIONRECURSO) REFERENCES DESCISIONRECURSO(IDDESCISIONRECURSO),
FOREIGN KEY(TIPOSANCION) REFERENCES TIPOSANCION(IDTIPOSANCION),
FOREIGN KEY(DEPENDENCIA) REFERENCES DEPENDENCIA(IDDEPENDENCIA));

CREATE INDEX IFK_REL_01 ON PROCESO (FASE);
CREATE INDEX IFK_REL_03 ON PROCESO (EMPRESA);
CREATE INDEX IFK_REL_07 ON PROCESO (USUARIOASIGNADO);
CREATE INDEX IFK_REL_08 ON PROCESO (DESCISIONRECURSO);
CREATE INDEX IFK_REL_09 ON PROCESO (TIPOSANCION);

----------------------------
-- DDL TABLA ETAPA_PROCESO V2.0
----------------------------
CREATE TABLE ETAPA_PROCESO (
  IDPROCESO INTEGER NOT NULL,
  IDESTADO INTEGER NOT NULL,
  NUMEROACTO INTEGER NOT NULL,
  RADICADO TEXT NOT NULL,
  FECHAINICIO TIMESTAMP WITH TIME ZONE,
  FECHAFIN TIMESTAMP WITH TIME ZONE,
  OBSERVACION TEXT,
  FECHAREGISTRO TIMESTAMP WITH TIME ZONE,
PRIMARY KEY(IDPROCESO, IDESTADO, NUMEROACTO),
FOREIGN KEY(IDPROCESO) REFERENCES PROCESO(IDPROCESO),
FOREIGN KEY(IDESTADO) REFERENCES ESTADO(IDESTADO));

CREATE INDEX IFK_REL_04 ON ETAPA_PROCESO (IDPROCESO);
CREATE INDEX IFK_REL_05 ON ETAPA_PROCESO (IDESTADO);

----------------------------
-- EJECUTAR DESPUES DE CREAR LAS TABLAS (PROCESO - PROCESO_CAUSAL - ETAPA_PROCESO)
-- FUNCION QUE EJECUTARA EL TRIGGER (INSERTAR DATOS EN LA TABLA PROCESO_CAUSAL Y LA TABLA ETAPA_PROCESO) CUANDO SE INSERTEN DATOS EN LA TABLA PROCESO
-- CON EL OBJETIVO DE INICIALIZAR EL MISMO IDPROCESO EN LAS (3) TABLAS (PROCESO - PROCESO_CAUSAL - ETAPA_PROCESO)
----------------------------
CREATE FUNCTION SP_PROCESO() RETURNS TRIGGER
AS
$$
BEGIN

-- INSERT INTO PROCESO_CAUSAL(IDPROCESO) VALUES (NEW.IDPROCESO);
INSERT INTO ETAPA_PROCESO(IDPROCESO, IDESTADO, NUMEROACTO, RADICADO, FECHAINICIO, FECHAFIN, OBSERVACION, FECHAREGISTRO) 
VALUES (NEW.IDPROCESO, 1, 1, 'No registra', null, null, 'Se inicia la etapa de IG', CURRENT_TIMESTAMP);

RETURN NEW;
END;
$$
LANGUAGE PLPGSQL;

----------------------------
-- CREACIÓN DEL TRIGGER QUE SE EJECUTARA CUANDO SE INSERTEN DATOS EN LA TABLA PROCESO
----------------------------
CREATE TRIGGER TR_PROCESO 
  AFTER INSERT
  ON PROCESO
  FOR EACH ROW
  EXECUTE PROCEDURE SP_PROCESO();

----------------------------
-- BORRADO DEL TRIGGER
----------------------------
-- DROP FUNCTION SP_PROCESO() CASCADE;

----------------------------
-- DDL TABLA PROCESO_CAUSAL v1.0
----------------------------
CREATE TABLE PROCESO_CAUSAL (
  IDPROCESO INTEGER NOT NULL,
  IDCAUSAL INTEGER,
  FECHAHECHOS TIMESTAMP WITH TIME ZONE,
  DESCRIPCION TEXT,
FOREIGN KEY(IDCAUSAL) REFERENCES CAUSAL(IDCAUSAL),
FOREIGN KEY(IDPROCESO) REFERENCES PROCESO(IDPROCESO));

CREATE INDEX IFK_REL_11 ON PROCESO_CAUSAL (IDCAUSAL);
CREATE INDEX IFK_REL_10 ON PROCESO_CAUSAL (IDPROCESO);
CREATE INDEX IFK_REL_13 ON PROCESO (IDPROCESO);

----------------------------
-- DDL TABLA TIPO_PERSONA
----------------------------
CREATE TABLE TIPOPERSONA (
  IDTIPOPERSONA SERIAL NOT NULL,
  NOMBRE TEXT NULL,
PRIMARY KEY(IDTIPOPERSONA));

----------------------------
-- DDL TABLA TERCEROS
----------------------------
CREATE TABLE TERCEROS (
  IDTERCEROS SERIAL NOT NULL,
  IDPROCESO INTEGER  NOT NULL  ,
  IDTIPOPERSONA INTEGER  NOT NULL  ,
  DOCUMENTO DOUBLE PRECISION  ,
  NOMBRE TEXT NULL  ,
  DIRECCION TEXT NULL  ,
  EMAIL TEXT NULL,
PRIMARY KEY(IDTERCEROS),
FOREIGN KEY(IDPROCESO) REFERENCES PROCESO(IDPROCESO),
FOREIGN KEY(IDTIPOPERSONA) REFERENCES TIPOPERSONA(IDTIPOPERSONA));

CREATE INDEX TERCEROS_FKINDEX1 ON PROCESO (IDPROCESO);
CREATE INDEX TERCEROS_FKINDEX2 ON TIPOPERSONA (IDTIPOPERSONA);