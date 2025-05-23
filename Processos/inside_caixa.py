import pyautogui as px
from time import sleep
import pyperclip as pc

class Caixa():
    def select_data(data):
        # clicar na data
        px.click(961,184, duration=0.5)
        sleep(0.5)
        # digitar a data
        px.write(data)
        # pesquisar o caixa
        px.sleep(0.5)
        px.click(434,98, duration=0.5)
        sleep(0.5)


    def voltar():    
    # voltar todos os caixas
        px.click(574,101, duration=0.2)


    def salvar(valor):
        cont = 1
        print('Logs:')
        while cont <= valor:
            print(f'Fechando {cont}º Caixa')
            print('Salvar')
            px.click(356,114, duration=0)
            sleep(10)
            print('Clicando enter pra confirmar fechamento')
            px.press('enter')
            sleep(5)
            if cont < valor:
                print('proximo')
                px.click(645,100, duration=0.2)
                sleep(5)
            print('')
            print(f'{cont}º procedimento finalizado')
            print('=+' * 30)
            print('')
            cont += 1
    
        print('Todos os caixas Salvos')
        print('')
        #fechar o fechamento de caixas
        px.click(1037,65, duration=0.5)
        sleep(5)


    def excluir_especie(caixas):
        cont = 1
        while cont <= caixas:
            print("desbugar")
            px.click(370,131)

            print('clicar no + de recebimento')
            px.click(316,185, duration=0.5)
            sleep(0.5)

            print('clicar em especie')
            px.click(383,197, duration=0.5)
            sleep(0.5)

            print('clicar em excluir')
            px.click(679,163, duration=0.5)
            sleep(0.5)

            print('confirmar exclusão')   
            px.write('y')
            sleep(3)

            print('salvar')
            px.click(356,114, duration=0.5)
            sleep(5)

            print('clicar enter pra confirmar fechamento')
            px.press('enter')
            sleep(3)
            
            if cont < caixas:
                print('proximo')
                px.click(645,100, duration=0.5)
                sleep(10)

            print(f'{cont}º procedimento finalizado')
            print('=+' * 30)
            print('')
            cont += 1
        
        print('fim do funcionamento ')
        print('')


    def rateio(valor):
        cont = 1
        while cont <= valor:
            print("desbugar")
            px.doubleClick(357,132, duration=0.5)

            print("pegar usuário")
            px.doubleClick(645,182, duration=0.5)
            sleep(0.5)
            px.hotkey('ctrl', 'c')
            operador = pc.paste()
            print(f'operador: {operador}')
            sleep(0.2)

            print('clicar em responsaveis')
            px.click(372,198, duration=0.5) #responsaveis
            sleep(1)
            print("pegar rateio")
            px.doubleClick(828,652, duration=0.5)
            sleep(1)
            px.hotkey('ctrl', 'c')
            rateio = pc.paste()
            if rateio == '0':
                print('Rateio : 0,00')
            else:
                print(f'Rateio: {rateio}')
                sleep(1)
                print('clicar em incluir')
                px.click(549,164, duration=0.5) #incluir
                sleep(2)
                print('colocar op')
                #px.doubleClick(557,273, duration=1) #colocar op
                sleep(0.5)
                px.write(operador)
                px.press("enter")
                sleep(0.5)
                print('colocar valor rateio')
                px.doubleClick(894,327, duration=0.5) #colocar valor rateio
                sleep(0.5)
                px.write(rateio)
                sleep(0.5)
                print('incluir')
                px.click(472,217, duration=0.5) #incluir)
                sleep(3)
                print('fechar aba')
                px.click(890,184, duration=0.5) #fehcar aba)
                sleep(0.5)
            print('salvando')
            px.click(357,98, duration=0.5) #salvar
            sleep(5)
            px.press("enter")
            print('próximo')
            px.click(640,101, duration=0.2) # clicar pro proximo
            print(f'{cont}º operador: {operador} com rateio {rateio} finalizado')
            cont += 1
            sleep(3)
        # fechar o fechamento de caixas
        px.click(1037,65, duration=0.5)
        sleep(10)
        print('fim da execução!')
