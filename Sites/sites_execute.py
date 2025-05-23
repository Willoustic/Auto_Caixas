import pyautogui as px
from sites import Site
from valores_cartões import Valores
from pyperclip import paste
import psutil as ps
from time import sleep

class Cartões:
    def __init__(self):
        def is_app_running(app_name):
            for proc in ps.process_iter(['name']):
                if proc.info['name'] and app_name.lower() in proc.info['name'].lower():
                    return True
            return False
        
        verificar = is_app_running('Chrome.exe')

        if verificar:
            # abrir o chrome
            px.click(477,736)
            sleep(0.7)
        else:
            px.click(477,736)
            sleep(2)
            px.click(680,415)
    
    def pesquisar(self, texto):
        px.hotkey('ctrl', 'f')
        px.write(texto)
        sleep(1)
        px.press('esc')
        sleep(1)
        px.press('enter')
        sleep(1)

    def pegar_relatorio_ctf_vitoria(self, data):
        site = Site.ctf()
        px.hotkey('ctrl', 'l')
        px.hotkey('ctrl', 'a')
        px.press('delete')
        px.write(site)
        px.press('enter')
        sleep(3)
        #clicar em login
        px.press('tab')
        sleep(1)
        px.hotkey('ctrl', 'a')
        # digitar o login
        px.write('POSTO018028')
        sleep(0.5)
        px.press('down')
        sleep(0.8)
        px.press('enter')
        sleep(1)
        # clicar no captcha
        for i in range(0, 3):
            px.press('tab')
            sleep(0.98)
        px.press('enter')
        sleep(3)
        # realizar login
        for i in range(0, 3):
            px.press('tab')
            sleep(0.98)
        px.press('enter')
        # esperar o abrir o site
        sleep(3)
        # clicar o relatorio
        self.pesquisar('Relatorio')
        # clicar em por abs
        self.pesquisar('por abastecimento')
        # clicar em por data
        
        self.pesquisar('por data')

        # esperar abrir
        sleep(2)

        # clique triplo no primeiro periodo
        px.tripleClick(155,423)

        # digitar a data
        px.write(data)

        # clique triplo no sgundo periodo
        px.tripleClick(342,429)

        # digitar a data
        px.write(data)
        # clicar para consultar do excel
        px.click(885,424)

        px.click(1082,506) # clicar em consultar

        sleep(7)

        px.click(1271,59) # clicar em downloads

        px.click(1109,152) # clicar para abrir a planilha

Cartões().pegar_relatorio_ctf_vitoria('19/05/2025')

