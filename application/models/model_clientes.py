import config as config # importa el archivo config

db = config.db # crea un objeto db del objeto db creado en config

'''
Metodo para seleccionar todos los registros de la tabla clientes
'''
def select_clientes():
    try:
        return db.select('clientes') # Selecciona todos los registros de la tabla clientes
    except Exception as e:
        print "Model select_clientes Error {}".format(e.args)
        print "Model select_clientes Message {}".format(e.message)
        return None

'''
Metodo para seleccionar un registro que coincida con el nombre dado
'''
def select_nombre(nombre_cliente):
    try:
        return db.select('clientes',where='nombre_cliente=$nombre_cliente', vars=locals())[0] # selecciona el primer registro que coincida con el nombre
    except Exception as e:
        print "Model select_nombre Error {}".format(e.args)
        print "Model select_nombre Message {}".format(e.message)
        return None

'''
Metodo para insertar un nuevo registro
'''
def insert_clientes(nombre_cliente,apellido_paterno,apellido_materno,telefono,email):
    try:
        return db.insert('clientes', nombre_cliente=nombre_cliente,apellido_paterno=apellido_paterno,apellido_materno=apellido_materno,telefono=telefono,email=email) # inserta un registro en clientes
    except Exception as e:
        print "Model insert_clientes Error {}".format(e.args)
        print "Model insert_clientes Message {}".format(e.message)
        return None

'''
Metodo para eliminar un registro que coincida con el nombre recibido
'''
def delete_clientes(nombre_cliente):
    try:
        return db.delete('clientes', where='nombre_cliente=$nombre_cliente',vars=locals()) # borra un registro de clientes
    except Exception as e:
        print "Model delete_clientes Error {}".format(e.args)
        print "Model delete_clientes Message {}".format(e.message)
        return None

'''
Metodo para actualizar o
'''
def update_clientes(nombre_cliente,apellido_paterno,apellido_materno,telefono,email): # actualiza los datos de la tabla 
    try:
        return db.update('clientes', 
            apellido_paterno=apellido_paterno, 
            apellido_materno=apellido_materno,
            telefono=telefono,
            email= email,
            where='nombre_cliente=$nombre_cliente',
            vars=locals())
    except Exception as e:
        print "Model update_clientes Error {}".format(e.args)
        print "Model update_clientes Message {}".format(e.message)
        return None

