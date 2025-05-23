from Processos_Emsys.inside_caixa import Caixa
from Processos_Emsys.outside_caixa import Emsys
from time import sleep

def mensagem(validation=True):
    if validation:
        print('')
        print('-=' * 20)
        print('Valores digitados incorretamente!')
        print('-=' * 20)
        print('')

    print('')
    print('-=' * 20)
    print('Exemplo:')
    print('-=' * 20)
    print('Digite o dia do fechamento: 01')
    print('Digite o mês do fechamento: 05')
    print('Código dos postos: \n[1] Novo Horizonte \n[2] Transportes \n[3] Vitória')
    print('-=' * 20)
    print('')

class Bot():
    def __init__(self, dia, mes, posto):
        while True:
            try:
                self.dia = dia
                self.mes = mes
                self.posto = posto
            except Exception:
                print(Exception)
            else:
                self.validation = True
                if len(self.dia) == 2:
                    if len(self.mes) == 2:
                        self.data = f'{self.dia}{self.mes}'
                        if self.posto == 1:
                            self.caixas = 12
                            break
                        elif self.posto == 2:
                            self.caixas = 3
                            break
                        elif self.posto == 3:
                            self.caixas = 10
                            break
                break


    def Fechamento_Inicial(self):
        if self.validation:
            Emsys.abrir_programa(posto=self.posto)
            Emsys.abrir_fechamento()
            Caixa.select_data(data=self.data)
            sleep(0.8)
            Caixa.salvar(self.caixas)
            Emsys.tirar_relatorio(posto=str(self.posto), data=self.data)
            Emsys.demonstrativo_csv(posto=str(self.posto), data=self.data)
            Emsys.fechamento_por_vendedor(posto=str(self.posto), data=self.data)
            Emsys.abrir_fechamento()
            sleep(3)
            Caixa.select_data(data=self.data)
            sleep(2.5)
            Caixa.excluir_especie(caixas=self.caixas)
            sleep(1)
            Caixa.voltar()
            sleep(5)
            Caixa.rateio(valor=self.caixas)
        
        print()
        print('-=' * 20)
        print('Programa de inicialização de verificação de caixas encerrado.')

    def Confirmamento(self):
        if self.validation:
            Emsys.abrir_programa(posto=self.posto)
            Emsys.abrir_fechamento()
            Caixa.select_data(data=self.data)
            Caixa.confirmar(caixas=self.caixas)
            Emsys.tirar_relatorio(posto=self.posto, data=self.data)
            Emsys.conferencia(data=self.data)
        print()
        print('-=' * 20)
        print('Programa de finalizamento de caixas encerrado.')


class App:
    def __init__(self):
        self.opcoes = [1, 2, 0]

    def menu(self):
        print("""ESCOLHA A OPÇÃO DESEJADA:
                  
[1] INICIAR A VERIFICAR UM CAIXA
[2] FINALIZAR OS CAIXAS
[0] ENCERRAR PROGRAMA                 
                                   """)
        
    def opcao_int(self, texto):
        try:
            opcao = int(input(texto))
        except:
            print('')
            print('=+' * 20)
            print('O valor digitado não é uma opção válida!')
            print('=+' * 20 )
            print('')
        else:
            if opcao in self.opcoes:
                return opcao

        
    def Programa(self):
        while True:
            try:        
                print('')
                self.menu()
                opcao = self.opcao_int('>>> ')
                if opcao == 1:
                    Bot().Fechamento_Inicial()
                elif opcao == 2:
                    Bot().Confirmamento()
                elif opcao == 0:
                    break
                else:
                    print('')
                    print('=+' * 20)
                    print('O valor digitado não é uma opção válida!')
                    print('=+' * 20 )
                    print('')        
            except KeyboardInterrupt:
                pass
            except Exception:
                pass
            else:
                if opcao == 0:
                    break
                           
            
        print('')
        print('=+' * 20)
        print('Programa finalizado'.center(40))
        print('=+' * 20 )
        print('')



