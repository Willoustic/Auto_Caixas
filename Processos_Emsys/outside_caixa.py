import pyautogui as px
from time import sleep
import psutil as ps


def caminho_do_arquivo(posto_id):
    if posto_id == 1:
        caminho = 'NOVO H\\ZN MAIO\\REL'
    elif posto_id == 2:
        caminho = 'TRANSP\\ZS MAIO\\REL'
    elif posto_id == 3:
        caminho = 'VITORIA\\VITORIA MAIO\\REL'
    return caminho


def nome_do_posto(posto_name):
    if posto_name == 1:
        posto_nome = 'POSTO ZN'
    elif posto_name == 2:
        posto_nome = 'POSTO ZS'
    elif posto_name == 3:
        posto_nome = 'POSTO VITORIA'
    return posto_nome



class Emsys():
    def __init__(self):
        pass


    def abrir_programa(posto):
    #abrir programa:
        def is_app_running(app_name):
            for proc in ps.process_iter(['name']):
                if proc.info['name'] and app_name.lower() in proc.info['name'].lower():
                    return True
            return False
        
        verify = is_app_running('EMSys3.exe')

        if verify == True:
            # abrir o emsys
            px.click(655,745, duration=0.5)
            # clicar na janela
            px.click(654,693, duration=0.5)
            sleep(0.5)
        else:
            # abrir o emsys
            px.click(655,745, duration=0.5)
            sleep(25)
            # reaalizar o login
            px.write('carlos.w')
            sleep(1)
            px.press('tab')
            px.write('140309')
            sleep(1)
            px.press('enter')
            sleep(10)
            px.write(str(posto))
            sleep(1)
            px.press('enter')
            sleep(15)

        return True


    def abrir_fechamento():
        px.hotkey('altleft')
        sleep(0.5)
        px.write('Y2')
        sleep(0.5)
        px.write('Y06')
        sleep(0.5)
        px.write('Y08')
        sleep(5)


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
        sleep(5)
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
            posto_nome = nome_do_posto(posto_name=posto)
            caminho = caminho_do_arquivo(posto_id=posto)
            # abrir relatorio de demonstrativo em csv
            px.click()
            px.hotkey('altleft')
            px.write('Y2')
            sleep(0.2)
            px.write('Y09')
            sleep(0.2)
            sleep(0.2)
            px.write('Y1')
            px.write('Y09')
            sleep(10)
            # selecionar csv
            px.hotkey('shift', 'tab')
            sleep(0.5)
            px.write('csv')
            sleep(0.5)
            px.press('tab')
            sleep(0.5)
            px.press('enter')
            # gerar relatorio
            sleep(15)
            px.write(str(posto))
            px.press('enter')
            sleep(1)
            px.write(data)
            px.press('tab')
            px.press('tab')
            px.press('tab')
            px.press('enter')
            sleep(15)
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
            px.write(f'C:\\Users\\POSTO NH\\Desktop\\Carlos\\{caminho}\\{posto_nome} {data} rel')
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


    def fechamento_por_vendedor(posto, data):
        try:
            posto = int(posto)
        except:
            print('Numero de posto inválido')
        else:
            posto_nome = nome_do_posto(posto_name=posto)
            caminho = caminho_do_arquivo(posto_id=posto)
        
        px.click()
        px.hotkey('altleft')
        px.write('Y2')
        sleep(0.2)
        px.write('Y09')
        sleep(0.2)
        px.write('Y1')
        sleep(0.2)
        px.write('Y16')
        sleep(2)
        px.hotkey('shift', 'tab')
        sleep(1)
        px.write('csv')
        sleep(0.5)
        px.press('tab')
        px.press('enter')
        sleep(5)
        px.write(str(data))
        px.sleep(1)
        for i in range(0,3):
            px.press('tab')
        sleep(0.5)
        px.press('enter')
        sleep(5)
        px.write('vendas')
        sleep(0.5)
        px.press('tab')
        sleep(0.3)
        px.press('space')
        sleep(2)
        px.write(f'C:\\Users\\POSTO NH\\Desktop\\Carlos\\{caminho}\\{posto_nome} {data} vendas')
        sleep(0.5)
        px.press('enter')
        sleep(1)
        px.press('enter')
        sleep(1)
        px.click(846,230)
        sleep(1)

    
    def conferencia(data):
        px.click()
        # abrir a conferencia de encerrante
        px.hotkey('altleft')
        px.write('Y2')
        sleep(0.2)
        px.write('Y06')
        sleep(0.2)
        px.write('Y20')
        sleep(5)
        # digitar data
        px.click(405,187)
        sleep(0.5)
        px.write(str(data))
        sleep(1)
        px.click(542,184)
        sleep(1)
        px.write('y')
        sleep(30)
        px.click(1048,185)
        sleep(1)
        px.press('enter')
        sleep(10)
        px.press('enter')
        sleep(30)
        px.press('enter')
        sleep(1)
        px.click(1108,135)
        sleep(5)
