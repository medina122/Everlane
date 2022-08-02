import random, colorama, requests
from colorama import Fore

# Enviar mensajes a Telegram

colorama.init()

def telegram(txt): # Cambiar chat id
    chatid = ''
    url = f'https://api.telegram.org/bot1759121577:AAHVHZMjB8cFkxzflzcJbNz1C4vLecxzOrg/sendMessage?chat_id={chatid}&text={txt}'
    requests.post(url)
    print(f"{Fore.GREEN}[Telegram] {Fore.WHITE} Message has been sent! ")

# Generar identidad nueva

nombres = ['Daniel', 'Claudia', 'Jose', 'Gustavo', 'Luis', 'John', 'Eduardo', 'Cristian', 'Alex', 'Angel', 'Henry', 'Alberto', 'Luz', 'Rosario', 'Sonia', 'Carlos', 'Maria', 'Cesar', 'Rafaek', 'Karla', 'Ronald', 'Karen', 'Leandro', 'Tony', 'Angel', 'Antonio', 'Miguel', 'Edgar', 'Manuel', 'Elizabeth', 'Victor', 'Hugo', 'David', 'William', 'Martin', 'Milagros', 'Marcos', 'Enrique', 'Ricardo', 'Steven', 'Jackson', 'Adrian', 'Alejandro', 'Gabriel', 'Nelson', 'Alexander']
apellidos = ['Garcia', 'Ferreira' ,'Rodriguez', 'Lopez', 'Martinez', 'Sanchez', 'Gonzalez', 'Hernandez', 'Diaz', 'Gomez', 'Alvarez', 'Torres', 'Ramirez', 'Flores', 'Sanz', 'Perez', 'Jimenez', 'Ruiz', 'Millan', 'Peña', 'Gutierrez', 'Vasquez', 'Guevara', 'Quispe', 'Rojas', 'Ramos', 'Mendoza', 'Castillo', 'Castro', 'Romero', 'Reyes', 'Leon', 'Espinoza', 'Fernandez', 'Calderon', 'Muñoz', 'Olivos', 'Larez', 'Gomez', 'Madrid', 'Cortez', 'Zambrano', 'Cardona', 'Molina', 'Edgardo'] 
dominios = ['@gmail.com', '@outlook.com', '@hotmail.com']

def generar_identidad():
    nombre = random.choice(nombres)
    apellido = random.choice(apellidos)
    email = nombre + apellido + str(random.randint(1,99)) + random.choice(dominios)
    return nombre, apellido, email
