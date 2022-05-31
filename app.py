#Importamos las librerias
from flask import Flask, redirect, render_template, request, url_for
#Intanciar la aplicacion
app = Flask(__name__, template_folder='templates')

#Array donde almacenaremos los datos
lista_clientes = []

#Decorador para definir la ruta del inicio
@app.route('/')
def index():
    return render_template('index.html', lista_clientes = lista_clientes)

#Decorador para definir la ruta del login
@app.route('/login')
def login():
    return render_template('login.html', lista_clientes = lista_clientes)

#Decorador para definir la ruta del login
@app.route('/registro')
def registro():
    return render_template('registro.html', lista_clientes = lista_clientes)

#Controlador de la ruta de envio de datos
@app.route('/enviar', methods=['POST'])                             
def enviar():                                                       #crea la funcion enviar
    if request.method == 'POST':                                    #Condicion que solicita que el metodo sea igual a post
        nombre_usuario = request.form['nombre_usuario']   #Extrae los datos ingresados en el input de la descripcion del usuario
        email_usuario = request.form['email_usuario']                   #Extrae los datos ingresados en el input del correo electronico
        contrasenia_usuario = request.form['contrasenia_usuario']           #Extrae los datos ingresados en el input de la contraseña
        Contagio_Covid = request.form['Contagio_Covid']
        #Crea la condicion de que no guarde el registro cuando el campo de la tarea y el del correo estan vacios
        if nombre_usuario == '' or email_usuario == '' or contrasenia_usuario == '' or Contagio_Covid == '':            
            return redirect(url_for('login'))                       
        else:
            #Agrega a la lista los campos llenos
            lista_clientes.append({'nombre_usuario': nombre_usuario, 'email_usuario': email_usuario, 'contrasenia_usuario': contrasenia_usuario, 'Contagio_Covid': Contagio_Covid})
            return redirect(url_for('index'))

#Controlador de la ruta de envio de datos
@app.route('/ingresar', methods=['POST'])                             
def ingresar():                                                       #crea la funcion enviar
    if request.method == 'POST':                                    #Condicion que solicita que el metodo sea igual a post
        nombre_usuario = request.form['nombre_usuario']   #Extrae los datos ingresados en el input de la descripcion del usuario
        email_usuario = request.form['email_usuario']                   #Extrae los datos ingresados en el input del correo electronico
        contrasenia_usuario = request.form['contrasenia_usuario']           #Extrae los datos ingresados en el input de la contraseña
        #Crea la condicion de que no guarde el registro cuando el campo de la tarea y el del correo estan vacios
        if nombre_usuario == '' or email_usuario == '' or contrasenia_usuario == '' or lista_clientes == []:            
            return redirect(url_for('login'))                       
        else:
            #Agrega a la lista los campos llenos
            return redirect(url_for('index'))


#Controlador de la ruta para borrar los datos de la tabla
@app.route('/borrar', methods=['POST'])
def borrar():                                                       #Crea la funcion de borrar la lista creada
    if request.method == 'POST':                                    #solicita al metodo post
        if lista_clientes == []:                                    #crea la condicional de la lista vacia
            return redirect(url_for('index'))                       #Si la lista esta vacia ejecuta el index
        else:
            lista_clientes.clear()                                  #Elimina toda la lista
            return redirect(url_for('index'))                       #Ejecuta el index
        

#main del programa
if __name__ == '__main__':
    app.run(debug=True)     #debug para reiniciar el servidor