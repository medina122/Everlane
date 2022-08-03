### Hecho el 02/08/2008 por SyntaxErr0r ###
import random
from pg_bot import PyAutoGUI_Bot
from funciones import generar_identidad, telegram, separar_cc, crear_lista

# Variables y Objetos

bot = PyAutoGUI_Bot()
url = 'https://www.everlane.com/products/unisex-diamond-stitch-sock-lavender'

# Funciones

def preparar_worksplace():

    if bot.locate('everlane', click=False) == True or bot.locate('payment_method') == True: 
        print('Usando el entorno de trabajo actual')    

    else:
        print('Preparando entorno de trabajo')
        # Necesitamos hacer que abra el Navegador, por defecto: chrome

        bot.press('win')
        bot.pause(0.2)
        bot.write('chrome')
        bot.pause(0.2)
        bot.press('enter')

        # Abrimos Everlane

        bot.pause(1)
        bot.press_both('ctrl', 'l')
        bot.copypaste(url)
        bot.press('enter')

        # Ponemos una pausa por si encontramos cualquier popup

        bot.pause(3)

        if bot.get_position('get_early_access') != None:
            bot.locate('no_thanks')

        bot.locate('sock', check=True, click=False)
        bot.scroll(-200)
        bot.locate('talla_M', wait=0.5) or bot.locate('talla_L')
        bot.locate('agregar_carrito', wait=0.5)
        bot.locate('your_cart', check=True, click=False)
        bot.locate('checkout')

        # Llenamos los datos de forma random y vamos haciendo scroll
        id = generar_identidad()

        bot.locate('enter_email', check=True, click=False)
        bot.locate('email_address')
        bot.write(id[2])
        bot.locate('continue_to_shipping', wait=0.1) or bot.press('enter')
        bot.scroll(-200)
        bot.locate('shipping', check=True, click=False)
        bot.locate('full_name', wait=0.3)
        print('Nombre')
        bot.pause(0.05)
        bot.write(f"{id[0]} {id[1]}")
        bot.press('tab') # Saltamos la casilla de Full Name
        bot.press('tab') # Saltamos la casilla de Country
        bot.pause(0.05)
        print('Direccion')
        bot.write(str(random.randint(1500,1700)))
        bot.press('tab') # Saltamos la casilla de Street Address
        bot.press('tab') # Saltamos la casilla de Apartment
        bot.press('tab') # Saltamos la casilla de PO Box
        bot.pause(0.05)
        print('Ciudad')
        bot.write('Doral')
        bot.press('tab') # Saltamos la casilla de City
        bot.write('fl')
        bot.pause(0.05)
        print('Estado')
        bot.press('enter')
        bot.press('tab') # Saltamos la casilla de State
        bot.pause(0.05)
        print('Zip Code')
        bot.write('33191')
        bot.press('tab') # Saltamos la casilla de Zip Code
        bot.press('tab') # Saltamos la casilla de Phone Number
        bot.pause(0.05)
        bot.scroll(-300)
        bot.locate('see_shipping_options', 1)
        bot.locate('select_shipping_option', check=True, click=False)
        bot.locate('continue_to_payment', wait=0.5) or bot.press('enter')
        bot.pause(0.20)
        bot.scroll(-500)

def livear(cc_namso):
    print(f"Current: {cc_namso}")
    cc = separar_cc(cc_namso)

    if bot.locate('cc'):
        bot.pause(0.2)
        print(f'CC: {cc[0]}')
        bot.write(cc[0])
        bot.pause(0.2)
        bot.write(cc[1])

        bot.pause(0.2)
        print(f"MMYY: {cc[1]}/{cc[2][2:4]}")
        bot.write(cc[2][2:4])

        bot.pause(0.2)
        print(f"CVC: {cc[3]}")
        bot.write(cc[3])

        bot.pause(0.2)
        bot.locate('credit_card')
        bot.scroll(-500)
        bot.pause(1.5)
        bot.locate('review_order', check=True)

        bot.pause(1)
        bot.locate('place_order')

    elif bot.locate('payment_method', click=False) or bot.locate('credit_card', click=False):

        # Si encontramos el boton de editar o cerrar
        bot.locate('edit') or bot.locate('close')
        bot.pause(1)

        # Obtenemos la posicion de credit card (Boton Azul)
        # Para poder mover el raton de forma relativa sobre esa posicion
        bot.locate('credit_card', check=True, click=False)
        credit_card = bot.get_position('credit_card')
        
        # Seleccionamos y escribimos la CC
        bot.move(credit_card[0]+100, credit_card[1]+66, click=True)
        bot.pause(0.5)
        bot.press_both('ctrl', 'a')
        bot.pause(0.5)
        print(f'CC: {cc[0]}')
        bot.copypaste(cc[0])

        # Seleccionamos y escribimos el MMYY
        if bot.locate('mmyy',wait=0.2):
            bot.pause(1)
        
        else:
            print('Corriendo ELSE MMYY')
            bot.move(credit_card[0]+293, credit_card[1]+66, click=True)
            bot.pause(0.5)
            bot.press_both('ctrl', 'a')
            bot.pause(0.5)

        print(f"MMYY: {cc[1]}/{cc[2][2:4]}")
        bot.copypaste(cc[1])
        bot.copypaste(cc[2][2:4])

        # Seleccionamos el CVC

        if bot.locate('cvv'):
            pass
        else:
            print('Corriendo ELSE CVC')
            bot.move(credit_card[0]+447, credit_card[1]+66, click=True)
            bot.pause(0.5)
            bot.press_both('ctrl', 'a')
            bot.pause(0.5)

        print(f"CVC: {cc[3]}")
        bot.copypaste(cc[3])
        bot.pause(1)

        # Hacemos click en credit card seguido de un scroll
        bot.press('enter')
        bot.pause(0.2)
        bot.press('end')
        bot.pause(0.5)
        
        if bot.locate('review_order'):
            pass
        else: 
            bot.locate('review_order', check=True)

        bot.locate('place_order', wait=1)

    # Validamos si fue success o failed

    bot.pause(5)

    if bot.locate('thanks', click=False) or bot.locate('live', click=False) or bot.locate('survey', click=False):
        print(f'CC: {cc} - Live!')
        bot.press_both('ctrl', 'l')
        bot.copypaste('chrome://settings/clearBrowserData')
        bot.press('enter')
        bot.locate('clear_data')
        bot.pause(0.10)
        bot.press_both('alt', 'f4')

        preparar_worksplace()

    elif bot.locate('error1', click=False):
        print('There was a problem processing your card. Please call your card issuer or try a different card.')

    
# Logica

def main():

    ccs = """
5217295329274181|11|2023|277
5217295329252583|11|2023|824
5217295329245041|11|2023|330
5217295329212850|11|2023|642
5217295329201127|11|2023|772
    """

    preparar_worksplace()

    cc_for_use = crear_lista(ccs)

    for cc in cc_for_use:
        
        livear(cc)
        
if __name__ == '__main__':

    try: 

        main() # Arreglos

    except KeyboardInterrupt:
        exit()

    


