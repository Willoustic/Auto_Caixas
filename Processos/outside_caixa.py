import pyautogui as px
from time import sleep
import psutil as ps


class Emsys():
    def __init__(self):
        pass

    def abrir_programa():
    #abrir programa:
        def is_app_running(app_name):
            for proc in ps.process_iter(['name']):
                if proc.info['name'] and app_name.lower() in proc.info['name'].lower():
                    return True
            return False
        
        verify = is_app_running('EMSys3.exe')

        if verify == True:
            px.click(433,739, duration=0.5)
            px.click(439,651, duration=0.5)
            sleep(0.5)

        return True

    def abrir_fechamento():
        px.hotkey('altleft')
        sleep(0.5)
        px.write('Y2')
        sleep(0.5)
        px.write('Y06')
        sleep(0.5)
        px.write('Y08')
        sleep(10)

    def tirar_relatorio(posto, data):
        # abrir rel. vendas por forma de pgto.
        px.hotkey('altleft')
        px.write('Y2')
        sleep(0.2)
        px.write('Y04')
        sleep(0.2)
        px.write('Y16')
        sleep(0.2)
        px.write('Y17')
        sleep(1)
        # selecionar a data
        px.write(data)
        px.hotkey('tab')
        sleep(0.2)
        px.write(data)
        px.hotkey('tab')
        sleep(0.5)
        # desabilitar a caixinha 'apenas caixas confirmados'
        px.click(796,360, duration=0.2)
        sleep(0.5)
        # gerar relatorio
        px.press('enter')
        sleep(5)
        # clicar para imprimir
        px.click(12,50)
        sleep(1)
        # clicar ok
        px.click(803,409)
        sleep(3)
        # clicar em area de trabalho
        px.click(69,270)
        sleep(0.5)
        # clicar para nomear
        px.click(268,335)
        sleep(0.3)
        # digitar o nome
        px.write(f'{posto} {data}')
        sleep(0.3)
        #clicar em ok
        px.click(484,445)
        sleep(5)
        #só para tratar erros, caso já haja arquivo com esse nome!
        px.press('enter')
        sleep(0.5)
        px.press('esc')
        sleep(0.5)
        # fechar o rel.
        px.click(1344,13)
        sleep(0.9)
        # fechar o selecionador de data de vendas por forma de pgto.
        px.click(922,292)
        sleep(1)

    def demonstrativo_csv(posto, data):
        try:
            posto = int(posto)
        except:
            print('Numero de posto inválido')
        else:
        
            if posto == 1:
                posto_nome = 'Novo'
            elif posto == 2:
                posto_nome = 'Transportes'
            elif posto == 3:
                posto_nome = 'Vitória'
            # abrir relatorio de demonstrativo em csv
            px.hotkey('altleft')
            px.write('Y2')
            sleep(0.2)
            px.write('Y09')
            sleep(0.2)
            px.write('Y1')
            sleep(0.2)
            px.write('Y09')
            sleep(5)
            # selecionar csv
            px.hotkey('shift', 'tab')
            sleep(0.5)
            px.write('csv')
            sleep(0.5)
            px.press('tab')
            sleep(0.5)
            px.press('enter')
            # gerar relatorio
            sleep(10)
            px.write(str(posto))
            px.press('enter')
            sleep(0.4)
            px.write(data)
            px.press('tab')
            px.press('tab')
            px.press('tab')
            px.press('enter')
            sleep(20)
            # selecionar tipo de relatório
            px.write('venda')
            px.sleep(0.5)
            px.press('tab')
            sleep(0.5)
            px.press('space')
            px.sleep(1)
            # area de trabalho
            px.click(389,266)
            sleep(0.6)
            # clicar para digitar o nome
            px.click(662,490)
            sleep(0.6)
            px.write(f'posto {posto} {data} rel')
            sleep(0.6)
            # salvar
            px.click(950,495)
            sleep(0.6)
            # tirar o popup da tela
            px.press('enter')
            sleep(0.6)
            # clicar para sair
            px.click(844,231, duration=0.3)
            sleep(0.3)
