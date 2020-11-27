TRUNCATE TABLE PROCESO RESTART IDENTITY CASCADE;
TRUNCATE TABLE ETAPA_PROCESO RESTART IDENTITY CASCADE;
TRUNCATE TABLE PROCESO_CAUSAL RESTART IDENTITY CASCADE;
----------------------------
-- DML TABLA ROL
----------------------------
INSERT INTO ROL (DESCRIPCION) VALUES ('administrador');
INSERT INTO ROL (DESCRIPCION) VALUES ('abogado');

----------------------------
-- DML TABLA USUARIO
----------------------------
INSERT INTO USUARIOS(NOMBRE, APELLIDO, NICKNAME, DESCRIPCION, ROL, AVATAR, CONTRASENA, TOKEN) VALUES ('Madia', 'Ortega', 'mortega', 'Directora de investigaciones - Administrador', 1, 'https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif', '123456', 'mortega-token');
INSERT INTO USUARIOS(NOMBRE, APELLIDO, NICKNAME, DESCRIPCION, ROL, AVATAR, CONTRASENA, TOKEN) VALUES ('Marco', 'Campaña', 'mcampana', 'Abogado DIEG', 2, 'https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif', '123456', 'mcampana-token');
INSERT INTO USUARIOS(NOMBRE, APELLIDO, NICKNAME, DESCRIPCION, ROL, AVATAR, CONTRASENA, TOKEN) VALUES ('Nathalia', 'Pinzon', 'npinzon', 'Abogada DIEG', 2, 'https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif', '123456', 'npinzon-token');

----------------------------
-- DML TABLA CAUSAL
----------------------------
INSERT INTO CAUSAL (NOMBRECAUSAL) VALUES ('Falla en la prestación del servicio');
INSERT INTO CAUSAL (NOMBRECAUSAL) VALUES ('Incumplimiento de aspectos técnicos');
INSERT INTO CAUSAL (NOMBRECAUSAL) VALUES ('Incumplimiento de los indicadores de calidad');
INSERT INTO CAUSAL (NOMBRECAUSAL) VALUES ('No atención a requerimientos');
INSERT INTO CAUSAL (NOMBRECAUSAL) VALUES ('Retie');
INSERT INTO CAUSAL (NOMBRECAUSAL) VALUES ('SUI');
INSERT INTO CAUSAL (NOMBRECAUSAL) VALUES ('Violación régimen tarifario');
INSERT INTO CAUSAL (NOMBRECAUSAL) VALUES ('Violación reglamentaria');

----------------------------
-- DML TABLA ESTADO
----------------------------
INSERT INTO ESTADO (NOMBREESTADO) VALUES ('Informe técnico de gestión');
INSERT INTO ESTADO (NOMBREESTADO) VALUES ('Memorando devolución');
INSERT INTO ESTADO (NOMBREESTADO) VALUES ('Memorando aclaratorio');
INSERT INTO ESTADO (NOMBREESTADO) VALUES ('Averiguación preliminar');
INSERT INTO ESTADO (NOMBREESTADO) VALUES ('Pliego de cargos');
INSERT INTO ESTADO (NOMBREESTADO) VALUES ('Descargos');
INSERT INTO ESTADO (NOMBREESTADO) VALUES ('Etapa probatoria');
INSERT INTO ESTADO (NOMBREESTADO) VALUES ('Alegatos');
INSERT INTO ESTADO (NOMBREESTADO) VALUES ('Alegatos presentados');
INSERT INTO ESTADO (NOMBREESTADO) VALUES ('Fallo');
INSERT INTO ESTADO (NOMBREESTADO) VALUES ('Presentación de recurso');
INSERT INTO ESTADO (NOMBREESTADO) VALUES ('Acto que resuelve recurso');
INSERT INTO ESTADO (NOMBREESTADO) VALUES ('Firmeza');
INSERT INTO ESTADO (NOMBREESTADO) VALUES ('Archivo');
INSERT INTO ESTADO (NOMBREESTADO) VALUES ('Eliminado');

----------------------------
-- DML TABLA descisionRecurso
----------------------------
INSERT INTO DESCISIONRECURSO (TIPODESCISIONRECURSO) VALUES('Aclara');
INSERT INTO DESCISIONRECURSO (TIPODESCISIONRECURSO) VALUES('Adiciona');
INSERT INTO DESCISIONRECURSO (TIPODESCISIONRECURSO) VALUES('Confirma');
INSERT INTO DESCISIONRECURSO (TIPODESCISIONRECURSO) VALUES('Modifica');
INSERT INTO DESCISIONRECURSO (TIPODESCISIONRECURSO) VALUES('Revoca');
INSERT INTO DESCISIONRECURSO (TIPODESCISIONRECURSO) VALUES('Por definir');

----------------------------
-- DML TABLA nombreTipoSancion
----------------------------
TRUNCATE TABLE tipoSancion RESTART IDENTITY CASCADE; -- LINEA PARA ELIMINAR DATOS DE UNA TABLA Y REINICIAR EL AUTOINCREMENT

INSERT INTO TIPOSANCION (NOMBRETIPOSANCION) VALUES('Amonestación');
INSERT INTO TIPOSANCION (NOMBRETIPOSANCION) VALUES('Archivo');
INSERT INTO TIPOSANCION (NOMBRETIPOSANCION) VALUES('Caducidad de contratos');
INSERT INTO TIPOSANCION (NOMBRETIPOSANCION) VALUES('Multa');
INSERT INTO TIPOSANCION (NOMBRETIPOSANCION) VALUES('Prohibición');
INSERT INTO TIPOSANCION (NOMBRETIPOSANCION) VALUES('Separación administrativa');
INSERT INTO TIPOSANCION (NOMBRETIPOSANCION) VALUES('Suspensión');
INSERT INTO TIPOSANCION (NOMBRETIPOSANCION) VALUES('Toma de posesión');
INSERT INTO TIPOSANCION (NOMBRETIPOSANCION) VALUES('Por definir');

----------------------------
-- DML TABLA FASE
----------------------------
INSERT INTO FASE (NOMBRE) VALUES ('En curso');
INSERT INTO FASE (NOMBRE) VALUES ('Finalizado');
INSERT INTO FASE (NOMBRE) VALUES ('Eliminado');

----------------------------
-- DML TABLA PROCESO
----------------------------
--TRUNCATE TABLE PROCESO RESTART IDENTITY;
--truncate table proceso_causal;
--truncate table ETAPA_PROCESO;
INSERT INTO PROCESO(RADICADOPROCESO, USUARIOASIGNADO, EMPRESA, IDSERVICIO, FASE, FECHACADUCIDAD)
VALUES ('426752354X7XD3E', 2, 2249, 1, 14, '2014/03/26');
-- DATOS PARA ENVIO DESDE POSTMANN
-- {"radicado":"7848284648434381E","usuario": 3,"empresa": 502,"servicio": 1,"fase": 14, "fecha_caducidad": "2014/03/26"}

----------------------------
-- DML TABLA ETAPA
----------------------------
INSERT INTO ETAPA(IDESTADO, NOMBRE, SIGUIENTEETAPA, ESTAMPILLA) VALUES (14, 'Archivo', null, 'ARCH');
INSERT INTO ETAPA(IDESTADO, NOMBRE, SIGUIENTEETAPA, ESTAMPILLA) VALUES (13, 'Firmeza', 1, 'FIR');
INSERT INTO ETAPA(IDESTADO, NOMBRE, SIGUIENTEETAPA, ESTAMPILLA) VALUES (12, 'Resolución resuelve recurso', 2, 'RRR');
INSERT INTO ETAPA(IDESTADO, NOMBRE, SIGUIENTEETAPA, ESTAMPILLA) VALUES (11, 'Escrito de recurso', 3, 'EDR');
INSERT INTO ETAPA(IDESTADO, NOMBRE, SIGUIENTEETAPA, ESTAMPILLA) VALUES (10, 'Resolución', 4, 'RES');
INSERT INTO ETAPA(IDESTADO, NOMBRE, SIGUIENTEETAPA, ESTAMPILLA) VALUES (9, 'Escrito de alegatos', 5, 'EDA');
INSERT INTO ETAPA(IDESTADO, NOMBRE, SIGUIENTEETAPA, ESTAMPILLA) VALUES (8, 'Auto traslado para alegatos', 6, 'ATPA');
INSERT INTO ETAPA(IDESTADO, NOMBRE, SIGUIENTEETAPA, ESTAMPILLA) VALUES (7, 'Primer auto de pruebas', 7, 'PADP');
INSERT INTO ETAPA(IDESTADO, NOMBRE, SIGUIENTEETAPA, ESTAMPILLA) VALUES (6, 'Escrito de descargos', 8, 'EDD');
INSERT INTO ETAPA(IDESTADO, NOMBRE, SIGUIENTEETAPA, ESTAMPILLA) VALUES (5, 'Pliego de cargos', 9, 'PDC');
INSERT INTO ETAPA(IDESTADO, NOMBRE, SIGUIENTEETAPA, ESTAMPILLA) VALUES (4, 'Auto archivo averiguación preliminar', 10, 'AAAP');
INSERT INTO ETAPA(IDESTADO, NOMBRE, SIGUIENTEETAPA, ESTAMPILLA) VALUES (4, 'Auto averiguación preliminar ', 11, 'APP');
INSERT INTO ETAPA(IDESTADO, NOMBRE, SIGUIENTEETAPA, ESTAMPILLA) VALUES (3, 'Memorando de alcance', 12, 'MDA'); -- Tambien hace referencia al Memorando aclarator, 4io
INSERT INTO ETAPA(IDESTADO, NOMBRE, SIGUIENTEETAPA, ESTAMPILLA) VALUES (2, 'Memorando de devolución', 13, 'MDD');
INSERT INTO ETAPA(IDESTADO, NOMBRE, SIGUIENTEETAPA, ESTAMPILLA) VALUES (1, 'Memorando IG', 14, 'MIG');

--- Tener presente que se puede guardar el campo de resolucion y fecha asociados a la decision en la tabla proceso

----------------------------
-- DML TABLA ETAPA_PROCESO
----------------------------
INSERT INTO ETAPA_PROCESO(ETAPA, PROCESO, FECHAINICIOETAPA, FECHAFINETAPA, RADICADOETAPA, OBSERVACIONETAPA)
VALUES (10, 1, '2016/12/31', null, 123456789, 'Se inicia la etapa de IG');
INSERT INTO ETAPA_PROCESO(ETAPA, PROCESO, FECHAINICIOETAPA, FECHAFINETAPA, RADICADOETAPA, OBSERVACIONETAPA)
VALUES (9, 1, '2017/01/01', null, 123, 'Radicado memorando devolución');
INSERT INTO ETAPA_PROCESO(ETAPA, PROCESO, FECHAINICIOETAPA, FECHAFINETAPA, RADICADOETAPA, OBSERVACIONETAPA, TIPONOTIFICACION, FECHASIGUIENTEETAPA)
VALUES (8, 1, '2017/03/01', null, 1234, 'Radicado memorando de alcance', 'Verbal', '2020/12/31');

----------------------------
-- DML TABLA PROCESO_CAUSAL
----------------------------
-- INSERT INTO proceso_causal(idproceso, causal_idcausal, fechahechos, fechacaducidad) 
-- VALUES (1, 3, '2016/01/01', '2020/12/31');
INSERT INTO PROCESO_CAUSAL(IDPROCESO) VALUES (1);

----------------------------
-- DML TABLA SERVICIO
----------------------------
INSERT INTO SERVICIO (NOMBRE) VALUES ('Energía');
INSERT INTO SERVICIO (NOMBRE) VALUES ('Gas');
INSERT INTO SERVICIO (NOMBRE) VALUES ('GLP');

----------------------------
-- DML TABLA EMPRESA | INSERT EMPRESAS ENERGIA
----------------------------
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('1864','AES CHIVOR & CIA SCA ESP','830025205','1');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('3372','A.S.C INGENIERIA SOCIEDAD ANONIMA SA ESP.','814002979','1');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('536','CELSIA COLOMBIA S.A. E.S.P.','800249860','1');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('44278','CELSIA TOLIMA S.A. E.S.P.','901280981','1');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('502','CENTRAL HIDROELECTRICA DE CALDAS S.A. E.S.P.','890800128','1');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('520','CENTRALES ELECTRICAS DE NARIÑO S.A. E.S.P.','891200200','1');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('505','CENTRALES ELECTRICAS DEL CAUCA S.A. EMPRESA DE SERVICIOS PUBLICOS ','891500025','1');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('604','CENTRALES ELECTRICAS DEL NORTE DE SANTANDER S.A. ESP','890500514','1');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('2103','CODENSA S.A. ESP','830037248','1');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('2452','COMERCIALIZADORA ANDINA DE ENERGIA SOCIEDAD ANONIMA EMPRESA DE SERVICIOS PUBLICOS','816003879','1');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('20156','COMERCIALIZADORA DEL CAFE S.A.S. E.S.P.','830147341','1');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('3338','COMERCIALIZADORA ELECTRICA DE COLOMBIA SA ESP','811040535','1');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('2023','COMERCIALIZADORA ELECTRICA DEL SINU S.A. E.S.P.','812001325','1');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('637','COMPAÑÍA DE ELECTRICIDAD DE TULUÁ S.A. E.S.P.','891900101','1');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('1058','COMPAÑIA ELECTRICA DE SOCHAGOTA S.A. E.S.P.','800219925','1');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('1031','CORPORACION ELECTRICA DE LA COSTA ATLANTICA S.A E.S.P.','890103010','1');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('2378','DICELER S.A E.S.P.','815001901','1');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('2081','DISTASA S.A. E.S.P.','807001845','1');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('2020','DISTRIBUIDORA Y COMERCIALIZADORA DE ENERGIA ELECTRICA S.A. E.S.P.','815000896','1');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('1811','E. S. P. DE ENERGIA ELECTRICA DE BAJO BAUDO PIZARRO S.A.','818000202','1');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('1816','E.A.T. DE ENERGIA ELECTRICA DEL MUNICIPIO DE  LA TOLA NARIÑO','840000036','1');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('1900','E.A.T. DE PRESTACION DE SERVCIOS PUBLICOS DEL MUNICIPIO DE MOSQUERA EL PORVENIR  E.S.P.','840000071','1');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('20067','EAT ELECTRIFICADORA DE LA ZONA RURAL DE TUMACO','840000937','1');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('1810','E.A.T. PARA EL SERVICIO DE ENERGIA ELECTRICA EN ISCUANDE','840000037','1');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('524','ELECTRIFICADORA DE SANTANDER S.A. E.S.P.','890201230','1');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('1032','ELECTRIFICADORA DEL CAQUETA S.A. ESP','891190127','1');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('2249','ELECTRIFICADORA DEL CARIBE S.A. E.S.P.','802007670','1');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('1014','ELECTRIFICADORA DEL HUILA S.A. E.S.P.','891180001','1');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('600','ELECTRIFICADORA DEL META S.A. E.S.P.','892002210','1');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('1817','ELECTRIFICADORA DEL MUNICIPIO DE RIOSUCIO CHOCO S.A. E.S.P.','818000192','1');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('20432','ELECTRIFICADORA DEL PACIFICO S.A. E.S.P.','900039007','1');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('597','EMGESA S.A. E.S.P.','860063875','1');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('1759','EMPRESA  DE SERVICIOS PUBLICOS DE LEGUIZAMO','846000021','1');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('1892','EMPRESA DE  ENERGÍA  DE GUAPI  S.A. E.S.P.','835000142','1');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('599','EMPRESA DE ENERGIA DE ARAUCA','892099499','1');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('500','EMPRESA DE ENERGIA DE BOYACA S.A. E.S.P. EMPRESA DE SERVICIOS PUBLICOS','891800219','1');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('3370','EMPRESA DE ENERGIA DE CASANARE SA ESP','844004576','1');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('20081','EMPRESA DE ENERGIA DE MAGUI PAYAN S.A E.S.P','840000929','1');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('2073','EMPRESA DE ENERGÍA DE PEREIRA S.A. ESP.','816002019','1');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('2272','EMPRESA DE ENERGIA DE SALAHONDA S.A. E.S.P.','840000203','1');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('523','EMPRESA DE ENERGIA DEL  QUINDIO S.A.E.S.P.','800052640','1');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('2371','EMPRESA DE ENERGIA DEL BAJO PUTUMAYO  S.A.  E.S.P.','846000553','1');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('2331','EMPRESA DE ENERGIA DEL GUAINIA LA CEIBA S.A. E.S.P.','843000057','1');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('2016','EMPRESA DE ENERGIA DEL PUTUMAYO S.A. ESP','846000241','1');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('1846','EMPRESA DE ENERGIA DEL VALLE DE SIBUNDOY S.A. E.S.P. ','846000060','1');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('3076','EMPRESA DE ENERGIA ELECTRICA DEL DEPARTAMENTO DEL GUAVIARE SA ESP','822004680','1');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('3212','EMPRESA DE ENERGIA ELECTRICA DEL DEPARTAMENTO DEL VICHADA S.A','842000155','1');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('2096','EMPRESA DE SERVICIOS DE ENERGIA ELECTRICA Y VARIOS DE LA MACARENA SA','822001610','1');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('1891','EMPRESA DE SERVICIOS PUBLICOS DE BAHIA SOLANO S.A. ESP','818000263','1');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('2054','EMPRESA DE SERVICIOS PUBLICOS DE PUERTO RICO - META','822001395','1');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('1895','EMPRESA DE SERVICOS PUBLICOS DE ACANDI S.A E.S.P.','818000293','1');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('3226','EMPRESA DISTRIBUIDORA DEL PACIFICO S.A. E.S.P','818001629','1');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('1809','EMPRESA ELECTRIFICADORA DE NUQUI   E.S.P.   S. A ECONOMIA MIXTA','818000166','1');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('3318','EMPRESA GENERADORA DE ENERGIA DEL TOLIMA S.A E.S.P.','809010915','1');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('1867','EMPRESA GENERADORA DE ENERGIA ELECTRICA DEL CHARCO S.A E.S.P','840000035','1');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('1890','EMPRESA MIXTA DE SERVICIOS PÚBLICOS DE ENERGÍA ELÉCTRICA DE TIMBIQUI S.A.','817000487','1');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('694','EMPRESA MUNICIPAL DE ENERGÍA ELÉCTRICA S.A-E.S.P','891500061','1');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('569','EMPRESA MUNICIPAL DE SERVICIOS PUBLICOS DE CARTAGENA DEL CHAIRA','828000191','1');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('2170','EMPRESA SIGLO XXI EICE ESP','842000030','1');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('2128','EMPRESA URRA S.A. E.S.P.','800175746','1');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('2438','EMPRESAS MUNICIPALES DE CALI   E.I.C.E  E.S.P','890399003','1');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('617','EMPRESAS MUNICIPALES DE CARTAGO E.S.P.','836000349','1');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('564','EMPRESAS PÚBLICAS DE MEDELLIN E.S.P.','890904996','1');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('2824','ENERCO S.A. E.S.P.','805016928','1');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('3111','ENERGETICOS S.A.S.  E.S.P. DISTRIBUIDORA Y COMERCIALIZADORA DE ENERGIA GAS E HIDROCARBUROS','830092965','1');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('2159','ENERGIA CONFIABLE S.A. E.S.P.','802006121','1');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('20437','ENERTOTAL S.A. E.S.P.','900039901','1');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('20256','E2 ENERGIA EFICIENTE S.A. E.S.P.','802025052','1');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('1757','GESTION ENERGETICA S.A. ESP','800194208','1');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('594','GRUPO ENERGÍA BOGOTA S.A. ESP.','899999082','1');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('592','INTERCONEXION ELECTRICA S.A. E.S.P.','860016610','1');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('480','ISAGEN S.A. E.S.P.','811000740','1');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('2080','JUNTA ADMINISTRADORA DE SERVICIOS PÚBLICOS  DE  CAPURGANA','818000276','1');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('3332','LATIN AMERICAN CAPITAL CORP SA ESP','809011444','1');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('256','MUNICIPIO DE PUERTO LLERAS ','892099309','1');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('20153','MUNICIPIO DE SIPI','800095613','1');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('1212','MUNICIPIO DE SOLANO ','800095786','1');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('3268','PRIME TERMOFLORES S.AS E.S.P.','830113630','1');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('497','PROMOTORA DE ENERGIA ELECTRICA DE CARTAGENA SAS ESP','800149537','1');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('2398','PROYECTOS ENERGETICOS DEL CAUCA S.A. E.S.P.','817000362','1');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('1737','RUITOQUE S.A. E.S.P.','804001062','1');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('1720','SOCIEDAD PRODUCTORA DE ENERGÍA DE SAN ANDRES Y PROVIDENCIA S.A. E.S.P.','827000108','1');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('485','TERMOBARRANQUILLA S.A. E.S.P.','800245746','1');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('2261','TERMOCANDELARIA SOCIEDAD EN COMANDITA POR ACCIONES EMPRESA DE SERVICIOS PUBLICOS','806005008','1');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('1077','TERMOEMCALI  I  S.A. ESP','800253702','1');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('2412','TERMOPIEDRAS S.A. E.S.P.','830058506','1');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('1806','TERMOVALLE S.A.S. E.S.P','805003351','1');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('20033','TERMOYOPAL GENERACION 2 S.A.S. E.S.P.','830129277','1');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('2998','TRANSACCIONES DE ENERGIA S.A. E.S.P.','802014214','1');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('2247','TRANSELCA S.A. E.S.P.','802007669','1');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('20217','UNIDAD DE SERVICIOS PUBLICOS DOMICILIARIOS DE ACUEDUCTO, ALCANTARILLADO, ASEO Y ENERGIA ZONA NO INTERCONECTADA, EN EL MUNICIPIO DE CARURU - VAUPES','832000605','1');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('2322','VATIA S.A. E.S.P.','817001892','1');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('20481','XM COMPAÑIA DE EXPERTOS EN MERCADOS S.A. E.S.P.','900042857','1');

----------------------------
-- DML TABLA EMPRESA | INSERT EMPRESAS GAS
----------------------------
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('20323','INGENIERIA Y OBRAS  SOCIEDAD ANONIMA EMPRESA DE SERVICIOS PUBLICOS','900007543','2');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('618','ALCANOS DE COLOMBIA S.A. E.S.P.','891101577','2');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('536','CELSIA COLOMBIA S.A. E.S.P.','800249860','2');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('44278','CELSIA TOLIMA S.A. E.S.P.','901280981','2');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('8888','CHEVRON PETROLEUM COMPANY','860005223','2');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('3151','DINAGAS S.A. E.S.P.','830055402','2');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('3206','ECOPETROL S.A.','899999068','2');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('1887','EFIGAS GAS NATURAL S.A E.S.P ','800202395','2');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('597','EMGESA S.A. E.S.P.','860063875','2');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('3370','EMPRESA DE ENERGIA DE CASANARE SA ESP','844004576','2');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('564','EMPRESAS PÚBLICAS DE MEDELLIN E.S.P.','890904996','2');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('3326','ESPIGAS S.A. E.S.P.','804014885','2');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('20256','E2 ENERGIA EFICIENTE S.A. E.S.P.','802025052','2');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('2225','GAS NATURAL CUNDIBOYACENSE SA ESP','830045472','2');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('525','GAS NATURAL DEL CESAR S.A. EMPRESA DE SERVICIOS PUBLICOS','804000551','2');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('526','GAS NATURAL DEL ORIENTE SA ESP','890205952','2');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('3181','GAS Y ELECTRICIDAD S.A. E.S.P.','830102340','2');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('978','GASES DE LA GUAJIRA S.A., EMPRESA DE SERVICIOS PUBLICOS','892115036','2');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('629','GASES DE OCCIDENTE S. A. EMPRESA DE SERVICIOS PUBLICOS','800167643','2');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('484','GASES DEL CARIBE S.A. EMPRESA DE SERVICIOS PUBLICOS ','890101691','2');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('541','GASES DEL CUSIANA S.A. E.S.P','800218682','2');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('620','GASES DEL LLANO S.A EMPRESA DE SERVICIOS PUBLICOS','800021272','2');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('1302','GASES DEL ORIENTE S.A.  EMPRESA DE SERVICIOS PUBLICOS DOMICILIARIOS','890503900','2');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('1601','GASES DEL SUR DE SANTANDER S.A. E.S.P.','804002801','2');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('480','ISAGEN S.A. E.S.P.','811000740','2');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('2097','MADIGAS INGENIEROS S.A. E.S.P.','822001073','2');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('1173','METROGAS DE COLOMBIA S.A. E.S.P. ','890208316','2');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('3359','NACIONAL DE SERVICIOS PÚBLICOS DOMICILIARIOS S.A. E.S.P.','830118416','2');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('513','PLEXA SAS ESP','860515802','2');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('3268','PRIME TERMOFLORES S.AS E.S.P.','830113630','2');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('3325','PROMESA S.A. ESP','804014818','2');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('1069','PROMIGAS S.A. E.S.P.','890105526','2');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('527','PROMIORIENTE S.A. E.S.P.','800226766','2');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('1626','PROMOTORA DE GASES DEL SUR S.A. E.S.P.','800170118','2');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('3227','PROMOTORA DE SERVICIOS PÚBLICOS S.A. E.S.P.','804013578','2');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('498','SURTIDORA DE GAS DEL CARIBE S.A. EMPRESA DE SERVICIOS PUBLICOS ','890400869','2');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('485','TERMOBARRANQUILLA S.A. E.S.P.','800245746','2');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('2261','TERMOCANDELARIA SOCIEDAD EN COMANDITA POR ACCIONES EMPRESA DE SERVICIOS PUBLICOS','806005008','2');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('1077','TERMOEMCALI  I  S.A. ESP','800253702','2');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('2264','TRANSOCCIDENTE S.A . E.S.P.','805010599','2');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('481','TRANSPORTADORA DE METANO E.S.P. S.A.','800215347','2');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('488','VANTI S.A. ESP','800007813','2');

----------------------------
-- DML TABLA EMPRESA | INSERT EMPRESAS GLP
----------------------------
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('1635','ALMACENADORA DE GASES DE APIAY S.A. ESP','800125495','3');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('572','ALMALLANO S.A. ESP','800176319','3');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('1171','ALMANSILLA  S.A. E.S.P.','860352913','3');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('2411','ANDIGAS S.A. E.S.P.','830029189','3');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('1792','AYAPEGAS S.A E.S.P','812002285','3');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('696','CARTAGAS S.A EMPRESA DE SERVICIOS PUBLICOS DOMICILIARIOS','800074692','3');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('20497','CATENA MANOA  SA ESP','830108459','3');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('44278','CELSIA TOLIMA S.A. E.S.P.','901280981','3');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('1638','COMPAÑIA DE ALMACENAMIENTO DE GAS S.A. ESP','860508892','3');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('3358','COMPAÑIA DE SERVICIOS PUBLICOS S.A E.S.P','830130648','3');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('3375','COMPAÑIA ENVASADORA NACIONAL DE GAS S.A ESP','832009598','3');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('1604','DISTRIBUIDORA CENTRAL DE GAS SA ESP','830046209','3');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('2923','DISTRIBUIDORA DE GAS MONZAGAS S.A. E.S.P.','834001051','3');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('3206','ECOPETROL S.A.','899999068','3');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('1564','ELECTROGAS SA ESP','891400900','3');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('3336','EMPRESA COLOMBIANA DE SERVICIOS PUBLICOS ','804014241','3');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('3012','EMPRESA DE GAS DEL PUTUMAYO SA ESP','846001218','3');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('1414','ENERGAS S.A. EMPRESA DE SERVICIOS PUBLICOS DOMICILIARIOS - ENERGAS SA  ESP','800182395','3');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('1195','ENVASADORA DE GAS DE PUERTO SALGAR S.A. EMPRESA DE SERVICIOS PUBLICOS','890701766','3');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('1600','GAS CAMARGO S.A. E.S.P','829001116','3');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('2180','GAS CAQUETA S.A  E.S.P','828000499','3');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('508','GAS CUNDINAMARCA SOCIEDAD ANONIMA EMPRESA DE SERVICIOS PUBLICOS','800082964','3');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('2308','GAS DEL PAEZ S.A. E.S.P.','817001685','3');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('20242','GAS EL PUENTE SOCIEDAD ANONIMA EMPRESA DE SERVICIOS PUBLICOS','830138744','3');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('1715','GAS EL SOL S.A. E.S.P.','800150534','3');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('2021','GAS GOMBEL S.A. E.S.P.','830021307','3');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('1801','GAS GUAVIARE S.A. E.S.P.','800136258','3');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('1643','GAS LICUADO DEL PETROLEO NORANTIOAQUIA S.A.E.S.P.','800208653','3');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('1598','GAS NEIVA S.A. E.S.P.','813002696','3');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('621','GAS ROSARIO S.A EMPRESA DE SERVICIOS PUBLICOS DOMICILIARIOS ','890503603','3');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('2232','GAS SANTA ROSA DEL SUR S.A. E.S.A.','804004965','3');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('20357','GAS SERRANIA S.A. E.S.P.','900022244','3');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('1545','GAS SUMAPAZ S.A. E.S.P.','860450098','3');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('3181','GAS Y ELECTRICIDAD S.A. E.S.P.','830102340','3');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('976','GAS ZIPA SAS  ESP','860026070','3');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('1595','GASES DEL CAGUAN S. A. E.S.P.','828000578','3');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('1623','GASES DEL CESAR S.A. -E.S.P.','892300026','3');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('1601','GASES DEL SUR DE SANTANDER S.A. E.S.P.','804002801','3');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('1330','GRANADOS GOMEZ Y CIA S.A. E.S.P.','891800082','3');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('1713','INTERMUNICIPAL DE GAS S.A. E.S.P.','890600185','3');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('3080','LA LLAMA OLÍMPICA S.A, E.S.P.','822004727','3');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('1854','LIDAGAS S.A E.S.P.','891300973','3');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('1681','LUSTRIGAS S.A EMPRESA DE SERVICIOS PUBLICOS','890503966','3');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('6026','MONTAGAS S.A. EMPRESA DE SERVICIOS PÚBLICOS DOMICILIARIOS MONTAGAS SA E S P.','891202203','3');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('1249','MOREGAS S.A. E.S.P.','807004443','3');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('3359','NACIONAL DE SERVICIOS PÚBLICOS DOMICILIARIOS S.A. E.S.P.','830118416','3');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('522','NORTESANTANDEREANA DE GAS S.A. E.S.P.','890500726','3');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('499','PEPEGAS S.A. E.S.P.','806004866','3');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('513','PLEXA SAS ESP','860515802','3');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('496','PORTOGAS S.A. E.S.P.','890402583','3');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('3227','PROMOTORA DE SERVICIOS PÚBLICOS S.A. E.S.P.','804013578','3');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('2634','PROVEEDORA MAYORISTA DE GAS S.A. E.S.P.','830055609','3');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('543','PROVIGAS S.A.S.  E.S.P.','827000149','3');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('1622','RAPIGAS S.A. E.S.P.','806001988','3');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('1634','RAYOGAS S.A. ESP','860033633','3');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('1420','SAN ANDRES GAS S.A. E.S.P.','892400417','3');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('1656','SODIGAS S.A EMPRESA DE SERVICIOS PUBLICOS - EN LIQUIDACION','890200805','3');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('2676','SUPERGAS DE NARIÑO S.A. E.S.P.','814003050','3');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('2277','ULTRAGAS S.A ESP','830043456','3');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('1855','VELOGAS DE OCCIDENTE S.A. E.S.P.','805003583','3');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('1115','VELOGAS S.A.  E.S.P.','800166132','3');
Insert into EMPRESA (IDEMPRESA,NOMBRE,NIT,SERVICIO) values ('1714','VILLA GAS S.A. E.S.P.','860025611','3');
