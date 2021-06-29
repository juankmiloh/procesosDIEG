import os

DEBUG = True
PUBLIC = False
SQLALCHEMY_TRACK_MODIFICATIONS = False
# SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:1234@localhost:5432/procesos_dieg' # BD equipo local juan camilo produccion
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:1234@localhost:5432/procesos_dieg_prueba' # BD equipo local juan camilo pruebas
# SQLALCHEMY_DATABASE_URI = 'postgresql://procesos_dieg:SSPD2020*@172.16.32.13:5432/procesos_dieg' # BD produccion PC SSPD
# SQLALCHEMY_DATABASE_URI = 'postgresql://procesos_dieg:SSPD2020*@172.16.32.13:5432/procesos_dieg_pruebas' # BD pruebas PC SSPD
