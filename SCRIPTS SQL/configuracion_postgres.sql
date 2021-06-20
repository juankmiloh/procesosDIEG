----------------------------
-- COMANDO PARA CREAR UNA BASE DE DATOS
----------------------------
1. sudo -i -u postgres -- Acceder al esquema por defecto 
2. postgres@1pc7-220-17741:~$ createdb procesos_dieg_pruebas -- Crear base de datos
3. postgres@1pc7-220-17741:~$ psql -d procesos_dieg_pruebas -- Acceder a la base de datos (utilizar BD)
4. procesos_dieg_pruebas=# \l -- Listar bases de datos
5. procesos_dieg_pruebas=# select * from rol; -- Hacer consulta a la BD 
6. procesos_dieg_pruebas=# \q -- Salir de la conexion de la BD