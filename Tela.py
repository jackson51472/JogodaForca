import PySimpleGUI as sg
from Jogo import *

sg.theme("LightBlue7")

global vidas


#Janela para escreve a palavra
def janela_Palavra():
    layout = [
                [sg.Text("Digite a palavra")],
                [sg.Input(key="digitar_palavra")],
                [sg.Button("COMFIRMAR")]
    ]
    return sg.Window("Adivinhando", layout=layout, finalize=True)


# def janela_Adivinhar(palavra):
#     global vidas
#
#     vidas = 2
#     palavraCerta = listar_palavra(palavra)
#     palavraEscondida = escondePalavra(palavraCerta)
#
#    print(palavraCerta)
#    print(palavraEscondida)

    # layout = [
    #     [sg.Text(f"VOCÊ AINDA TEM {vidas:.0f} VIDAS")],
    #     [sg.Text(palavraCerta)],
    #     [sg.Text(palavraEscondida)],
    #     [sg.Text(f"Digite uma letra: ")],
    #     [sg.Input(key="letra")],
    #     [sg.Button("Comfirmar")]
    # ]
    # return sg.Window("Adivinhar", layout = layout, finalize = True)


def janela_Adivinhar(palavra, letra, palavraEscondida):
    if letra != None:
        letra = letra.upper()
    adivinhar(palavra, palavraEscondida, letra)


#    print(palavraCerta)
#    print(palavraEscondida)

    layout = [
        [sg.Text(f"VOCÊ AINDA TEM {vidas:.0f} VIDAS")],
        [sg.Text(palavraEscondida)],
        [sg.Text(f"Digite uma letra: ")],
        [sg.Input(key="letra")],
        [sg.Button("Comfirmar")]
    ]
    return sg.Window("Adivinhar", layout = layout, finalize = True)

def janela_Vitoria():
    layout = [
        [sg.Text("PARABÉNS VOCÊ ACERTOU")],
        [sg.Text("    Deseja continuar?")],
        [sg.Button("Continuar"),sg.Button("Parar")]
    ]
    return sg.Window("Ganhou", layout=layout, finalize=True)

def janela_Derrota():
    layout = [
        [sg.Text("Você perdeu")],
        [sg.Text("Deseja continuar?")],
        [sg.Button("Continuar"),sg.Button("Parar")]
    ]
    return sg.Window("Perdeu", layout=layout, finalize=True)



janela_Um, janela_Dois = janela_Palavra(), None

while True:
    window,evento, valor = sg.read_all_windows()

    #Abre primeira janela
    if window == janela_Um and evento == sg.WIN_CLOSED or evento == "Parar" or window == janela_Dois and evento == sg.WIN_CLOSED:
        sg.popup("Fechando")
        break
    elif window == janela_Dois and evento == "Continuar":
        janela_Dois.close()
        janela_Um = janela_Palavra()

    #Abre segunda janela e fecha a primeira
    elif window == janela_Um and evento == "COMFIRMAR":

        #Chama 2 função para que a palavra seja colocar em uma lista
        palavra_Sup = listar_palavra(valor["digitar_palavra"])
        palavra_Escondida= esconde_Palavra(palavra_Sup)

        #Verifica a dificuldade da palavra
        if len(palavra_Sup) <= 4:
            vidas = 2
        elif len(palavra_Sup) < 7:
            vidas = 4
        elif len(palavra_Sup) >= 7:
            vidas = 6

        janela_Dois = janela_Adivinhar(palavra_Sup, None, palavra_Escondida)

        #Fecha a janela um
        janela_Um.close()

    #Atualiza a janela e verifica vidas e se a palavra_Escondida esta igual a palavra_Sup
    elif window == janela_Dois and evento == "Comfirmar":
        #Fecha
        janela_Dois.close()
        #Atualiza
        janela_Dois = janela_Adivinhar(palavra_Sup, valor["letra"], palavra_Escondida)

        #Verifica se palavra_Escondida esta igual a palavra_Sup
        if palavra_Sup == palavra_Escondida:
            janela_Dois.close()
            janela_Dois = janela_Vitoria()
        else:
            vidas = verificar_Vidas(valor["letra"], palavra_Sup, vidas)
            if vidas <= 0:
                janela_Dois.close()
                janela_Dois = janela_Derrota()




window.close()


#[
# [1]
# [2]
# [3,3]
#]