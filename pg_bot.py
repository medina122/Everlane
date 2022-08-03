import pyautogui as pg
import os, time, pyperclip
import colorama
from colorama import Fore

# En esta ocasion no randomizaremos la duracion y el movimiento
# Fecha: 02/08/2022

class PyAutoGUI_Bot():

    # Inicializamos Colorama para agregar colores a los print
    colorama.init()

    # Establecemos la pausa a 0         
    pg.PAUSE = 0.10
    
    # Asignamos las variables que necesitaremos
    def __init__(self):
        self.cords = None
        self.conf = 0.7
        self.path = os.getcwd()
        self.size = pg.size()

    # Ubicamos imagenes en pantalla y realizamos acciones en consecuencia
    def locate(self, name, check=False, wait=0, move=False, click=True):
        
        # Inicio retardado si es diferente a 0
        if wait != 0: time.sleep(wait)
        
        # Establecemos la carpeta de los recursos, por defecto 
        path = os.path.join(self.path, 'src', name)+'.png'
        self.cords = pg.locateOnScreen(path, self.conf)
        count = 0
        
        # Si tenemos check buscara la imagen en bucle
        while not self.cords and check:
            count +=1
            time.sleep(0.2)
            print(f"{Fore.YELLOW}[...]{Fore.WHITE} Trying to locate {name}, attempt: {count}")
            self.cords = pg.locateOnScreen(path, self.conf) 

        # Si encuentra la imagen realizara las acciones que se le indique
        if self.cords != None:
            print(f"{Fore.GREEN}[+]{Fore.WHITE} Found {name} at {self.cords}")

            # Para simular comportamiento humano agregaremos lo siguiente:
            if move: pg.moveTo(self.cords)
            if click: pg.click(self.cords)
            return True
        
        # Si no encuentra nada, retornara False
        else:
            print(f"{Fore.RED}[-]{Fore.WHITE} Not found {name}") 
            return False
    
    # Obtenemos la posicion de una imagen
    def get_position(self, name):
        path = os.path.join(self.path, 'src', name)+'.png'
        return pg.locateOnScreen(path, self.conf)
    
    def press(self, key):
        time.sleep(0.1)
        pg.press(key)

    def press_both(self, key1, key2):
        pg.hotkey(key1, key2)

    def scroll(self, clicks):
        pg.scroll(clicks)
    
    def write(self, content):
        pg.typewrite(content, interval=0.04)
    
    def pause(self, interval):
        time.sleep(interval)

    def move(self, x, y, click=False):
        pg.moveTo(x, y)
        if click: pg.click()

    def click(self):
        pg.click()
    
    def copypaste(self, text:str):
        pyperclip.copy(text)
        pg.hotkey('ctrl', 'v')
    