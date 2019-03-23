import web
import config as config


class Insert:
    def __init__(self):
        pass

    def GET(self):  
        return config.render.insert() # renderiza la pagina insert.html
    
    def POST(self):
        formulario = web.input() # almacena los datos del formulario
        nombre_cliente = formulario['nombre_cliente'] # alamcena el nombre escrito en el input
        apellido_paterno = formulario['apellido_paterno'] # almacena el apellido paterno escrito en el input
        apellido_materno = formulario['apellido_materno'] # alamcena el apellido materno escrito en el input
        telefono= formulario['telefono'] # almacena el telefono escrito en el input
        email = formulario['email'] # almacena el email  escrito en el input
        config.model_clientes.insert_clientes(nombre_cliente,apellido_paterno,apellido_materno,telefono,email) # llama al metodo insert_datos y le paso los datos guardados
        raise web.seeother('/') # redirecciona al index.html
