import tkinter as tk
from config_app import Bot

class Main_screen:
    def __init__(self):
        
        def commando(valor):
            posto = valor
            segunda_janela = Menu(posto_id=posto)
            segunda_janela.rodar()
              
        self.app = tk.Tk()
        self.app.title('Fechamento Automático')
        self.app.geometry('550x120')
        self.app.iconbitmap("C:\\Users\\davip\\Downloads\\App\\Projeto de Fechamento\\Projeto de Fechamento\\Projeto de Fechamento\\icon.ico")
        self.app.configure(background='black')

        texto = tk.Label(self.app, text='Fechamento de Caixas', bg='black', fg='white', font='Calibri, 20 italic' )
        texto.pack(padx=2, pady=2)

        self.frame_botoes = tk.Frame(self.app)
        self.frame_botoes.pack(pady=20)
        self.frame_botoes.configure(bg='black')

        self.fech_zn = tk.Button(self.frame_botoes, text=f"POSTO NOVO", bg='green', command=lambda: commando(1), width=18)
        self.fech_zn.pack(side='left', padx=20)
        
        self.fech_zs = tk.Button(self.frame_botoes, text=f"POSTO TRANSPORTES", bg='green', command=lambda: commando(2), width=18)
        self.fech_zs.pack(side='left', padx=20)

        self.fech_pv = tk.Button(self.frame_botoes, text=f"POSTO VITORIA", bg='green', command=lambda: commando(3), width=18)
        self.fech_pv.pack(side='left', padx=20)

    def rodar(self):
        self.app.mainloop()

class Menu:
    def __init__(self, posto_id):
        if posto_id == 1:
            self.nome_posto = 'Novo Horizonte'
        elif posto_id == 2:
            self.nome_posto = 'Transportes'
        elif posto_id == 3:
            self.nome_posto = 'Vitória'

        def data_format(event):
            data = self.data.get().replace('/', '')
            data = ''.join(filter(str.isdigit, data))[:8]

            nova_data = ""
            if len(data) >= 1:
                nova_data += data[:2]
            if len(data) >= 3:
                nova_data = data[:2] + '/' + data[2:4]

            if len(data) >= 5:
                nova_data = data[:2] + '/' + data[2:4] + '/' + data[4:]

            self.data.delete(0, tk.END)
            self.data.insert(0, nova_data)
        
        def comando(opcao):
            data = self.data.get()
            data = data.replace('/', '')
            dia = data[:2]
            mes = data[2:4]

            posto_auto = Bot(dia=dia, mes=mes, posto=posto_id)
            print(dia, mes, posto_id)
            if opcao == 1:
                posto_auto.Fechamento_Inicial()
            elif opcao == 2:
                posto_auto.Confirmamento()


        self.app_2 = tk.Toplevel()
        self.app_2.title(f'Posto {self.nome_posto}')
        self.app_2.configure(bg='black', highlightcolor='white')
        self.app_2.iconbitmap("C:\\Users\\davip\\Downloads\\App\\Projeto de Fechamento\\Projeto de Fechamento\\Projeto de Fechamento\\icon.ico")
        self.app_2.geometry('300x160')
        self.texto = tk.Label(self.app_2, text=f'Posto {self.nome_posto}', fg='green', font='Calibri, 18 italic', background='black')
        self.texto.pack(padx=10)
    
        self.data_label = tk.Label(self.app_2, text='Data do fechamento', bg='black', fg='white', font='Calibri, 10 italic')
        self.data_label.pack(padx=1, pady=1)

        self.data = tk.Entry(self.app_2, width=10)
        self.data.config(bg='white', fg='black', border='5')
        self.data.pack(padx=20, pady=1)
        self.data.bind("<KeyRelease>", data_format)

        self.frame = tk.Frame(self.app_2)
        self.frame.pack(pady=10)
        self.frame.configure(bg='black')

        self.inicial = tk.Button(self.frame, text=f"Inicialização", bg='green', command=lambda: comando(1), width=18)
        self.inicial.pack(side='left', padx=20)

        self.fech = tk.Button(self.frame, text=f"Finalização", bg='red', fg='white', command=lambda: comando(2), width=18)
        self.fech.pack(side='left', padx=20)

    def rodar(self):
        self.app_2.mainloop()
