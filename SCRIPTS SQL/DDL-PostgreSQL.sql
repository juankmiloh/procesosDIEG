----------------------------
-- DDL TABLA ETAPA
----------------------------
CREATE TABLE ETAPA (
  IDETAPA SERIAL  NOT NULL ,
  SIGUIENTEETAPA INTEGER    ,
  NOMBRE TEXT    ,
PRIMARY KEY(IDETAPA),
  FOREIGN KEY(SIGUIENTEETAPA)
    REFERENCES ETAPA(IDETAPA));

CREATE INDEX IFK_REL_08 ON ETAPA (SIGUIENTEETAPA);

----------------------------
-- DDL TABLA TIPOSANCION
----------------------------
CREATE TABLE TIPOSANCION (
  IDTIPOSANCION SERIAL  NOT NULL ,
  NOMBRETIPOSANCION TEXT      ,
PRIMARY KEY(IDTIPOSANCION));

----------------------------
-- DDL TABLA SERVICIO
----------------------------
CREATE TABLE SERVICIO (
  IDSERVICIO SERIAL NOT NULL,
  NOMBRE TEXT  NULL    ,
PRIMARY KEY(IDSERVICIO));

----------------------------
-- DDL TABLA USUARIO
----------------------------
CREATE TABLE USUARIOS (
  IDUSUARIO SERIAL  NOT NULL ,
  NOMBRE TEXT    ,
  APELLIDO TEXT,
  ROL INTEGER,
  CONTRASENA TEXT      ,
PRIMARY KEY(IDUSUARIO));

----------------------------
-- DDL TABLA ROL
----------------------------
CREATE TABLE ROL (
  IDROL SERIAL  NOT NULL,
  DESCRIPCION TEXT  NULL    ,
PRIMARY KEY(IDROL));

----------------------------
-- DDL TABLA ESTADO
----------------------------
CREATE TABLE ESTADO (
  IDESTADO SERIAL  NOT NULL ,
  NOMBREESTADO TEXT      ,
PRIMARY KEY(IDESTADO));

----------------------------
-- DDL TABLA CAUSAL
----------------------------
CREATE TABLE CAUSAL (
  IDCAUSAL SERIAL  NOT NULL ,
  NOMBRECAUSAL TEXT      ,
PRIMARY KEY(IDCAUSAL));

----------------------------
-- DDL TABLA DESCISIONRECURSO
----------------------------
CREATE TABLE DESCISIONRECURSO (
  IDDESCISIONRECURSO SERIAL  NOT NULL ,
  TIPODESCISIONRECURSO TEXT      ,
PRIMARY KEY(IDDESCISIONRECURSO));

----------------------------
-- DDL TABLA EMPRESA
----------------------------
CREATE TABLE EMPRESA (
  CONSECUTIVO SERIAL  NOT NULL ,
  IDEMPRESA INTEGER,
  NOMBRE TEXT    ,
  NIT INTEGER    ,
  SERVICIO INTEGER,
PRIMARY KEY(CONSECUTIVO));

----------------------------
-- DDL TABLA PROCESO
----------------------------
CREATE TABLE PROCESO (
  IDPROCESO SERIAL  NOT NULL ,
  RADICADOPROCESO TEXT   NOT NULL ,
  USUARIOASIGNADO INTEGER   NOT NULL ,
  EMPRESA INTEGER   NOT NULL ,
  IDSERVICIO INTEGER NOT NULL,
  ESTADO INTEGER NOT NULL,
  TIPOSANCION INTEGER,
  DESCISIONRECURSO INTEGER,
  MONTOSANCION INTEGER      ,
  FECHACADUCIDAD TIMESTAMP WITH TIME ZONE      ,
PRIMARY KEY(IDPROCESO),
UNIQUE (IDPROCESO, RADICADOPROCESO),
  FOREIGN KEY(ESTADO)
    REFERENCES ESTADO(IDESTADO),
  FOREIGN KEY(USUARIOASIGNADO)
    REFERENCES USUARIOS(IDUSUARIO),
  FOREIGN KEY(DESCISIONRECURSO)
    REFERENCES DESCISIONRECURSO(IDDESCISIONRECURSO),
  FOREIGN KEY(TIPOSANCION)
    REFERENCES TIPOSANCION(IDTIPOSANCION));

CREATE INDEX IFK_REL_02 ON PROCESO (ESTADO);
CREATE INDEX IFK_REL_03 ON PROCESO (EMPRESA);
CREATE INDEX IFK_REL_07 ON PROCESO (USUARIOASIGNADO);
CREATE INDEX IFK_REL_08 ON PROCESO (DESCISIONRECURSO);
CREATE INDEX IFK_REL_09 ON PROCESO (TIPOSANCION);

----------------------------
-- EJECUTAR DESPUES DE CREAR LAS TABLAS (PROCESO - PROCESO_CAUSAL - ETAPA_PROCESO)
-- FUNCION QUE EJECUTARA EL TRIGGER (INSERTAR DATOS EN LA TABLA PROCESO_CAUSAL Y LA TABLA ETAPA_PROCESO) CUANDO SE INSERTEN DATOS EN LA TABLA PROCESO
-- CON EL OBJETIVO DE INICIALIZAR EL MISMO IDPROCESO EN LAS (3) TABLAS (PROCESO - PROCESO_CAUSAL - ETAPA_PROCESO)
----------------------------
CREATE FUNCTION SP_PROCESO() RETURNS TRIGGER
AS
$$
BEGIN

INSERT INTO PROCESO_CAUSAL(IDPROCESO) VALUES (NEW.IDPROCESO);
INSERT INTO ETAPA_PROCESO(etapa, proceso, fechainicioetapa, fechafinetapa, radicadoetapa, observacionetapa)
VALUES (10, NEW.IDPROCESO, CURRENT_TIMESTAMP, null, 'P'||NEW.IDPROCESO||'EIG', 'Se inicia la etapa de IG');

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
-- DDL TABLA PROCESO_CAUSAL
----------------------------
CREATE TABLE PROCESO_CAUSAL (
  IDPROCESO INTEGER   NOT NULL ,
  IDCAUSAL INTEGER,
  FECHAHECHOS DATE    ,
  DESCRIPCION TEXT      ,
PRIMARY KEY(IDPROCESO),
  FOREIGN KEY(IDCAUSAL)
    REFERENCES CAUSAL(IDCAUSAL),
  FOREIGN KEY(IDPROCESO)
    REFERENCES PROCESO(IDPROCESO));

CREATE INDEX IFK_REL_11 ON PROCESO_CAUSAL (IDCAUSAL);
CREATE INDEX IFK_REL_10 ON PROCESO_CAUSAL (IDPROCESO);

----------------------------
-- DDL TABLA ETAPA_PROCESO
----------------------------
CREATE TABLE ETAPA_PROCESO (
  ETAPA INTEGER   NOT NULL ,
  PROCESO INTEGER   NOT NULL ,
  FECHAINICIOETAPA TIMESTAMP WITH TIME ZONE   NOT NULL ,
  FECHAFINETAPA TIMESTAMP WITH TIME ZONE    ,
  RADICADOETAPA TEXT   NOT NULL ,
  OBSERVACIONETAPA TEXT      ,
  TIPONOTIFICACION TEXT      ,
  FECHASIGUIENTEETAPA DATE      ,
PRIMARY KEY(ETAPA, PROCESO),
  FOREIGN KEY(ETAPA)
    REFERENCES ETAPA(IDETAPA),
  FOREIGN KEY(PROCESO)
    REFERENCES PROCESO(IDPROCESO));

CREATE INDEX IFK_REL_04 ON ETAPA_PROCESO (ETAPA);
CREATE INDEX IFK_REL_05 ON ETAPA_PROCESO (PROCESO);