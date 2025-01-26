from Inimigosvanio.inimigos import Inimigo
from Jogador.jogador_final import *
from NPCs.NPCs import *


def carregar_sala(id, obj, cords):
    var = open(f"Jogo/Salas/{id}.csv")

    # -------------------------------------- TILES SIMPLES ------------------------------- #
    quant = var.readline().strip()

    obj["tiles_simples"] = []
    if int(quant[0]) > 0:

        # ler do arquivo
        x = var.readline().split()
        y = var.readline().split()
        x[-1].strip()
        y[-1].strip()

        cords["x"] = x
        cords["y"] = y

        # colocar na lista
        for i in range(len(x)):
            obj["tiles_simples"].append(Elementos_de_sala(int(x[i]), int(y[i])))

    # --------------------------------------- INIMIGOS --------------------------------- #
    quant = var.readline().strip()

    obj["inimigos"] = []
    if int(quant[0]) > 0:

        # ler do arquivo
        x = var.readline().split()
        y = var.readline().split()
        tipo = var.readline().split()
        x[-1].strip()
        y[-1].strip()
        tipo[-1].strip()

        # colocar na lista
        for i in range(len(x)):
            obj["inimigos"].append(Inimigo(i, tipo[i], int(x[i]), int(y[i])))

    # --------------------------------------- INIMIGOS --------------------------------- #
    quant = var.readline().strip()

    obj["tiles_ini"] = []
    if int(quant[0]) > 0:

        # ler do arquivo
        x = var.readline().split()
        y = var.readline().split()
        x[-1].strip()
        y[-1].strip()

        # colocar na lista
        for i in range(len(x)):
            obj["tiles_ini"].append(Elementos_de_sala(int(x[i]), int(y[i])))

    # ---------------------------------------- PORTAS ---------------------------------- #
    quant = var.readline().strip()

    obj["portas"] = []
    if int(quant[0]) > 0:

        # ler do arquivo
        x = var.readline().split()
        y = var.readline().split()
        codigo = var.readline().split()
        novo_x = var.readline().split()
        novo_y = var.readline().split()
        x[-1].strip()
        y[-1].strip()
        codigo[-1].strip()
        novo_x[-1].strip()
        novo_y[-1].strip()

        # colocar na lista
        for i in range(len(x)):
            obj["portas"].append(Porta(codigo[i], int(x[i]), int(y[i]), int(novo_x[i]), int(novo_y[i])))

    # --------------------------------- PONTOS DE SALVAMENTO --------------------------- #
    quant = var.readline().strip()

    obj["salvamentos"] = []
    if int(quant[0]) > 0:

        # ler do arquivo
        x = var.readline().split()
        y = var.readline().split()
        codigo = var.readline().strip()
        x[-1].strip()
        y[-1].strip()

        # colocar na lista
        for i in range(len(x)):
            obj["salvamentos"].append(Ponto_salvamento(int(x[i]), int(y[i]), codigo, x[i], y[i]))

    # ----------------------------------------- NPCS ----------------------------------- #
    quant = var.readline().strip()

    obj["npcs"] = []
    if int(quant[0]) > 0:

        # ler do arquivo
        x = var.readline().split()
        y = var.readline().split()
        tipo = var.readline().split()
        x[-1].strip()
        y[-1].strip()
        tipo[-1].strip()

        # colocar na lista
        for i in range(len(x)):
            obj["npcs"].append(NPC(tipo[i], int(x[i]), int(y[i])))


    # ------------------------------------ PROJETEIS ---------------------------------- #
    obj["projeteis_player"] = []
    obj["projeteis_inimig"] = []

    # --------------------------------- CENARIO E FUNDO ------------------------------ #
    obj["cenario"] = GameImage(f"Assets/Imagens/Mapa/{id}.png")
    obj["cenario"].x = 0
    obj["cenario"].y = 0

    obj["fundo"] = GameImage(f"Assets/Imagens/Cenario/{id[0]}.png")
    obj["fundo"].x = 0
    obj["fundo"].y = 0

    var.close()


def carregar_jogador(num, obj):
    var = open(f"Saves/{num}.csv")
    var.readline()  #  <-- essa linha é o id da sala

    obj["jogador"].hitbox.x = int(var.readline().strip()) * 32
    obj["jogador"].hitbox.y = int(var.readline().strip()) * 32

    obj["jogador"].hpmax = 3 + int(var.readline().strip())
    obj["jogador"].dano = 1 + int(var.readline().strip())
    obj["jogador"].armaduramax = 1 + int(var.readline().strip())

    obj["jogador"].hp = obj["jogador"].hpmax
    obj["jogador"].mana = int(var.readline().strip())
    obj["jogador"].armadura = int(var.readline().strip())

    for i in range(15):
        aux = var.readline().strip()
        obj["jogador"].itens[i] = int(aux)

    obj["jogador"].magia_equip = int(var.readline().strip())
    for i in range(4):
        aux = var.readline().strip()
        if aux == "True":
            obj["jogador"].magias[i] = True
        else:
            obj["jogador"].magias[i] = False


    aux = var.readline().strip()
    if aux == "True":
        obj["jogador"].habilidades[0] = True
    else:
        obj["jogador"].habilidades[0] = False

    var.close()


def salvar(num, obj):
    var = open(f"Saves/{num}.csv", "w")

    var.write("099\n")

    var.write("60\n")
    var.write("45\n")

    var.write(f"{obj["jogador"].hpmax - 3}\n")
    var.write(f"{obj["jogador"].dano - 1}\n")
    var.write(f"{obj["jogador"].armaduramax - 1}\n")

    var.write(f"{obj["jogador"].mana}\n")
    var.write(f"{obj["jogador"].armadura}\n")

    for i in range(15):
        var.write(f"{obj["jogador"].itens[i]}\n")

    var.write(f"{obj["jogador"].magia_equip}\n")
    for i in range(4):
        var.write(f"{obj["jogador"].magias[i]}\n")

    for i in range(2):
        var.write(f"{obj["jogador"].habilidades[i]}\n")

    var.close()


def camera_dinamica(em_x, em_y, obj, delay):
    if -5 < em_x < 5:
        em_x = 0
    if -5 < em_y < 5:
        em_y = 0

    for i in range(len(obj["npcs"])):
        obj["npcs"][i].tipo.hitbox.x += em_x / delay
        obj["npcs"][i].tipo.hitbox.y += em_y / delay

    for i in range(len(obj["tiles_simples"])):
        obj["tiles_simples"][i].sprite.x += em_x / delay
        obj["tiles_simples"][i].sprite.y += em_y / delay

    for i in range(len(obj["tiles_ini"])):
        obj["tiles_ini"][i].sprite.x += em_x / delay
        obj["tiles_ini"][i].sprite.y += em_y / delay

    for i in range(len(obj["inimigos"])):
        if obj["inimigos"][i] != 0:
            obj["inimigos"][i].tipo.hitbox.x += em_x / delay
            obj["inimigos"][i].tipo.hitbox.y += em_y / delay

    for i in range(len(obj["portas"])):
        obj["portas"][i].sprite.x += em_x / delay
        obj["portas"][i].sprite.y += em_y / delay

    for i in range(len(obj["salvamentos"])):
        obj["salvamentos"][i].sprite.x += em_x / delay
        obj["salvamentos"][i].sprite.y += em_y / delay

    for i in range(len(obj["projeteis_player"])):
        obj["projeteis_player"][i].imagem.x += em_x / delay
        obj["projeteis_player"][i].imagem.y += em_y / delay

    for i in range(len(obj["projeteis_inimig"])):
        obj["projeteis_inimig"][i].imagem.x += em_x / delay
        obj["projeteis_inimig"][i].imagem.y += em_y / delay

    obj["jogador"].hitbox.x += em_x / delay
    obj["jogador"].hitbox.y += em_y / delay

    obj["cenario"].x += em_x / delay
    obj["cenario"].y += em_y / delay


def jogo(num, contrl, audio):
    # ---------------------------- DEFINIÇÕES INICIAIS ------------------------ #

    janela = Window(960, 640)

    var = open(f"Saves/{num}.csv")
    id = var.readline().strip()
    var.close()

    obj = {
        "tiles_simples": [],

        "inimigos": [],

        "portas": [],
        "salvamentos": [],

        "projeteis_player": [],
        "projeteis_inimig": [],

        "cenario": GameImage,
        "fundo": GameImage,

        "jogador": Jogador(
            0, 0,
            0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, False, False, False, False,
            False
        ),

        "npcs": []
    }

    cords = {
        "x": [],
        "y": []
    }


    carregar_sala(id, obj, cords)
    carregar_jogador(num, obj)
    camera_dinamica(444 - obj["jogador"].hitbox.x, 306 - obj["jogador"].hitbox.y, obj, 1)

    anim = "parado_esq"
    while True:
        deltatime = janela.delta_time()

        # ----------------------------- PROCESSAR ELEMENTOS ------------------------ #
        ini_anim = []
        for i in range(len(obj["inimigos"])):
            if obj["inimigos"][i] != 0:
                retorno = obj["inimigos"][i].tipo.atualizar(obj, deltatime, cords["x"], cords["y"])
                if retorno == 1:
                    obj["inimigos"][i] = 0
                ini_anim.append(retorno)
            else:
                ini_anim.append(0)

        anim = obj["jogador"].atualizar(contrl, deltatime, obj, cords["x"], cords["y"], audio[1], janela, ini_anim,
                                        anim)

        mod = 0
        for i in range(len(obj["projeteis_player"])):
            mod += obj["projeteis_player"][i - mod].atualizar(obj, deltatime)

        mod = 0
        for i in range(len(obj["projeteis_inimig"])):
            mod += obj["projeteis_inimig"][i - mod].atualizar(obj, deltatime)

        for i in range(len(obj["npcs"])):
            obj["npcs"][i].tipo.atualizar(obj, janela, contrl, teclado, audio, ini_anim, anim)

        # ------------------------------ CAMERA DINAMICA --------------------------- #
        camera_dinamica(444 - obj["jogador"].hitbox.x, 306 - obj["jogador"].hitbox.y, obj, 100)


        # ----------------------------- DESENHAR ELELEMTOS ------------------------ #
        obj["fundo"].draw()


        for i in range(len(obj["tiles_simples"])):
            obj["tiles_simples"][i].sprite.draw()

        for i in range(len(obj["tiles_ini"])):
            obj["tiles_ini"][i].sprite.draw()

        obj["cenario"].draw()

        for i in range(len(obj["portas"])):
            obj["portas"][i].sprite.draw()

        for i in range(len(obj["salvamentos"])):
            obj["salvamentos"][i].sprite.draw()

        for i in range(len(obj["inimigos"])):
            if obj["inimigos"][i] != 0:
                obj["inimigos"][i].tipo.desenhar(ini_anim[i], True)

        for i in range(len(obj["npcs"])):
            obj["npcs"][i].desenhar(obj, janela, contrl, True)

        for i in range(len(obj["projeteis_player"])):
            obj["projeteis_player"][i].desenhar()

        for i in range(len(obj["projeteis_inimig"])):
            obj["projeteis_inimig"][i].desenhar()

        obj["jogador"].desenhar(anim, janela, True)

        # ------------------------------- PASSAR DE SALA -------------------------- #
        for i in range(len(obj["portas"])):
            if obj["portas"][i].sprite.collided(obj["jogador"].hitbox) and teclado.key_pressed(contrl["abaixar"]):
                obj["jogador"].hitbox.x = obj["portas"][i].x * 32
                obj["jogador"].hitbox.y = obj["portas"][i].y * 23
                carregar_sala(obj["portas"][i].id, obj, cords)
                break

        # ---------------------------------- MORRER ------------------------------- #
        if obj["jogador"].morto:
            obj["jogador"].morto = False
            obj["jogador"].hp = obj["jogador"].hpmax
            var = open(f"Saves/{num}.csv")
            id = var.readline().strip()
            var.close()
            carregar_sala(id, obj, cords)
            carregar_jogador(num, obj)

        # ------------------------------- sair do jogo ---------------------------- #
        if obj["jogador"].sair:
            obj["jogador"].hp = obj["jogador"].hpmax
            salvar(num, obj)
            break

        # ------------------------------ ATUALIZAR JANELA -------------------------- #
        janela.update()
