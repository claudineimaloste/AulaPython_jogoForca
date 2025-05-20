from tkinter import *
import random
#import playsound
import pygame



#playsound.playsound('musica_fundo.mp3',block=False) # mantemk a musica tocando
def musica_fundo ():
    pygame.mixer.init()
    pygame.mixer.music.load('musica_fundo3.mp3')
    pygame.mixer.music.play(-1)  # -1 = loop infinito
def som_vitoria():
    pygame.mixer.init()
    pygame.mixer.music.load('vitoria.mp3')
    pygame.mixer.music.play()
def som_game_over():
    pygame.mixer.init()
    pygame.mixer.music.load('derrota.mp3')
    pygame.mixer.music.play()

musica_fundo()


# metodo para informação e escolha da dificuldade

def escolha_dificuldade():
    Label(interface_dificuldade,text='Escolha a dificuldade: ',font=('Arial',12),fg='black').pack(pady=10,padx=10)

    Button(interface_dificuldade,text='Facil - 10 erros permitidos',font=('Arial',12),fg='black',
           command=escolha_facil).pack(pady=10,padx=10)
    Button(interface_dificuldade,text='Medio - 7 erros permitidos',font=('Arial',12),fg='black',
            command=escolha_medio).pack(pady=10,padx=10)
    Button(interface_dificuldade,text='Dificil - 5 erros permitidos',font=('Arial',12),fg='black',
            command=escolha_dificil).pack(pady=10,padx=10)


def imagem_vencedor ():
    img = PhotoImage(file='vitoria.png')
    figura_final = Label(interface_forca,image=img )
    figura_final.image = img
    figura_final.pack()
    caracter.destroy()
def imagem_derrota ():
    img = PhotoImage(file='derrota.png')
    figura_final = Label(interface_forca,image=img )
    figura_final.image = img
    figura_final.pack()
    caracter.destroy()


#metodos para escolha, ativar os botoes e acrescentar na lista a quantidade de chances

def escolha_facil():
    dificuldade.append(10)
    interface_dificuldade.destroy()

def escolha_medio():
    dificuldade.append(7)
    interface_dificuldade.destroy()

def escolha_dificil():
    dificuldade.append(5)
    interface_dificuldade.destroy() 

def forca(event):    
    
    try:
        char = caracter.get().upper()[0]

    except IndexError:
        pass
    
    else:

        try:
            int(char)

        except ValueError:
            if char not in letras_escolhidas:
                letras_escolhidas.append(char)#Atualiza a lista letras_escolhidas
                for indice in range (len(letras)):#Percorre toda lista de letras para conferencia
                    if char == letras[indice]:#Se o usuario acertou a letra faça:
                        lista_traco[indice] = letras[indice]#Atualiza lista_traco
                        caracter_vazio['text'] = lista_traco#Atualiza a interface
                        lista_conferencia.append(char)#Atualiza lista_conferencia
                if char not in letras:
                    lista_erro.append(char)
                    caracteres_anteriores ['text'] = lista_erro
        desenhar_boneco()


        entrada_dados.set('')
    if len(lista_conferencia) == len(letras):
        mensagem_final['text'] = 'Você acertou!!'
        palavra_escolhida['text'] = letras
        mensagem_final['fg'] = 'green'#atualiza a cor da mensagem        
        interface_forca.after(500, imagem_vencedor)
        pygame.mixer.music.stop()  # parar música de fundo
        som_vitoria()
        caracter.destroy() #Destroi o caracter para impedir mais entrada de dados
        label_instrucoes.destroy()
        label_letras_erradas.destroy()

        #Button(interface_jogo, text='Reiniciar', font=('Arial', 12), fg='blue', command=reiniciar_jogo).pack()      
        Button(interface_jogo,text='Finalizar',font=('Arial',12),fg='red',command=quit).pack() #Cria um botao para finalizar
        
    if len(lista_erro) == dificuldade [0]:
        mensagem_final['text'] = 'Tentativas finalizadas! Você Perdeu!'
        mensagem_final['fg'] = 'red'#atualiza a cor da mensagem 
        palavra_escolhida['text'] = letras
        interface_forca.after(500, imagem_derrota)
        pygame.mixer.music.stop()  # parar música de fundo
        som_game_over()
        caracter.destroy() #Destroi o caracter para impedir mais entrada de dados
        label_instrucoes.destroy()

       # Button(interface_jogo, text='Reiniciar', font=('Arial', 12), fg='blue', command=reiniciar_jogo).pack()
        Button(interface_jogo,text='Finalizar',font=('Arial',12),fg='red',command=quit).pack()      


def desenhar_boneco():
    cabeca_olhos_nariz = interface_forca.create_oval
    corpo = interface_forca.create_rectangle
    braco = interface_forca.create_line
    boca = interface_forca.create_arc

    if len(lista_erro) == 1:
        cabeca_olhos_nariz(165,95,215,140, fill='gray',outline='black')
    elif len(lista_erro) == 2:
        corpo(190,140,193,235, fill='Black')
    elif len(lista_erro) == 3:
         braco(190,140,130,190)
    elif len(lista_erro) == 4:
        braco(190,140,250,190)
    elif len(lista_erro) == 5:
        braco(190, 235, 125, 300)
    elif len(lista_erro) == 6:
        braco(190, 235, 250, 300)
    elif len(lista_erro) == 7:
        cabeca_olhos_nariz(175, 105, 185, 115, fill='white', outline='black')
    elif len(lista_erro) == 8:
        cabeca_olhos_nariz(195, 105, 205, 115, fill='white', outline='black')
    elif len(lista_erro) == 9:  # nariz
        cabeca_olhos_nariz(187.5, 117.5, 192.5, 122.5, fill='white', outline='black')
    elif len(lista_erro) == 10:  # boca
        boca(165, 125, 205, 130, fill='white')   

# Leitura do arquivo linha por linha de modo aleatório

with open ('Palavras.txt') as arq:

    leitura = arq.readlines() 
    palavra  = random.choice (leitura).split('\n')[0].upper()#seleciona a palavra, desconsiderando o enter.
# [0] seleciona a palavra, pois o split retorna uma lista.
#print(palavra)
# criar as listas para armazenar os dados.
letras = [] # armazena as letras da palavra escolhida aleatoriamente
lista_traco = [] # traços para apresentar o tamanho da palavra
lista_erro = [] # letras que forem erradas
letras_escolhidas = [] # todas as letras escolhidas
dificuldade = [] # numero maximo de erros
lista_conferencia = []


print(palavra)

# armazenar dados nas listas

for indice in range (len(palavra)):
    letras.append(palavra[indice]) 
    lista_traco.append('___')

# print(letras)
# print(lista_traco)
interface_dificuldade = Tk()#cria o objeto da classe Tk
interface_dificuldade.geometry('400x300')
interface_dificuldade.title('JOGO FORCA - PRIMEIRO MODULO (LOGICA DE PROGRAMAÇÃO)')#titulo da janela
escolha_dificuldade()#Chama a função da escolha da dificuldade
interface_dificuldade.mainloop()#manem a janela aberta


# interface do jogo

if len(dificuldade) == 1: # veerifica se há valor na lista dificuldade(primeiro criar a interface e explicar depois)
   
    interface_jogo = Tk ()# inicio da interface do jogo
    interface_jogo.title('JOGO FORCA - PRIMEIRO MODULO (LOGICA DE PROGRAMAÇÃO)')#titulo da janela
    
    # para organizar nossa interface
    interface_titulo = Canvas(interface_jogo)# otimiza uso e construção de formas geométrica
    interface_titulo.pack(side=TOP)
    interface_forca = Canvas(interface_jogo,width=300,height=300)
    interface_forca.pack(side=TOP)
    interface_texto = Canvas(interface_jogo,width=300,height=300)
    interface_texto.pack(side=TOP)
    
    interface_forca.create_rectangle(10,400,20,30,fill='blue')
    interface_forca.create_rectangle(10,30,200,40,fill='blue')
    interface_forca.create_rectangle(180,40,200,50,fill='red')
    interface_forca.create_rectangle(187.5,50,192.5,90,fill='black')
    interface_forca.create_oval(160,90,220,145,fill='black')
    interface_forca.create_oval(165,95,215,140,fill='white')

    # Mensagem inicial do jogo

    Label(interface_titulo,text='Bem vindo ao jogo da Forca',font=('Courier',20,'bold')).pack(padx=10,pady=10)
    label_instrucoes = Label(interface_texto,text='Informe uma letra abaixo:\n',font=('Courier',14,'bold'),fg='black')
    label_instrucoes.pack(padx=10,pady=10)

    entrada_dados = StringVar() # variavel responsável por receber a letra do usuário
    caracter = Entry(interface_texto,textvariable=entrada_dados,font=('arial',15))# reconhece o que o usuário digitou
    caracter.pack()
    caracter.bind('<Return>',forca)# Bind liga a letra a função forca

    #criar interface dos caracteres vazios

    caracter_vazio = Label(interface_texto,text=lista_traco,font=(20))
    caracter_vazio.pack()

    # bloco para as letras erradas

    label_letras_erradas = Label(interface_texto,text='Letras Erradas:', font=('Courier',14,'bold'))
    label_letras_erradas.pack()
    caracteres_anteriores = Label(interface_texto,text=lista_erro,font=(20))
    caracteres_anteriores.pack()

    # mensagem final
    mensagem_final = Label(interface_texto, text='',font=('courier', 16))
    mensagem_final.pack() 

    palavra_escolhida = Label(interface_texto,text='',font=('Arial Black', 20))
    palavra_escolhida.pack(padx=15,pady=20)

    interface_jogo.mainloop()