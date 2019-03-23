import web
'''
Parametros de configuracion para conectarse a una base de datos
MySQL o MariaDB
'''
db = web.database(
    dbn='mysql', # motor de base de datos
    host='localhost', # ruta del servidor
    db='ferreteria_egr', # nombre de la base de datos
    user='elle', # usuario dela base de datos
    pw='elle.2019', # password del usuario
    port = 3306 # puerto de mariadb
    )