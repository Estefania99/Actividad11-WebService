import web
import config as config


class Update:
    def __init__(self):
        pass

    def GET(self, nombre_cliente): 
        clientes = config.model_clientes.select_nombre(nombre_cliente) # Selecciona el registro que coincida con nombre
        return config.render.update(clientes) # Envia el registro y renderiza update.html
    
    def POST(self,clientes):
        formulario = web.input() # almacena los datos del formulario
        nombre_cliente = formulario['nombre_cliente'] # alamcena el nombre escrito en el input
        apellido_paterno = formulario['apellido_paterno'] # almacena el apellido paterno escrito en el input
        apellido_materno = formulario['apellido_materno'] # alamcena el apellido materno escrito en el input
        telefono= formulario['telefono'] # almacena el telefono escrito en el input
        email = formulario['email'] # almacena el email  escrito en el input
        config.model_clientes.update_clientes(nombre_cliente,apellido_paterno,apellido_materno,telefono,email) # llama al metodo insert_datos y le paso los datos guardados
        raise web.seeother('/') # redirecciona al index

    
   