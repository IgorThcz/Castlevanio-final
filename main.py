# ------------------------------------- IMPORTAÇÕES ----------------------------------- #
from Menus.Configuracoes import *
from PPlay.sound import *
from Menus.Botoes import Botao
from Menus.Espaço import espaco


# ----------------------------- DEFINIÇÃO DE ALGUMAS COISAS --------------------------- #
janela = Window(960, 640)
mouse = Window.get_mouse()
clicado = True

# ---------------------------------- GAME OBJECTS ------------------------------------- #

# FUNDO
fundo = GameImage("Assets/Imagens/Menus/Variados/fundo.png")
fundo.x = 0
fundo.y = 0

# TÍTULO
titulo = GameImage("Assets/Imagens/Menus/Variados/titulo.png")
titulo.x = 171
titulo.y = 50

# BOTÕES
botjogar = Botao("Botoes/bot_jogar", 90, 430)
botconfig = Botao("Botoes/bot_config", 380, 430)
botsair = Botao("Botoes/bot_sair", 670, 430)

tapestry = Sound("Assets/Audio/tapestry.mp3")
tapestry.set_volume(40)

clique = Sound("Assets/Audio/Fantasy_UI (19).wav")
clique.set_volume(40)

# ----------------------------------------- LOOP ------------------------------------- #
while True:

    # ----------------------------------- MUSUICA E SOM ------------------------------ #
    var = open("Saves/audio.csv", "r")
    audio = [0, 0]
    audio[0] = var.readline().strip()
    audio[1] = var.readline().strip()
    var.close()

    if not tapestry.is_playing() and audio[0] == "1":
        tapestry.play()

    if audio[0] == "0":
        tapestry.stop()

    # ---------------------------- AÇÕES DENTRO DO GAME LOOP ------------------------- #

    # SISTEMA DE MENU ------------------------------------------------------------------
    if not clicado and mouse.is_button_pressed(1):

        # INICIAR O JOGO -------------------------
        if mouse.is_over_object(botjogar.image):
            if audio[1] == "1":
                clique.play()
            espaco(tapestry, audio, clique)

        # IR PARA CINFIGURAÇÕES ------------------
        elif mouse.is_over_object(botconfig.image):
            if audio[1] == "1":
                clique.play()
            config(tapestry, clique)

        # SAIR DO JOGO ---------------------------
        elif mouse.is_over_object(botsair.image):
            if audio[1] == "1":
                clique.play()
            break

    if mouse.is_button_pressed(1):
        clicado = True
    else:
        clicado = False

    # DESENHAR OS OBJETOS -------------------------------------------------------------------
    fundo.draw()
    titulo.draw()
    botjogar.desenhar(audio[1])
    botconfig.desenhar(audio[1])
    botsair.desenhar(audio[1])

    # ATUALIZAR JANELA ------------------------------------------------------------------
    janela.update()

