def listar_palavra(palavra):
    variavel =[]
    for i in palavra:
        variavel.append(i.upper())
    return variavel

def esconde_Palavra(palavra):
    escodida = []
    for i in range(len(palavra)):
        escodida.append("_")
    return escodida

def adivinhar(palavraCerta, palavraEscondida, letra):

    for i in range(len(palavraCerta)):
        if letra == palavraCerta[i]:
            palavraEscondida[i] = palavraCerta[i]

    return palavraEscondida

def verificar_Vidas(letra, palavraCerta,vidas):
    letra = letra.upper()

    for i in range(len(palavraCerta)):

        if letra == palavraCerta[i]:
            aux = 0
            break
        else:
            aux = -1

    vidas += aux

    return vidas

def verificar_Vitoria(palavraCerta, palavraEscondida):
    tamannho = len(palavraCerta)
    acertos = 0
    for i in range(len(palavraCerta)):
        if palavraCerta[i] == palavraEscondida[i]:
            acertos += 1
        else:
            break
    if acertos == tamannho:
        return 1
    else:
        return 0

def executavel():
    vidas = 2
    palavraCerta = listar_palavra()
    palavraEscondida = esconde_Palavra(palavraCerta)
    print(palavraCerta)
    print(palavraEscondida)

    while True:
        letra = input(f"VOCÊ AINDA TEM {vidas:.0f} VIDAS\nDigite uma letra: \n>>>")
        letra = letra.upper()
        print(palavraCerta)

        adivinhar(palavraCerta, palavraEscondida, letra)
        vidas = verificar_Vidas(letra,palavraCerta,vidas)

        if vidas <= 0:
            print("VOCÊ PERDEU ")
            print("A PALAVRA ERA: ", palavraCerta)
            print("VOCÊ DIGITOU:  ", palavraEscondida)
            break

        vitoria = verificar_Vitoria(palavraCerta, palavraEscondida)

        if vitoria == 1:
            print("VOCÊ GANHOU")
            print("A PALAVRA ERA: ", palavraCerta)
            print("VOCÊ DIGITOU:  ", palavraEscondida)
            break




        print(palavraEscondida)

# sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
# layout = [  [sg.Text('Some text on Row 1')],
#             [sg.Text('Enter something on Row 2'), sg.InputText()],
#             [sg.Button('Ok'), sg.Button('Cancel')] ]
#
# Create the Window
# window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
# while True:
#     event, values = window.read()
#     if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
#         break
#     print('You entered ', values[0])
#
# window.close()
