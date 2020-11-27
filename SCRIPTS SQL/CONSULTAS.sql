----------------------------
-- CONSULTA PARA OBTENER LISTADO DE EMPRESAS
----------------------------
SELECT E.IDEMPRESA, E.NOMBRE, E.NIT, S.NOMBRE AS SERVICIO FROM EMPRESA E, SERVICIO S
WHERE E.SERVICIO = S.idservicio
AND S.IDSERVICIO IN (1, 2, 3);

----------------------------
-- CONSULTA PARA OBTENER LISTADO DE EMPRESAS POR UN SERVICIO ESPECIFICO
----------------------------
SELECT
    E.IDEMPRESA,
    E.NOMBRE,
    E.NIT,
    S.IDSERVICIO,
    S.NOMBRE AS SERVICIO 
FROM EMPRESA E, SERVICIO S
WHERE
    E.SERVICIO = S.idservicio
    AND (S.IDSERVICIO = :SERVICIO_ARG OR 0 = :SERVICIO_ARG)
ORDER BY E.NOMBRE ASC;

-- http://localhost:5000/procesosDIEG/api/empresa?servicio=0

----------------------------
-- CONSULTA PARA OBTENER LISTADO DE PROCESOS
----------------------------
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

----------------------------
-- CONSULTA PARA OBTENER UN PROCESO ESPECIFICO
----------------------------
SELECT 
	P.IDPROCESO,
	P.RADICADOPROCESO AS EXPEDIENTE,
	S.NOMBRE AS SERVICIO,
	EMP.NOMBRE AS EMPRESA,
	U.IDUSUARIO AS IDUSUARIO,
	E.NOMBREESTADO AS ESTADO,
	P.TIPOSANCION,
	P.MONTOSANCION,
	P.DESCISIONRECURSO AS DECISION,
	PC.IDCAUSAL,
	PC.FECHAHECHOS,
	PC.DESCRIPCION,
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
	AND P.IDPROCESO = 1
	AND P.IDPROCESO = PC.IDPROCESO
	AND P.IDPROCESO = EP.PROCESO
	AND EP.ETAPA = ET.IDETAPA;

----------------------------
-- CONSULTA PARA OBTENER LISTADO DE PROCESOS Y SUS CAUSAS [REVISAR]
----------------------------
SELECT 
    P.IDPROCESO,
    P.RADICADOPROCESO,
    PC.FECHACADUCIDAD,
    EMP.NOMBRE,
    E.NOMBREESTADO,
    S.NOMBRE,
    U.NOMBRE || ' ' || U.APELLIDO AS USUARIO
FROM
    EMPRESA EMP, SERVICIO S, PROCESO P, PROCESO_CAUSAL PC, CAUSAL C, ESTADO E, USUARIOS U
WHERE
    P.EMPRESA = EMP.IDEMPRESA
    AND P.SERVICIO = S.IDSERVICIO
    AND P.IDPROCESO = PC.IDPROCESO
    AND C.IDCAUSAL = PC.IDCAUSAL
    AND P.ESTADO = E.IDESTADO
    AND P.USUARIOASIGNADO = U.IDUSUARIO;

----------------------------
-- CANTIDAD DE ETAPAS POR PROCESO
----------------------------
SELECT P.IDPROCESO, COUNT(*) AS CANT_ETAPAS FROM PROCESO P, ETAPA_PROCESO EP WHERE P.IDPROCESO = EP.PROCESO GROUP BY P.IDPROCESO;