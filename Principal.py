from contextlib import nullcontext
from datetime import date
import datetime
import tkinter
from tkinter import *
import conexao

from models.Dados_Planilha_1231 import Estacao1231
from models.Dados_Planilha_1232 import Estacao1232

try:
    class Principal():     

# Seleção da estação de consulta
        def executa(self):
            data1 = self.entry2.get()
            data2 = self.entry3.get()
            Nome_Arquivo = self.entry4.get()
            Nome_Salvar = self.entry5.get()
            estacao = self.rb_value.get()
            resultado = str("Arquivo excel criado com sucesso!!!")
            self.v.set("")
            Window.update()

            # Validação de dados
            if ((data1 == "") or (data2 == "") or (Nome_Arquivo == "") or (Nome_Salvar == "") or (estacao == 0)):
                validacao = str("Preencha os campos corretamente!!!")
                self.v.set(validacao)
                Window.update()

            elif estacao == 1:  # Estação 1231
                objeto = Estacao1231()   
                instancia = objeto._init_(data1, data2, Nome_Arquivo, Nome_Salvar)
                self.v.set(resultado)

            elif estacao == 2: # Estação 1232
                objeto = Estacao1232() 
                instancia = objeto._init_(data1, data2, Nome_Arquivo, Nome_Salvar)
                self.v.set(resultado)

        def limpar(self):
            self.entry2.delete(0,END)
            self.entry3.delete(0,END)
            self.entry4.delete(0,END)
            self.entry5.delete(0,END)
            self.rb_value.set(0)
            self.v.set("")
            self.entry2.focus()
            Window.update()

# Parâmetros da tela
        def __init__(self, instancia_de_Tk):
            frame1 = tkinter.Frame(instancia_de_Tk)
            frame1.configure(border=5)
            frame1.pack()
            frame2 = Frame(instancia_de_Tk)
            frame2.configure(border=5)
            frame2.pack()
            frame3 = Frame(instancia_de_Tk)
            frame3.configure(border=5)
            frame3.pack()
            frame4 = Frame(instancia_de_Tk)
            frame4.configure(border=5)
            frame4.pack()
            frame5 = Frame(instancia_de_Tk)
            frame5.configure(border=5)
            frame5.pack()
            frame6 = Frame(instancia_de_Tk)
            frame6.configure(border=5)
            frame6.pack()
            frame7 = Frame(instancia_de_Tk)
            frame7.configure(border=5)
            frame7.pack()
            frame8 = Frame(instancia_de_Tk)
            frame8.configure(border=5)
            frame8.pack()

# Parâmetros dos dados apresentados na tela
            label1 = Label(frame1, text="Formato de data: yyyy-mm-dd")
            label1.pack()

            label2 = Label(frame2, text="Insira a data inicio para consulta: ")
            label2.pack()
            self.entry2 = Entry(frame2)
            self.entry2.pack()

            label3 = Label(frame3, text="Insira a data final para consulta: ")
            label3.pack()
            self.entry3 = Entry(frame3)
            self.entry3.pack()

            label4 = Label(frame4, text="Insira o nome do arquivo existente: ")
            label4.pack()
            self.entry4 = Entry(frame4)
            self.entry4.pack()

            label5 = Label(frame5, text="Insira um nome para salvar o arquivo: ")
            label5.pack()
            self.entry5 = Entry(frame5)
            self.entry5.pack()


            self.rb_value = IntVar()
            self.rb1 = Radiobutton(frame6, text="Estação 1231", value=1, variable=self.rb_value).pack(anchor=W)
            self.rb2 = Radiobutton(frame6, text="Estação 1232", value=2, variable=self.rb_value).pack(anchor=W)

            label6 = Label(frame7, text="Resultado: ")
            label6.pack()
            self.v = StringVar()
            label6 = Label(frame7, text="", textvariable=self.v, background="white", font="14")
            label6.pack()

# Parâmetros de execução
            button1 = Button(frame8, text="Buscar", borderwidth=5, command=lambda: self.executa())
            button1.pack(side= "right")

            button2 = Button(frame8, text="Limpar", borderwidth=5, command=lambda: self.limpar())
            button2.pack(side= "left")

# Parâmetros da tela
    Window = tkinter.Tk()
    Window.title("Dados Planilha")
    Window.geometry("360x400")
    Principal(Window)
    Window.mainloop()

# Encerrar conexao com o banco de dados
    if (conexao.con.is_connected()):
        conexao.cursor.close()
        conexao.con.close()
        print("Conexão ao MySQL encerrada.\n")

except OSError as e:
    print("Erro: ", e)
