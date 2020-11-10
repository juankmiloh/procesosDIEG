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
    AND S.IDSERVICIO = :SERVICIO_ARG OR 0 = :SERVICIO_ARG;

-- http://localhost:5000/procesosDIEG/api/empresa?servicio=0

----------------------------
-- CONSULTA PARA OBTENER LISTADO DE PROCESOS
----------------------------
SELECT 
    P.IDPROCESO,
    P.RADICADOPROCESO AS EXPEDIENTE,
    P.FECHACADUCIDAD AS CADUCIDAD,
    EMP.NOMBRE AS EMPRESA,
	E.NOMBREESTADO AS ESTADO,
    S.NOMBRE AS SERVICIO,
    U.NOMBRE || ' ' || U.APELLIDO AS USUARIO
FROM
    EMPRESA EMP, SERVICIO S, PROCESO P, ESTADO E, USUARIOS U
WHERE
    P.EMPRESA = EMP.IDEMPRESA
    AND P.IDSERVICIO = S.IDSERVICIO
	AND P.ESTADO = E.IDESTADO
    AND P.USUARIOASIGNADO = U.IDUSUARIO
ORDER BY P.IDPROCESO ASC;

----------------------------
-- CONSULTA PARA OBTENER LISTADO DE PROCESOS Y SUS CAUSAS
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