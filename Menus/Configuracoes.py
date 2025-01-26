# ------------------------------------- IMPORTAÇÕES -------------------------------------#
from PPlay.window import *
from PPlay.gameimage import *
from PPlay.mouse import *

from Menus.Botoes import Botao
from Menus.Auxiliar import Display


# -------------------------------------- função definir tecla -----------------------------------#
'''essa função serve para realizar a seleção da entrada que o jogador quer usar para cada controle
nas configurações do jogo'''


def definir_tecla(janela):
    # ----------------------------------- DEFINIR AS COISAS :) ---------------------------------#
    teclado = Window.get_keyboard()

    teclas = ["esc",
              "q", "w", "e", "r", "t", "y", "u", "i", "o", "p",
              "a", "s", "d", "f", "g", "h", "j", "k", "l",
              "z", "x", "c", "v", "b", "n", "m",
              "space",
              ]

    pausa = GameImage("Assets/Imagens/Menus/Variados/pre-imput.png")
    pausa.x = 0
    pausa.y = 126

    pausa.draw()
    janela.update()

    while True:

        # ------------------------------- PARTE PRINTCIPAL ------------------------------------------- #
        for i in range(len(teclas)):
            print(teclado.show_key_pressed())
            if teclado.key_pressed(teclas[i]):
                return teclas[i]


# -------------------------------- FUNÇÃO DAS CONFIGURAÇÕES --------------------------------#
def config(musica_menu, clique):

    # --------------------------- DEFINIÇÕES DE ALGUMAS COISAS -------------------------#
    janela = Window(960, 640)
    mouse = Window.get_mouse()
    teclado = Window.get_keyboard()

    # FUNDO ----------------------------------------------------------------------------
    fundo = GameImage("Assets/Imagens/Menus/Variados/fundo.png")
    fundo.x = 0
    fundo.y = 0

    # CONTROLES -------------------------------------------------------------------------
    sec_controles = GameImage("Assets/Imagens/Menus/Variados/controles_config.png")
    sec_controles.x = 100
    sec_controles.y = 200
    controles = [
        Botao("Botoes/bot_direita", 180, 300),  # andar para a direita
        Botao("Botoes/bot_esquerda", 180, 380),  # andar para a esquerda
        Botao("Botoes/bot_pulo", 180, 460),  # pular
        Botao("Botoes/bot_abaixar", 180, 540),  # agachar
        Botao("Botoes/bot_atacar", 180, 620),  # atacar
        Botao("Botoes/bot_usar_magia", 180, 700),  # usar magia

        Botao("Botoes/bot_habilidade", 590, 300),  # usar habilidade
        Botao("Botoes/bot_item", 590, 380),  # usar item
        Botao("Botoes/bot_mochila", 590, 460),  # abrir mochila
        Botao("Botoes/bot_pausar", 590, 540),  # pausar
        Botao("Botoes/bot_mapa", 590, 620)  # abrir mapa
    ]
    red = Botao("Botoes/bot_redefinir", 590, 700)

    # DISPLAY DA TECLA -----------------------------------------------------------------
    var = open("Saves/config.csv", "r")
    lista = var.readlines()
    var.close()
    for i in range(len(lista)):
        lista[i].strip()
    displays = [
        Display(390, 300, f"{lista[0]}"),
        Display(390, 380, f"{lista[1]}"),
        Display(390, 460, f"{lista[2]}"),
        Display(390, 540, f"{lista[3]}"),
        Display(390, 620, f"{lista[4]}"),
        Display(390, 700, f"{lista[5]}"),

        Display(800, 300, f"{lista[6]}"),
        Display(800, 380, f"{lista[7]}"),
        Display(800, 460, f"{lista[8]}"),
        Display(800, 540, f"{lista[9]}"),
        Display(800, 620, f"{lista[10]}")

    ]

    # AUDIO -----------------------------------------------------------------------------
    sec_audio = GameImage("Assets/Imagens/Menus/Variados/audio_config.png")
    sec_audio.x = 100
    sec_audio.y = 20

    mus = Botao("Botoes/bot_musica", 180, 92)
    mus_on = GameImage("Assets/Imagens/Menus/Botoes/audio_true.png")
    mus_on.x = 390
    mus_on.y = 92
    mus_off = GameImage("Assets/Imagens/Menus/Botoes/audio_false.png")
    mus_off.x = 390
    mus_off.y = 92

    efe = Botao("Botoes/bot_efeitos", 590, 92)
    efe_on = GameImage("Assets/Imagens/Menus/Botoes/audio_true.png")
    efe_on.x = 800
    efe_on.y = 92
    efe_off = GameImage("Assets/Imagens/Menus/Botoes/audio_false.png")
    efe_off.x = 800
    efe_off.y = 92

    # BOTÃO VOLTAR ---------------------------------------------------------------------
    botvoltar = Botao("Botoes/bot_voltar", 20, 20)

    # ----------------------------------- LOOP ---------------------------------------- #
    clicado = True
    while True:

        # --------------------------- AÇÕES DENTRO DO GAME LOOP ----------------------- #


        # ------------------------------- MUSICA E SONS ------------------------------- #
        var = open("Saves/audio.csv", "r")
        audio = [0, 0]
        audio[0] = var.readline().strip()
        audio[1] = var.readline().strip()
        var.close()
        vel = janela.delta_time() * 1000

        if not musica_menu.is_playing() and audio[0] == "1":
            musica_menu.play()

        if audio[0] == "0":
            musica_menu.stop()

        # ROLAGEM DE TELA --------------------------------------------------------------

        if teclado.key_pressed("s") and sec_controles.y >= 20:

            sec_audio.y -= vel
            mus.image.y -= vel
            mus.image_var.y -= vel
            mus_on.y -= vel
            mus_off.y -= vel
            efe.image.y -= vel
            efe.image_var.y -= vel
            efe_on.y -= vel
            efe_off.y -= vel

            sec_controles.y -= vel
            for i in range(len(controles)):
                controles[i].image.y -= vel
                controles[i].image_var.y -= vel
            red.image.y -= vel
            red.image_var.y -= vel
            for i in range(len(displays)):
                displays[i].imagem.y -= vel


        elif teclado.key_pressed("w") and sec_audio.y < 20:

            sec_audio.y += vel
            mus.image.y += vel
            mus.image_var.y += vel
            mus_on.y += vel
            mus_off.y += vel
            efe.image.y += vel
            efe.image_var.y += vel
            efe_on.y += vel
            efe_off.y += vel

            sec_controles.y += vel
            for i in range(len(controles)):
                controles[i].image.y += vel
                controles[i].image_var.y += vel
            red.image.y += vel
            red.image_var.y += vel
            for i in range(len(displays)):
                displays[i].imagem.y += vel

        # OPÇÕES DAS CONFIGURAÇÕES -----------------------------------------------------
        if mouse.is_button_pressed(BUTTON_LEFT) and not clicado:

            # voltar ao menu
            if mouse.is_over_object(botvoltar.image):
                if audio[1] == "1":
                    clique.play()
                break

            # personalizar controles
            for i in range(len(controles)):
                if mouse.is_over_object(controles[i].image):
                    if audio[1] == "1":
                        clique.play()
                    var = open("Saves/config.csv", "r")
                    lista = var.readlines()
                    for j in range(len(lista)):
                        lista[j].strip()
                    var.close()

                    var = open("Saves/config.csv", "w")
                    lista[i] = f"{definir_tecla(janela)}\n"
                    for j in range(len(lista)):
                        var.write(f"{lista[j]}")
                    var.close()

            # redefinir controles
            if mouse.is_over_object(red.image):
                if audio[1] == "1":
                    clique.play()
                var = open("Saves/config.csv", "w")
                aux = ["d", "a", "w", "s", "g", "k", "h", "j", "i", "esc", "m"]
                for i in range(len(lista)):
                    var.write(f"{aux[i]}\n")
                var.close()

            # musica on/off
            if mouse.is_over_object(mus.image):
                if audio[1] == "1":
                    clique.play()
                var = open("Saves/audio.csv", "r")
                lista = var.readlines()
                var.close()

                var = open("Saves/audio.csv", "w")
                if lista[0] == "1\n":
                    var.write("0\n")
                else:
                    var.write("1\n")
                var.write(lista[1])
                var.close()

            # sfx on/off
            if mouse.is_over_object(efe.image):
                if audio[1] == "1":
                    clique.play()
                var = open("Saves/audio.csv", "r")
                lista = var.readlines()
                var.close()

                var = open("Saves/audio.csv", "w")
                var.write(lista[0])
                if lista[1] == "1\n":
                    var.write("0\n")
                else:
                    var.write("1\n")
                var.close()

            pygame.time.delay(100)

        if mouse.is_button_pressed(1):
            clicado = True
        else:
            clicado = False

        # ----------------------------- DESENHAR OS OBJETOS ----------------------------#
        # game images
        fundo.draw()
        sec_controles.draw()
        sec_audio.draw()

        # desenhar as informações das configurações de áudio
        var = open("Saves/audio.csv", "r")
        lista = var.readlines()
        if lista[0] == "1\n":
            mus_on.draw()
        else:
            mus_off.draw()
        if lista[1] == "1\n":
            efe_on.draw()
        else:
            efe_off.draw()

        # desenhar as informações das configurações de controle
        var = open("Saves/config.csv", "r")
        lista = var.readlines()
        var.close()
        for i in range(len(lista)):
            displays[i].texto = lista[i].strip()
            displays[i].desen()

        # botoes independentes
        botvoltar.desenhar(audio[1])
        mus.desenhar(audio[1])
        efe.desenhar(audio[1])
        red.desenhar(audio[1])

        # botoes em lista
        for i in range(len(controles)):
            controles[i].desenhar(audio[1])

        # ------------------------------- ATUALIZAR JANELA -----------------------------#
        janela.update()
