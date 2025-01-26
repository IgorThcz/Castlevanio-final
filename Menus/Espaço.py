# ------------------------------------- IMPORTAÇÕES ----------------------------------- #
from Jogo.Sala_novo import *
from Menus.Botoes import Botao


# ---------------------------- FUNÇÕES UTEIS PARA SAVES ------------------------------- #
def excluir(nome):
    # dados iniciais
    dados = [
             "099", 60, 45, 0, 0, 0, 10, 1,               # id/pos x/pos y/ ...
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, # itens
             4, False, False, False, False,               # magia selecionada/magias
             False                                        # habilidade
             ]
    var = open(f"Saves/{nome}.csv", "w")
    for i in range(len(dados)):
        var.write(f"{dados[i]}\n")
    var.close()


def espaco(menu_music, audio, clique):
    # ----------------------------- DEFINIÇÃO DE ALGUMAS COISAS --------------------------- #
    janela = Window(960, 640)
    mouse = Window.get_mouse()
    clicado = True

    # LER AS CONGIGURAÇÕES DOD CONTROLES ---------------
    var = open("Saves/config.csv")
    config = var.readlines()
    for i in range(len(config)):
        config[i] = config[i].strip()
    var.close()
    contrl = {
        "pular": config[2],
        "abaixar": config[3],
        "esquerda": config[1],
        "direita": config[0],
        
        "atacar": config[4],
        "habilidade": config[6],
        "item": config[7],
        "magia": config[5],
        
        "pausa": config[9],
        "mapa": config[10],
        "mochila": config[8]
    }

    # ---------------------------------- GAME OBJECTS ------------------------------------- #

    # FUNDO
    fundo = GameImage("Assets/Imagens/Menus/Variados/fundo.png")
    fundo.x = 0
    fundo.y = 0

    # CAIXAS
    caixa_1 = GameImage("Assets/Imagens/Menus/Botoes/caixa_um.png")
    caixa_1.x = 90
    caixa_1.y = 258

    caixa_2 = GameImage("Assets/Imagens/Menus/Botoes/caixa_dois.png")
    caixa_2.x = 380
    caixa_2.y = 258

    caixa_3 = GameImage("Assets/Imagens/Menus/Botoes/caixa_tres.png")
    caixa_3.x = 670
    caixa_3.y = 258

    # BOTÕES
    botjog_1 = Botao("Botoes/bot_seta", 204, 408)
    botjog_2 = Botao("Botoes/bot_seta", 494, 408)
    botjog_3 = Botao("Botoes/bot_seta", 784, 408)

    botdel_1 = Botao("Botoes/bot_lixo", 120, 408)
    botdel_2 = Botao("Botoes/bot_lixo", 420, 408)
    botdel_3 = Botao("Botoes/bot_lixo", 700, 408)

    voltar = Botao("Botoes/bot_voltar", 20, 20)

    # ----------------------------------------- LOOP ------------------------------------- #
    while True:

        # ---------------------------- AÇÕES DENTRO DO GAME LOOP ------------------------- #

        # MÚSICA --------------------------------------------------------------------------
        if not menu_music.is_playing() and audio[0] == "1":
            menu_music.play()

        # SISTEMA DE MENU ------------------------------------------------------------------
        if mouse.is_button_pressed(BUTTON_LEFT) == 1 and not clicado:

            # ESPAÇO DE SALVAMENTO 1 -------------------------
            if mouse.is_over_object(botjog_1.image):
                menu_music.stop()
                if audio[1] == "1":
                    clique.play()
                jogo("save1", contrl, audio)
            elif mouse.is_over_object(botdel_1.image):
                if audio[1] == "1":
                    clique.play()

                # caixa
                caixa_confirm = GameImage("Assets/Imagens/Menus/Botoes/caixa_confirm.png")
                caixa_confirm.x = 376
                caixa_confirm.y = 224

                # boão sim
                bot_sim = Botao("Botoes/bot_sim", 380, 268)

                # botão não
                bot_nao = Botao("Botoes/bot_nao", 380, 338)

                clicado_outro = True
                while True:

                    if mouse.is_button_pressed(1) and not clicado_outro:

                        if mouse.is_over_object(bot_nao.image):
                            break

                        if mouse.is_over_object(bot_sim.image):
                            excluir("save1")
                            break

                    if mouse.is_button_pressed(1):
                        clicado_outro = True
                    else:
                        clicado_outro = False

                    caixa_confirm.draw()

                    bot_sim.desenhar(audio[1])
                    bot_nao.desenhar(audio[1])

                    janela.update()

            # ESPAÇO DE SALVAMENTO 2 -------------------------
            elif mouse.is_over_object(botjog_2.image):
                menu_music.stop()
                if audio[1] == "1":
                    clique.play()
                jogo("save2", contrl, audio)
            elif mouse.is_over_object(botdel_2.image):
                if audio[1] == "1":
                    clique.play()

                # caixa
                caixa_confirm = GameImage("Assets/Imagens/Menus/Botoes/caixa_confirm.png")
                caixa_confirm.x = 376
                caixa_confirm.y = 224

                # boão sim
                bot_sim = Botao("Botoes/bot_sim", 380, 268)

                # botão não
                bot_nao = Botao("Botoes/bot_nao", 380, 338)

                clicado_outro = True
                while True:

                    if mouse.is_button_pressed(1) and not clicado_outro:

                        if mouse.is_over_object(bot_nao.image):
                            break

                        if mouse.is_over_object(bot_sim.image):
                            excluir("save2")
                            break

                    if mouse.is_button_pressed(1):
                        clicado_outro = True
                    else:
                        clicado_outro = False

                    caixa_confirm.draw()

                    bot_sim.desenhar(audio[1])
                    bot_nao.desenhar(audio[1])

                    janela.update()

            # ESPAÇO DE SALVAMENTO 3
            elif mouse.is_over_object(botjog_3.image):
                menu_music.stop()
                if audio[1] == "1":
                    clique.play()
                jogo("save3", contrl, audio)
            elif mouse.is_over_object(botdel_3.image):
                if audio[1] == "1":
                    clique.play()

                # caixa
                caixa_confirm = GameImage("Assets/Imagens/Menus/Botoes/caixa_confirm.png")
                caixa_confirm.x = 376
                caixa_confirm.y = 224

                # boão sim
                bot_sim = Botao("Botoes/bot_sim", 380, 268)

                # botão não
                bot_nao = Botao("Botoes/bot_nao", 380, 338)

                clicado_outro = True
                while True:

                    if mouse.is_button_pressed(1) and not clicado_outro:

                        if mouse.is_over_object(bot_nao.image):
                            break

                        if mouse.is_over_object(bot_sim.image):
                            excluir("save3")
                            break

                    if mouse.is_button_pressed(1):
                        clicado_outro = True
                    else:
                        clicado_outro = False

                    caixa_confirm.draw()

                    bot_sim.desenhar(audio[1])
                    bot_nao.desenhar(audio[1])

                    janela.update()

            # VOLTAR -----------------------------------------
            elif mouse.is_over_object(voltar.image):
                if audio[1] == "1":
                    clique.play()
                break

        if mouse.is_button_pressed(1):
            clicado = True
        else:
            clicado = False

        # DESENHAR OS OBJETOS ---------------------------------------------------------------
        fundo.draw()

        caixa_1.draw()
        caixa_2.draw()
        caixa_3.draw()

        botjog_1.desenhar(audio[1])
        botjog_2.desenhar(audio[1])
        botjog_3.desenhar(audio[1])

        botdel_1.desenhar(audio[1])
        botdel_2.desenhar(audio[1])
        botdel_3.desenhar(audio[1])

        voltar.desenhar(audio[1])

        # ATUALIZAR JANELA ------------------------------------------------------------------
        janela.update()


