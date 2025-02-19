##########INTEGRANTES#######
#Caso Cuba Jhordi
#Chávez Lozano Abigail
#Haro Sanchez Alexander
############################
from flask import Flask, render_template, redirect, url_for, request #REQUEST DE LA PROPIA LIBRERIA DE FLASK
#Importa la funcion send_email de el archivo "send_email.py"
from send_email import send_email as send_email_function
#Crear la variable app para llamar al name
app=Flask(__name__)
#Cargar el servidor
#Define la RUTA RAIZ (/) y la funcion INDEX que renderiza la plantilla INDEX.HTML 
@app.route('/')
def index():
    return render_template('index.html')

#Define la RUTA (/productos) y la funcion "productos" que renderiza la plantilla PRODUCTOS.html
@app.route('/servicios')
def productos():
    return render_template('servicios.html')

#Define la Ruta (/somos) y la funcion "somos" que renderiza la plantilla SOMOS.html
@app.route('/nosotros') 
def somos():
    return render_template('nosotros.html')

#Define la Ruta (/contactos) y la funcion "contactos" que renderiza la plantilla CONTACTOS.html
@app.route('/contactos') 
def contactos():
    return render_template('contactos.html')

#Define la Ruta (/historia) y la funcion "historia" que renderiza la plantilla HISTORIA.html
@app.route('/historia') 
def historia():
    return render_template('historia.html')

#Define la Ruta (/send-email) y la funcion "send_email"
#La RUTA SEND-EMAIL UTILIZA EL METODO HTTP POST
@app.route('/send-email', methods=['POST']) #POST se utiliza para enviar datos al servidor
#Definiendo la función "send_email" que maneja las solicitudes a la ruta /send-email
def send_email():
    if request.method == 'POST':
        #Todo jala de "NAME" en CONTACTOS.HTML
        nombre_cliente = request.form['nombreCliente']
        apelido_cliente = request.form['apellidoCliente']
        email = request.form['email']
        #subject es ASUNTO de los correos(TEXTO)
        subject = "Mensaje de: " + nombre_cliente + " " + apelido_cliente + " | Correo: " + email 
        #BODY cuerpo del mensaje
        body = request.form['mensaje']
        #Llamando a la funcion "send_email_function" Importada de "send_email.py"
        send_email_function(subject, body)
    #Redirecciona a la ruta "contactos"
    return redirect(url_for('contactos'))
if __name__ == '__main__':
    app.run(debug=True,port=8001)
    
##########INTEGRANTES#######
############################
#Caso Cuba Jhordi
#Chávez Lozano Abigail
#Haro Sanchez Alexander
############################
 
 
 
 
 
    