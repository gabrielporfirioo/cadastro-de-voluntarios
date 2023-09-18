import tkinter as tk
from tkinter import ttk
import datetime as dt
import pandas as pd
import openpyxl


material = pd.read_excel('voluntarios.xlsx', engine='openpyxl')



lista_sexos= ["Masculino","Feminino","Outro"]
lista_codigos= []
janela = tk.Tk()
janela.geometry("500x350")


#FUNÇAO

def cadastrar():
    nome = entry_nome.get()
    email = entry_email.get()
    telefone = entry_telefone.get()
    cpf = entry_cpf.get()
    sexo = combobox_selecionar_sexo.get()
    data = dt.datetime.now()
    data =  data.strftime("%d/%m/%Y %H:%M")
    codigo = material.shape[0] + len(lista_codigos) + 1
    codigo_num= f"COD-{codigo}"
    lista_codigos.append((codigo_num, nome, email, telefone, cpf, sexo, data ))

    

#Titulo da janela

janela.title("Cadastro de Voluntários")

#CONTEUDO

label_inicio= tk.Label(text=" Por favor, preencha todos os campos! ",borderwidth=2, relief="solid")
label_inicio.grid(row=0, column=0, padx=130, pady=10, sticky='nswe', columnspan=10)




#nome#
label_nome = tk.Label(text="Nome:")
label_nome.grid(row=2, column=0, padx=10, pady=10, sticky='nswe', columnspan=1)

entry_nome = tk.Entry()
entry_nome.grid(row=2, column=1, padx=0, pady=10, sticky='nswe', columnspan=6)


#email#
label_email = tk.Label(text="Email:")
label_email.grid(row=3, column=0, padx=10, pady=10, sticky='nswe', columnspan=1)

entry_email = tk.Entry()
entry_email.grid(row=3, column=1, padx=0, pady=10, sticky='nswe', columnspan=5)


#telefone#
label_telefone = tk.Label(text="Telefone:")
label_telefone.grid(row=4, column=0, padx=10, pady=10, sticky='nswe', columnspan=1)

entry_telefone = tk.Entry()
entry_telefone.grid(row=4, column=1, padx=0, pady=10, sticky='nswe', columnspan=3)


#CPF#
label_cpf = tk.Label(text="CPF:")
label_cpf.grid(row=5, column=0, padx=10, pady=10, sticky='nswe', columnspan=1)

entry_cpf = tk.Entry()
entry_cpf.grid(row=5, column=1, padx=0, pady=10, sticky='nswe', columnspan=3)


#sexo#
label_sexo = tk.Label(text="Sexo:")
label_sexo.grid(row=6, column=0, padx=10, pady=10, sticky='nswe', columnspan=1)

combobox_selecionar_sexo = ttk.Combobox(values= lista_sexos)
combobox_selecionar_sexo.grid(row=6, column=1, padx=0, pady=10, sticky='nswe', columnspan=2)


#BOTÃO

botao_cadastrar = tk.Button(text="Cadastrar", command=cadastrar, background= '#b3e4e1',)
botao_cadastrar.grid(row=7, column=5, padx=0, pady=10, sticky='nswe', columnspan=1)




janela.mainloop()


#DATAFRAME (ENVIAR DADOS PARA O EXCEL)

novo_material = pd.DataFrame(lista_codigos, columns=['Código', 'Nome', 'Email','Telefone', 'CPF', 'Sexo', 'Data'])
material = pd.concat([novo_material], ignore_index= True)
material.to_excel('voluntarios.xlsx', index= False)


