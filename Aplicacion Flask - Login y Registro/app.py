#Importamos las librerias
from flask import Flask, redirect, render_template, request, url_for, session
#Intanciar la aplicacion
app = Flask(__name__, template_folder='templates')

app.secret_key = 'your_secret_key'

#Array donde almacenaremos los datos
lista_clientes = []

# Variable global para almacenar el ID actual
current_id = 1

#Decorador para definir la ruta del inicio
@app.route('/')
def index():
    if 'logged_in' in session and session['logged_in']:
        return render_template('index.html', lista_clientes=lista_clientes)
    else:
        return redirect(url_for('login'))

#Decorador para definir la ruta del login
@app.route('/login')
def login():
    return render_template('login.html', lista_clientes = lista_clientes)

#Decorador para definir la ruta del registro
@app.route('/registro')
def registro():
    if 'logged_in' in session and session['logged_in']:
        return render_template('registro.html', lista_clientes = lista_clientes)
    else:
        return redirect(url_for('login'))

#Controlador de la ruta de envio de datos
@app.route('/enviar', methods=['POST'])                             
def enviar():                                                       #crea la funcion enviar
    if request.method == 'POST':                                    #Condicion que solicita que el metodo sea igual a post
        nombre_usuario = request.form['nombre_usuario']             #Extrae los datos ingresados en el input de la descripcion del usuario
        email_usuario = request.form['email_usuario']               #Extrae los datos ingresados en el input del correo electronico
        contrasenia_usuario = request.form['contrasenia_usuario']   #Extrae los datos ingresados en el input de la contraseña
        Contagio_Covid = request.form['Contagio_Covid']                #Extrae los datos ingresados en el listado del estado de COVID
        #Crea la condicion de que no guarde el registro cuando el campo de la tarea y el del correo estan vacios
        if nombre_usuario == '' or email_usuario == '' or contrasenia_usuario == '' or Contagio_Covid == '':            
            return redirect(url_for('registro'))                       
        else:
            #Agrega a la lista los campos llenos
            global current_id
            lista_clientes.append({'id': current_id, 'nombre_usuario': nombre_usuario, 'email_usuario': email_usuario, 'contrasenia_usuario': contrasenia_usuario, 'Contagio_Covid': Contagio_Covid})
            current_id += 1
            return redirect(url_for('index'))

#Controlador de la ruta de comparacion de datos
@app.route('/ingresar', methods=['POST'])
def ingresar():
    if request.method == 'POST':
        nombre_usuario = request.form['nombre_usuario']
        email_usuario = request.form['email_usuario']
        contrasenia_usuario = request.form['contrasenia_usuario']
        
        # Check if login credentials are valid (replace with your own logic)
        if nombre_usuario == 'admin' and email_usuario == 'admin@example.com' and contrasenia_usuario == 'password':
            # Start a session and store the logged-in user
            session['logged_in'] = True
            session['nombre_usuario'] = nombre_usuario
            return redirect(url_for('index'))
        else:
            return redirect(url_for('login'))


#Controlador de la ruta para borrar los datos de la tabla
@app.route('/borrar', methods=['POST'])
def borrar():                                                       #Crea la funcion de borrar la lista creada
    if request.method == 'POST':                                    #solicita al metodo post
        if lista_clientes == []:                                    #crea la condicional de la lista vacia
            return redirect(url_for('index'))                       #Si la lista esta vacia ejecuta el index
        else:
            lista_clientes.clear()                                  #Elimina toda la lista
            return redirect(url_for('index'))                       #Ejecuta el index
        
#Controlador para borrar por id
@app.route('/borrar/<int:id>', methods=['POST'])
def eliminar(id):
    if request.method == 'POST':
        global lista_clientes
        lista_clientes = [usuario for usuario in lista_clientes if usuario['id'] != id]
        return redirect(url_for('index'))
    
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

#main del programa
if __name__ == '__main__':
    app.run(debug=True)     #debug para reiniciar el servidor