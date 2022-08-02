### Hecho el 02/08/2008 por SyntaxErr0r ###
import random
from pg_bot import PyAutoGUI_Bot
from funciones import generar_identidad, telegram, separar_cc

# Variables y Objetos

bot = PyAutoGUI_Bot()
url = 'https://www.everlane.com/products/unisex-diamond-stitch-sock-lavender'

# Logica

# 1- Necesitamos hacer que abra el Navegador, por defecto: chrome

bot.press('win')
bot.write('chrome')
bot.press('enter')

# 2. Abrimos Everlane

bot.pause(1)
bot.press_both('ctrl', 'l')
bot.write(url)
bot.press('enter')

# Quitamos la casilla del 10% descuento

#bot.locate('descuento', check=True, click=False)
#bot.locate('descuento1', wait=1) or bot.locate('descuento2')

# Escogemos la Talla, agregamos al carrito y hacemos checkout
bot.locate('sock', wait=3, check=True, click=False)
bot.scroll(-200)
bot.locate('talla_M', wait=0.5) or bot.locate('talla_L')
bot.locate('agregar_carrito', wait=0.3)
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
bot.locate('full_name', wait=0.5)
print('Nombre')
bot.pause(0.10)
bot.write(f"{id[0]} {id[1]}")
bot.press('tab') # Saltamos la casilla de Full Name
bot.press('tab') # Saltamos la casilla de Country
bot.pause(0.10)
print('Direccion')
bot.write(str(random.randint(1500,1700)))
bot.press('tab') # Saltamos la casilla de Street Address
bot.press('tab') # Saltamos la casilla de Apartment
bot.press('tab') # Saltamos la casilla de PO Box
bot.pause(0.10)
print('Ciudad')
bot.write('Doral')
bot.press('tab') # Saltamos la casilla de City
bot.write('fl')
bot.pause(0.10)
print('Estado')
bot.press('enter')
bot.press('tab') # Saltamos la casilla de State
bot.pause(0.10)
print('Zip Code')
bot.write('33191')
bot.press('tab') # Saltamos la casilla de Zip Code
bot.press('tab') # Saltamos la casilla de Phone Number
bot.pause(0.10)
bot.scroll(-300)
bot.locate('see_shipping_options', 1)
bot.locate('select_shipping_option', check=True)
bot.locate('continue_to_payment', wait=0.5) or bot.press('enter')
bot.pause(0.20)
bot.scroll(-500)

# Ponemos la CC #

cc_namso = '5217295329264455|11|2023|458'
cc = separar_cc(cc_namso)

print(cc_namso)

bot.locate('cc')
bot.write(cc[0])
print('CC')

bot.write(cc[1])
print(f"CC: {cc[1]}")

bot.write(cc[2][2:4])
print(f"MMYY: {cc[1]}/{cc[2][2][2:4]}")

bot.write(cc[3])
print(f"CVC: {cc[3]}")
bot.pause(0.1)
bot.scroll(-500)

bot.locate('review_order')