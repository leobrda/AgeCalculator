from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from dateutil.relativedelta import relativedelta
from datetime import date

# Criando a janela
janela = Tk()
janela.title('Calculadora de Idade')
janela.geometry('310x400')
janela.resizable(FALSE, FALSE)

# Cor cinza
cor1 = '#4f4f4f'
# Cor preta
cor2 = '#333333'
# Cor branca
cor3 = '#ffffff'
# Cor laranja
cor4 = '#fcc058'

# Criando frames para a janela
# Parte de cima
frame_cima = Frame(janela, width=310, height=140, pady=0, padx=0, relief='flat', bg=cor2)
frame_cima.grid(row=0, column=0)

# Parte debaixo
frame_baixo = Frame(janela, width=310, height=400, pady=0, padx=0, relief=FLAT, bg=cor1)
frame_baixo.grid(row=1, column=0)

# Criando labels para frame cima
l_calculadora = Label(frame_cima, text='CALCULADORA', width=25, height=1, padx=3,
                      relief=FLAT, anchor='center', font='Ivi 15 bold', bg=cor2, fg=cor3)
l_calculadora.place(x=0, y=30)

l_idade = Label(frame_cima, text='DE IDADE', width=11, height=1, padx=0,
                      relief=FLAT, anchor='center', font='Arial 35 bold', bg=cor2, fg=cor4)
l_idade.place(x=0, y=70)


# Criando a função para calcular a idade
def calcular():
    dia_atual = cal_1.get()
    dia_nascimento = cal_2.get()

    # Separando os valores
    dia_1, mes_1, ano_1 = [int(f) for f in dia_atual.split('/')]
    # Convertendo os valores em date/datetime
    data_inicial = date(ano_1, mes_1, dia_1)

    # Separando os valores
    dia_2, mes_2, ano_2 = [int(f) for f in dia_nascimento.split('/')]
    # Convertendo os valores em date/datetime
    data_nascimento = date(ano_2, mes_2, dia_2)

    # Convertendo os valores em formato date/datetime
    anos = relativedelta(data_inicial, data_nascimento).years
    meses = relativedelta(data_inicial, data_nascimento).months
    dias = relativedelta(data_inicial, data_nascimento).days

    l_app_anos['text'] = anos
    l_app_meses['text'] = meses
    l_app_dias['text'] = dias


# Criando labels para frame baixo
# Data inicial e calendário para data inicial
l_data_inicial = Label(frame_baixo, text='Data atual', height=1, padx=0, pady=0,
                      relief=FLAT, anchor=NW, font='Ivi 11 bold', bg=cor1, fg=cor3)
l_data_inicial.place(x=20, y=30)
cal_1 = DateEntry(frame_baixo, width=13, bg='darkblue', fg=cor3, borderwith=2, date_pattern='dd/mm/yyyy',
                  y=2024)
cal_1.place(x=185, y=30)

# Data de nascimento e calendário para data de nascimento
l_data_nascimento = Label(frame_baixo, text='Data de nascimento', height=1, padx=0, pady=0,
                      relief=FLAT, anchor=NW, font='Ivi 11 bold', bg=cor1, fg=cor3)
l_data_nascimento.place(x=20, y=70)
cal_2 = DateEntry(frame_baixo, width=13, bg='darkblue', fg=cor3, borderwith=2, date_pattern='dd/mm/yyyy',
                  y=2024)
cal_2.place(x=185, y=70)

# Label para anos
l_app_anos = Label(frame_baixo, text='--', height=1, padx=0, pady=0,
                      relief=FLAT, anchor=CENTER, font='Ivi 25 bold', bg=cor1, fg=cor3)
l_app_anos.place(x=60, y=135)
l_app_anos_nome = Label(frame_baixo, text='ANOS', height=1, padx=0, pady=0,
                      relief=FLAT, anchor=CENTER, font='Ivi 11 bold', bg=cor1, fg=cor3)
l_app_anos_nome.place(x=55, y=175)

# Label para meses
l_app_meses = Label(frame_baixo, text='--', height=1, padx=0, pady=0,
                      relief=FLAT, anchor=CENTER, font='Ivi 25 bold', bg=cor1, fg=cor3)
l_app_meses.place(x=146, y=135)
l_app_meses_nome = Label(frame_baixo, text='MESES', height=1, padx=0, pady=0,
                      relief=FLAT, anchor=CENTER, font='Ivi 11 bold', bg=cor1, fg=cor3)
l_app_meses_nome.place(x=130, y=175)

# Label para dias
l_app_dias = Label(frame_baixo, text='--', height=1, padx=0, pady=0,
                      relief=FLAT, anchor=CENTER, font='Ivi 25 bold', bg=cor1, fg=cor3)
l_app_dias.place(x=210, y=135)
l_app_dias_nome = Label(frame_baixo, text='DIAS', height=1, padx=0, pady=0,
                      relief=FLAT, anchor=CENTER, font='Ivi 11 bold', bg=cor1, fg=cor3)
l_app_dias_nome.place(x=210, y=175)

# Criando botão para calcular
botao_calcular = Button(frame_baixo, command=calcular, text='CALCULAR', width=20, height=1,
                      relief=RAISED, overrelief=RIDGE, font='Ivi 10 bold', bg=cor1, fg=cor3)
botao_calcular.place(x=70, y=210)

janela.mainloop()

