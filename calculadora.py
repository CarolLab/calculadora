from tkinter import *

#Janela


# def apagar_uma():
#     monitor["text"] -= monitor["text"][:-1]

    #Por noutra versão no github
    # texto_atual = monitor.cget("text")  # Obtém o texto atual corretamente
    # if texto_atual:
    #     monitor["text"] = texto_atual[:-1] #o que fica no "text" é o quetêm text_atual até ao índice -2,
    #     # ou seja não inclui o último (-1)

def mostrar(va):
    try:
        monitor["text"] += str(va) #Soma ao monitor o simbolo pretendido
    except: #dá erro de não poder juntar int + str então apaga e mostra o número escolhido
        monitor["text"] = va



def apagar2():
    monitor["text"] = "" #Apaga/transforma o texto da string(label) em nada




def resultado(tela): #Reseltado
    try:
        conta = tela["text"]

        result = eval(conta)

        tela["text"] = result



    except: #De der erro a tela fica vazia
        tela["text"] = ""


################################################################

#Janela

janela = Tk()

janela.geometry("234x330")
janela.title("Calculadora")
#Adicionar icon
#Mudar a fonte da letras/ números


#Monitor
monitor = Label(janela, text="", anchor= "e", relief = "flat",justify= RIGHT,
                width = 18, height= 2, padx = 7,
                bg="#423f3f", fg="White",font = "Ivy 16")
monitor.place(x = 0,y = 3)



#Operadores
#Divisão
divid = Button(janela, text="/", width=7, height = 3, bg = "Orange", relief="raised",
               command= lambda: mostrar("/"))
divid.place(x = 175, y = 58)


#Multiplicação
mult = Button(janela, text = "*", width=7, height=3, bg = "Orange",relief="raised",
              command = lambda: mostrar("*"))
mult.place(x = 175, y = 113)


#Subtração
subtrair = Button(janela, text = "-", width=7,height=3, bg = "Orange",relief="raised",
                  command=lambda: mostrar("-"))
subtrair.place(x = 175, y = 168)


#Adição
somar = Button(janela, text= "+", width=7,height=3,bg = "Orange",relief= "raised",
               command= lambda: mostrar("+"))
somar.place(x = 175, y = 223)





#Apagar
apagtud = Button(janela, text="C", width=15, height = 3, padx=2,
                 command= apagar2) #tamanho original 14
apagtud.place(x = 0, y = 58)


apagar = Button(janela, width = 7, height = 3, text = "⌫",anchor="center",state = "disabled")
apagar.place(x = 116, y = 58)



#A função lambda cria uma função anónima sem nome, que executa a função mostrar() quando o botão seja clicado
#def funcao():
#    mostrar("/")

#Linha 1
sete = Button(janela, text= "7", width=7,height=3,
              relief= "raised", overrelief="flat",
              command= lambda: mostrar("7"))
sete.place(x = 0, y= 113)

oito = Button(janela, text="8",width=7,height=3,
              relief= "raised", overrelief= "flat",
              command= lambda: mostrar("8"))
oito.place(x = 58, y = 113)

nove = Button(janela, text = "9",width=7,height=3,
              relief= "raised",overrelief="flat",
              command = lambda: mostrar("9"))
nove.place(x = 116, y = 113)



#Linha2
quatro = Button(janela, text = "4",width=7,height=3,
                relief= "raised", overrelief="flat",
                command = lambda: mostrar("4"))
quatro.place(x = 0, y = 168)

cinco = Button(janela, text = "5", width=7,height=3,
               relief= "raised", overrelief="flat",
               command= lambda: mostrar("5"))
cinco.place(x = 58, y = 168)

seis= Button(janela, text = "6",width=7,height=3,
             relief= "raised", overrelief="flat",
             command= lambda: mostrar("6"))
seis.place(x = 116, y = 168)



#Linha3
um = Button(janela, text = "1", width=7,height=3,
            relief= "raised", overrelief="flat",
            command= lambda: mostrar("1"))
um.place(x=0, y =223)

dois = Button(janela, text = "2", width=7,height=3,
              relief= "raised", overrelief="flat",
              command= lambda: mostrar("2"))
dois.place(x = 58, y = 223)

tres = Button(janela, text="3", width=7,height=3,
              relief= "raised", overrelief="flat",
              command= lambda: mostrar("3"))
tres.place(x = 116, y = 223)



#Linha4
zero = Button(janela, text = "0", width=15, height = 3,padx=2,
              relief= "raised", overrelief="flat",
              command= lambda: mostrar("0"))
zero.place(x = 0, y = 278)

ponto = Button(janela, text = ".", width=7,height=3,
               relief="raised", overrelief="flat",
               command= lambda: mostrar("."))
ponto.place(x = 116, y = 278)

igual = Button(janela, text= "=", width=7,height=3,bg= "Orange", relief= "raised",
               command=lambda : resultado(monitor))
igual.place(x = 175, y = 278)

###################
janela.mainloop()