import pandas as pd

class Valores():
    def __init__(self):
        self.dados = {
            'Cartão': [],
            'Valor': []
        }
    
    def adicionar_cartao(self, cartao):
        self.dados['Cartão'].append(cartao)

    def adicionar_valor(self, valor):
        self.dados['Valor'].append(valor) 

    def salvar(self):
        df = pd.DataFrame(self.dados)
        df.to_excel('Cartões.xlsx', index=False)

