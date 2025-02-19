#Importando SMTPLIB libreria para enviar correos electronicos
#Utilizando SMTP(Simple Mail Transfer Protocol) para enviar correos electronicos
import smtplib
#Importando MIMEText para crear el contenido del correo en formato de texto
from email.mime.text import MIMEText
#Definiendo una función llamada "send_email" que toma dos parámetros: 
#subject (asunto) y body (cuerpo del correo).
def send_email(subject, body):
    # Definiedo las variables "me", "password" y "you"
    me = "stylehaven1024@gmail.com"  # "me" que seria el Correo del remitente
    password = "fosv yima bfmr rnyx"  #Contraseña de aplicacion generada por gmail
    you = "stylehaven1024@gmail.com"  # "you" Correo del destinatario

    # Crear el mensaje
    #body y subject es texto
    msg = MIMEText(body) # Crear el contenido del mensaje con el cuerpo del correo
    msg['From'] = me # Establecer el remitente del correo
    msg['To'] = you # Establecer el destinatario del correo
    msg['Subject'] = subject # Establecer el asunto del correo

    # Enviar el mensaje a través del servidor SMTP de Gmail
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        # Conectar al servidor SMTP de Gmail en el puerto 587
        # Puerto 587 es el puerto estandar para enviar correos electronicos ultilizando SMTP
        server.starttls() # Iniciar la conexión TLS (Transport Layer Security)
        server.login(me, password) # Iniciar sesión en el servidor SMTP con el correo y la contraseña
        server.sendmail(me, you, msg.as_string()) # Enviar el correo Como TEXTO
        server.quit()  # Cerrar la conexión con el servidor SMTP
        print("Correo enviado exitosamente")#Solo para ver en consola si se envio el correo
    except Exception as e:
        print(f"Error al enviar el correo: {e}")
