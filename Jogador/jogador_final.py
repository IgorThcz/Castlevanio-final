# ------------------------------------ IMPORTAÇÕES ---------------------------------- #
from PPlay.sprite import *
from PPlay.window import *

from Jogo.Apoio_novo import *
from Menus.Botoes import Botao
from Jogador.Projéteis import Projetil_Jogador

# -------------------------------- DEFINIR ALGUMAS COISAS ------------------------- #
teclado = Window.get_keyboard()

itens_dict = {
    "0": "vazio",

    "1": "poc_cura_peq",
    "2": "poc_cura_med",
    "3": "poc_cura_gra",

    "4": "poc_mana_peq",
    "5": "poc_mana_med",
    "6": "poc_mana_gra",

    "7": "poc_comp_peq",
    "8": "poc_comp_med",
    "9": "poc_comp_gra",

    "10": "pergaminho_vel",
    "11": "pergaminho_med",
    "12": "pergaminho_nov",

    "13": "botas_relíquia",
    "14": "dinheiro"
}

magias_dict = {
    "0": "raio_arcano",
    "1": "escudo_magico",
    "2": "onda_magica",
    "3": "foco_arcano",
    "4": "foco_arcano"
}

itens_texto = {
    "1": ["Poção da Cura Pequena",
          "poção mágica pequena que aplica cura a",
          "quem a consumir,são comummente usadas",
          "em batalhas"],
    "2": ["Poção da Cura Média",
          "poção mágica média que aplica cura a",
          "quem a consumir,são comummente usadas",
          "em batalhas"],
    "3": ["Poção da Cura Grande",
          "poção mágica grande que aplica cura a",
          "quem a consumir,são comummente usadas",
          "em batalhas"],

    "4": ["Poção de Mana Pequena",
          "poção mágica pequena que recarrega mana",
          "de a quem a consumir, são comummente",
          "usadas por magos e feitiçeiros"],
    "5": ["Poção de Mana Média",
          "poção mágica média que recarrega mana",
          "de a quem a consumir, são comummente",
          "usadas por magos e feitiçeiros"],
    "6": ["Poção de Mana Grande",
          "poção grande grande que recarrega mana",
          "de a quem a consumir, são comummente",
          "usadas por magos e feitiçeiros"],

    "7": ["Poção Completa Pequena",
          "poção mágica pequena que recarrega mana",
          "e aplica cura a quem a consumir, são",
          "comummente usadas por magos e",
          "feitiçeiros em batalhas"],
    "8": ["Poção Completa Média",
          "poção mágica pequena que recarrega mana",
          "e aplica cura a quem a consumir, são",
          "comummente usadas por magos e",
          "feitiçeiros em batalhas"],
    "9": ["Poção Completa Grande",
          "poção mágica pequena que recarrega mana",
          "e aplica cura a quem a consumir, são",
          "comummente usadas por magos e",
          "feitiçeiros em batalhas"],

    "10": ["Pergaminho Velho",
           "um pergaminho usado comumente para",
           "reparode obetos, usar em sua armadura",
           "pode funcionar também, esse pergaminho",
           "está em péssimo estado"],
    "11": ["Pergaminho Amassado",
           "um pergaminho usado comumente para",
           "reparo de obetos, usar em sua armadura",
           "pode funcionar também, esse pergaminho",
           "não está tão conservado"],
    "12": ["Pergaminho Novo",
           "um pergaminho usado comumente para",
           "reparo de obetos, usar em sua armadura",
           "pode funcionar também, esse pergaminho",
           "está em ótimo estado"],

    "13": ["Botas Antigas",
           "parecem ser botas antigas que, apesar de",
           "bem sujas, parecem ter certo poder mágico,",
           "será que algém sabe algo sobre isso?"],
    "14": ["dinheiro",
           "As moedas usadas aqui são de ouro, prata",
           "e cobre. Uma moeda de prata vale 10",
           "moeda de cobre e uma moeda de ouro vale",
           "5 moedas de prata"]
}


# ----------------------- FUNÇÃO ÚTIL PARA ABRIR O INVENTÁRIO ---------------------- #

def fundo_pausado(obj, janela, contrl, ini_anim, anim):
    obj["fundo"].draw()
    obj["cenario"].draw()

    for i in range(len(obj["tiles_simples"])):
        obj["tiles_simples"][i].sprite.draw()

    for i in range(len(obj["portas"])):
        obj["portas"][i].sprite.draw()

    for i in range(len(obj["salvamentos"])):
        obj["salvamentos"][i].sprite.draw()

    for i in range(len(obj["inimigos"])):
        if obj["inimigos"][i] != 0:
            obj["inimigos"][i].tipo.desenhar(ini_anim[i], False)

    for i in range(len(obj["npcs"])):
        obj["npcs"][i].desenhar(obj, janela, contrl, False)

    for i in range(len(obj["projeteis_player"])):
        obj["projeteis_player"][i].desenhar()

    for i in range(len(obj["projeteis_inimig"])):
        obj["projeteis_inimig"][i].desenhar()

    obj["jogador"].desenhar(anim, janela, False)


# ===============================✩✩ CLASSE JOGADOR ✩✩===============================#

class Jogador:
    def __init__(self, x, y, hp_extra, dano_extra, armadura_extra, mana, armadura,
                 i0, i1, i2, i3, i4, i5, i6, i7, i8, i9, i10, i11, i12, i13, i14,
                 m_s, m0, m1, m2, m3,
                 h0
                 ):

        self.interacoes = {
            "Comerciante": False,
            "Ferreiro": False,
            "Maga": False,
            "Soldado": False
        }

        self.hitbox = GameImage("Assets/Imagens/Hitboxes/Hitbox.png")
        self.hitbox_abaixado = GameImage("Assets/Imagens/Hitboxes/Hit_Abaixado.png")
        self.dir = "esq"

        self.sair = False

        self.hitbox.x = x
        self.hitbox.y = y
        self.hitbox_abaixado.x = 0
        self.hitbox_abaixado.y = 0

        self.velx = 0
        self.vely = 0
        self.ajuste_x = 0
        self.ajuste_y = 0

        self.hpmax = 3 + hp_extra
        self.hp = self.hpmax
        self.manamax = 10
        self.mana = mana
        self.armaduramax = 1 + armadura_extra
        self.armadura = armadura

        self.hud = []
        self.cooldowns = []

        self.dano = 1 + dano_extra
        self.velocidade = 250

        self.direcao = "esq"
        self.dir_animacao = "esq"

        '''0 = dash, 1 = pulo duplo'''
        self.habilidades = [h0, True]
        self.pulado = True

        self.magia_equip = m_s
        '''
        magias:
        0 = raio
        1 = escudo
        2 = onda
        3 = foco
        '''
        self.magias = [
            m0,
            m1,
            m2,
            m3,
            False
        ]

        self.usar_item_agora = False
        self.item_selec = 0
        self.itens = [
            # nenhum item
            i0,
            # poções da cura
            i1,
            i2,
            i3,
            # poções de mana
            i4,
            i5,
            i6,
            # poções completas
            i7,
            i8,
            i9,
            # pergaminhos de reparação
            i10,
            i11,
            i12,
            # botas antigas
            i13,
            # moedas
            i14
        ]

        # ----------------------------------- CRIAÇÃO DAS ANIMAÇÕES ----------------------------- #
        self.nomes = [
            "ataque_esq",
            "ataque_dir",
            "item_esq",
            "item_dir",
            "habilidade_esq",
            "habilidade_dir",
            "queda_esq",
            "queda_dir",
            "abaixar_esq",
            "abaixar_dir",
            "pulo_esq",
            "pulo_dir",
            "corrida_esq",
            "corrida_dir",
            "parado_esq",
            "parado_dir",
        ]

        self.abaixado = False
        self.atacando = False
        self.usando_h1 = False
        self.usando_h2 = False
        self.usando_i = False
        self.correndo = False
        self.pulando = False
        self.tomando = False
        self.caindo = False
        self.usando_m = False
        self.acertado = False
        self.invencivel = False
        self.morrendo = False
        self.morto = False
        self.pulou_duplo = False

        self.recarga_ataque = 0
        self.recarga_item = 0
        self.recarga_habilidade = 0
        self.recarga_dano = 0
        self.recarga_magia = 0
        self.mana_regen = 20
        self.recarga_invenc = 0

        self.animacoes = {

            # PARADO DIREITA -------------------------------------------------------------
            "parado_dir": Sprite("Assets/Imagens/Sprites/Jogador/jogador_parado_dir.png", 4),

            # PARADO ESQUERDA ------------------------------------------------------------
            "parado_esq": Sprite("Assets/Imagens/Sprites/Jogador/jogador_parado_esq.png", 4),

            # CORRENDO ESQUERDA ----------------------------------------------------------
            "corr_esq": Sprite("Assets/Imagens/Sprites/Jogador/jogador_corrida_esq.png", 12),

            # CORRENDO DIREITA -----------------------------------------------------------
            "corr_dir": Sprite("Assets/Imagens/Sprites/Jogador/jogador_corrida_dir.png", 12),

            # PULANDO ESQUERDA -----------------------------------------------------------
            "pulo_esq": Sprite("Assets/Imagens/Sprites/Jogador/jogador_pulo_esq.png", 4),

            # PULANDO DIREITA ------------------------------------------------------------
            "pulo_dir": Sprite("Assets/Imagens/Sprites/Jogador/jogador_pulo_dir.png", 4),

            # CAINDO ESQUERDA ------------------------------------------------------------
            "caindo_esq": Sprite("Assets/Imagens/Sprites/Jogador/jogador_queda_esq.png", 1),

            # CAINDO DIREITA --------------------------------------------------------------
            "caindo_dir": Sprite("Assets/Imagens/Sprites/Jogador/jogador_queda_dir.png", 1),

            # ATACANDO ESQUERDA -----------------------------------------------------------
            "atacando_esq": Sprite("Assets/Imagens/Sprites/Jogador/jogador_ataque_esq.png", 6),

            # ATACANDO DIREITA ------------------------------------------------------------
            "atacando_dir": Sprite("Assets/Imagens/Sprites/Jogador/jogador_ataque_dir.png", 6),

            # ATACANDO ESQUERDA -----------------------------------------------------------
            "abaixar_esq": Sprite("Assets/Imagens/Sprites/Jogador/jogador_abaixar_esq.png", 1),

            # ATACANDO DIREITA ------------------------------------------------------------
            "abaixar_dir": Sprite("Assets/Imagens/Sprites/Jogador/jogador_abaixar_dir.png", 1),

            # HABILIDADE1 ESQUERDA -----------------------------------------------------------
            "habilidade1_esq": Sprite("Assets/Imagens/Sprites/Jogador/jogador_habilidade1_esq.png", 1),

            # HABILIDADE1 DIREITA ------------------------------------------------------------
            "habilidade1_dir": Sprite("Assets/Imagens/Sprites/Jogador/jogador_habilidade1_dir.png", 1),

            # HABILIDADE2 ESQUERDA -----------------------------------------------------------
            "habilidade2_esq": Sprite("Assets/Imagens/Sprites/Jogador/jogador_habilidade2_esq.png", 1),

            # HABILIDADE3 DIREITA ------------------------------------------------------------
            "habilidade2_dir": Sprite("Assets/Imagens/Sprites/Jogador/jogador_habilidade2_dir.png", 1),

            # ITEM ESQUERDA ------------------------------------------------------------------
            "item_esq": Sprite("Assets/Imagens/Sprites/Jogador/jogador_item_esq.png", 1),

            # ITEM DIREITA -------------------------------------------------------------------
            "item_dir": Sprite("Assets/Imagens/Sprites/Jogador/jogador_item_dir.png", 1),

            # DANO ESQUERDA ------------------------------------------------------------------
            "dano_esq": Sprite("Assets/Imagens/Sprites/Jogador/jogador_dano_esq.png", 4),

            # DANO DIREITA -------------------------------------------------------------------
            "dano_dir": Sprite("Assets/Imagens/Sprites/Jogador/jogador_dano_dir.png", 4),

            # MORTE ESQUERDA -----------------------------------------------------------------
            "morte_esq": Sprite("Assets/Imagens/Sprites/Jogador/jogador_morte_esq.png", 5),

            # MORTE DIREITA ------------------------------------------------------------------
            "morte_dir": Sprite("Assets/Imagens/Sprites/Jogador/jogador_morte_dir.png", 5)

        }

        self.animacoes["parado_dir"].set_total_duration(1000)
        self.animacoes["parado_esq"].set_total_duration(1000)
        self.animacoes["corr_esq"].set_total_duration(1000)
        self.animacoes["corr_dir"].set_total_duration(1000)
        self.animacoes["pulo_esq"].set_total_duration(300)
        self.animacoes["pulo_dir"].set_total_duration(300)
        self.animacoes["caindo_esq"].set_total_duration(1000)
        self.animacoes["caindo_dir"].set_total_duration(1000)
        self.animacoes["atacando_esq"].set_total_duration(500)
        self.animacoes["atacando_dir"].set_total_duration(500)
        self.animacoes["abaixar_esq"].set_total_duration(1000)
        self.animacoes["abaixar_dir"].set_total_duration(1000)
        self.animacoes["habilidade1_esq"].set_total_duration(1000)
        self.animacoes["habilidade1_dir"].set_total_duration(1000)
        self.animacoes["habilidade2_esq"].set_total_duration(1000)
        self.animacoes["habilidade2_dir"].set_total_duration(1000)
        self.animacoes["item_esq"].set_total_duration(1000)
        self.animacoes["item_dir"].set_total_duration(1000)
        self.animacoes["dano_esq"].set_total_duration(500)
        self.animacoes["dano_dir"].set_total_duration(500)
        self.animacoes["morte_esq"].set_total_duration(700)
        self.animacoes["morte_dir"].set_total_duration(700)

    # ------------------------- FUNÇÕES DE AÇÃO DO JOGADOR ------------------------------ #

    def atacar(self, obj):

        if self.direcao == "dir":
            obj["projeteis_player"].append(Projetil_Jogador(
                "Assets/Imagens/Pojéteis/area_ataque.png",
                self.hitbox.x + self.hitbox.width,
                self.hitbox.y + 6,
                0,
                self.dano,
                0,
                "Tiro"
            ))
        else:
            obj["projeteis_player"].append(Projetil_Jogador(
                "Assets/Imagens/Pojéteis/area_ataque.png",
                self.hitbox.x - 77,
                self.hitbox.y + 6,
                0,
                self.dano,
                0,
                "Tiro"
            ))

        return True

    def raio(self, obj):
        if self.direcao == "esq":
            vel = -500
        else:
            vel = 500
        if self.mana >= 3:
            self.mana -= 2
            obj["projeteis_player"].append(Projetil_Jogador(f"Assets/Imagens/Pojéteis/raio_arcano_{self.direcao}.png",
                                                            self.hitbox.x + 7, self.hitbox.y + 8, vel, 1, 10, "Tiro"))

    def onda(self, obj):
        if self.direcao == "esq":
            vel = -300
        else:
            vel = 300
        if self.mana >= 3:
            self.mana -= 3
            obj["projeteis_player"].append(Projetil_Jogador(f"Assets/Imagens/Pojéteis/onda_magica_{self.direcao}.png",
                                                            self.hitbox.x + 7, self.hitbox.y + 8, vel, 3, 10, "Onda"))

    def foco(self, obj):
        if self.direcao == "esq":
            vel = -400
        else:
            vel = 400
        if self.mana >= 5:
            self.mana -= 5
            obj["projeteis_player"].append(Projetil_Jogador(f"Assets/Imagens/Pojéteis/foco_arcano.png",
                                                            self.hitbox.x + 7, self.hitbox.y + 8, vel, 0, 10,
                                                            "Paralizante"))

    def escudo(self, obj):
        if self.direcao == "esq":
            mod = -20
        else:
            mod = 20
        if self.mana >= 2:
            self.mana -= 2
            obj["projeteis_player"].append(Projetil_Jogador(f"Assets/Imagens/Pojéteis/escudo_magico_{self.direcao}.png",
                                                            self.hitbox.x + mod, self.hitbox.y + 13, 0, 0, 10,
                                                            "Escudo"))

    # -------------------------------- FUNÇÃO GERAL ----------------------------------- #
    def atualizar(self, contrl, time, obj, lista_x, lista_y, som, janela, ini_anim, anim):

        # ------------------------------- OUTROS -------------------------------------- #
        if self.itens[self.item_selec] == 0 and not self.item_selec == 0:
            self.item_selec = 0

        # --------------------------------- HUD --------------------------------------- #

        self.hud = {
            "imagem": GameImage("Assets/Imagens/Hud/retrato_jogador.png"),

            "vida_gasta": [],
            "vida_cheia": [],

            "mana_gasta": [],
            "mana_cheia": [],

            "armadura_gasta": [],
            "armadura_cheia": [],
        }

        self.hud["imagem"].x = 0
        self.hud["imagem"].y = 0

        for i in range(self.hpmax):
            self.hud["vida_gasta"].append(GameImage("Assets/Imagens/Hud/vida_gasta.png"))
            self.hud["vida_gasta"][i].x = 74 + 30 * i
            self.hud["vida_gasta"][i].y = 39

        for i in range(self.hp):
            self.hud["vida_cheia"].append(GameImage("Assets/Imagens/Hud/vida_cheia.png"))
            self.hud["vida_cheia"][i].x = 74 + 30 * i
            self.hud["vida_cheia"][i].y = 39

        for i in range(self.manamax):
            self.hud["mana_gasta"].append(GameImage("Assets/Imagens/Hud/mana_gasta.png"))
            self.hud["mana_gasta"][i].x = 74 + 30 * i
            self.hud["mana_gasta"][i].y = 13

        for i in range(self.mana):
            self.hud["mana_cheia"].append(GameImage("Assets/Imagens/Hud/mana_cheia.png"))
            self.hud["mana_cheia"][i].x = 74 + 30 * i
            self.hud["mana_cheia"][i].y = 13

        for i in range(self.armaduramax):
            self.hud["armadura_gasta"].append(GameImage("Assets/Imagens/Hud/armadura_gasta.png"))
            self.hud["armadura_gasta"][i].x = 74 + 30 * i
            self.hud["armadura_gasta"][i].y = 65

        for i in range(self.armadura):
            self.hud["armadura_cheia"].append(GameImage("Assets/Imagens/Hud/armadura_cheia.png"))
            self.hud["armadura_cheia"][i].x = 74 + 30 * i
            self.hud["armadura_cheia"][i].y = 65

        # -------------------------------- HUD (COOLDOWNS) ---------------------------------- #

        self.cooldowns = {
            "moldura_h": GameImage("Assets/Imagens/Hud/moldura.png"),
            "moldura_m": GameImage("Assets/Imagens/Hud/moldura.png"),
            "moldura_i": GameImage("Assets/Imagens/Hud/moldura.png"),

            "habilidade": GameImage(f"Assets/Imagens/Outros/pulo_duplo.png"),
            "magia": GameImage(f"Assets/Imagens/Magias/{magias_dict[str(self.magia_equip)]}_img.png"),
            "item": GameImage(f"Assets/Imagens/Itens/{itens_dict[str(self.item_selec)]}.png"),

            "indisponivel_h": GameImage(f"Assets/Imagens/Hud/indisponivel.png"),
            "indisponivel_m": GameImage(f"Assets/Imagens/Hud/indisponivel.png"),
            "indisponivel_i": GameImage(f"Assets/Imagens/Hud/indisponivel.png"),
        }

        if self.habilidades[0]:
            self.cooldowns["habilidade"] = GameImage(f"Assets/Imagens/Outros/dash.png")
        else:
            self.cooldowns["habilidade"] = GameImage(f"Assets/Imagens/Hud/bloqueado.png")

        if self.magia_equip == 4:
            self.cooldowns["magia"] = GameImage(f"Assets/Imagens/Hud/bloqueado.png")

        self.cooldowns["moldura_h"].x = 726
        self.cooldowns["moldura_h"].y = 6

        self.cooldowns["moldura_m"].x = 804
        self.cooldowns["moldura_m"].y = 6

        self.cooldowns["moldura_i"].x = 882
        self.cooldowns["moldura_i"].y = 6

        self.cooldowns["habilidade"].x = 732
        self.cooldowns["habilidade"].y = 12

        self.cooldowns["magia"].x = 810
        self.cooldowns["magia"].y = 12

        self.cooldowns["item"].x = 886
        self.cooldowns["item"].y = 10

        self.cooldowns["indisponivel_h"].x = 732
        self.cooldowns["indisponivel_h"].y = 12

        self.cooldowns["indisponivel_m"].x = 810
        self.cooldowns["indisponivel_m"].y = 12

        self.cooldowns["indisponivel_i"].x = 888
        self.cooldowns["indisponivel_i"].y = 12

        # ------------------------------ CHECAGEM DE COLISÕES ------------------------------- #
        colisoes = {
            "Teto": False,
            "Esquerda": False,
            "Direita": False,
            "Chão": False
        }


        for i in range(len(obj["tiles_simples"])):
            if self.hitbox.collided(obj["tiles_simples"][i].sprite):
                direcao = obj["tiles_simples"][i].identificar_lado(obj["jogador"].hitbox)

                ilusao = False
                for j in range(len(lista_x)):

                    if direcao == "Chão" and int(lista_x[i]) == int(lista_x[j]) \
                            and int(lista_y[i]) == int(lista_y[j]) + 1:
                        ilusao = True
                        break

                    elif direcao == "Teto" and int(lista_x[i]) == int(lista_x[j]) \
                            and int(lista_y[i]) == int(lista_y[j]) - 1:
                        ilusao = True
                        break

                    elif direcao == "Esquerda" and int(lista_x[i]) == int(lista_x[j]) - 1 \
                            and int(lista_y[i]) == int(lista_y[j]):
                        ilusao = True
                        break

                    elif direcao == "Direita" and int(lista_x[i]) == int(lista_x[j]) + 1 \
                            and int(lista_y[i]) == int(lista_y[j]):
                        ilusao = True
                        break

                if not ilusao:
                    colisoes[direcao] = True

        # DIREÇÃO --------------------------------------------------
        if teclado.key_pressed(contrl["direita"]) and not teclado.key_pressed(contrl["esquerda"]):
            self.direcao = "dir"
        if teclado.key_pressed(contrl["esquerda"]) and not teclado.key_pressed(contrl["direita"]):
            self.direcao = "esq"

        # ----------------------------------- CONTINUIDADE --------------------------------- #
        '''TEMPO DE RECARDA REDUZIDO PARA EFETIVAMENTE TERMINAR A AÇÃO'''

        travado = False

        if self.recarga_ataque > 0:
            self.recarga_ataque -= time
            travado = True
            if self.recarga_ataque <= 0.5:
                self.atacando = False
                travado = False

        if self.recarga_item > 0:
            self.recarga_item -= time
            travado = True
            if self.recarga_item <= 7.5:
                self.usando_i = False
                travado = False

        if self.recarga_magia > 0:
            self.recarga_magia -= time
            travado = True
            if self.recarga_magia <= 6.5:
                self.usando_m = False
                travado = False

        if self.recarga_habilidade > 0:
            self.recarga_habilidade -= time
            if self.habilidades[0]:
                travado = True
            if self.recarga_habilidade <= 4.7 and self.habilidades[0]:
                self.usando_h1 = False
                travado = False
            elif self.recarga_habilidade <= 5 and self.habilidades[1]:
                self.usando_h2 = False

        if self.morrendo:
            travado = True
            if self.animacoes[f"morte_{self.direcao}"].get_curr_frame() == 4:
                self.morrendo = False
                travado = False
                self.morto = True
                self.hp = self.hpmax

        if self.recarga_dano > 0:
            self.recarga_dano -= time
            travado = True
            if self.recarga_dano <= 0:
                self.tomando = False
                travado = False

        if self.tomando and not self.morrendo:
            travado = True
            if self.animacoes[f"dano_{self.direcao}"].get_curr_frame() == 3:
                travado = False
                self.tomando = False

        if self.recarga_invenc > 0:
            self.recarga_invenc -= time
            if self.recarga_invenc <= 0:
                self.invencivel = False

        # -------------------------------- AÇÕES COM RECARGA --------------------------------- #
        '''TEMPO DE TECARGA CHEIO PARA LIMITAR O USO DAS AÇÕES'''

        # ATACAR
        if teclado.key_pressed(contrl["atacar"]) and self.recarga_ataque <= 0:
            self.atacar(obj)
            self.animacoes[f"atacando_{self.direcao}"].set_curr_frame(0)
            self.atacando = True
            self.recarga_ataque = 1
            travado = True
            self.dir_animacao = self.direcao

        # USAR ITEM
        if (teclado.key_pressed(contrl["item"]) or self.usar_item_agora) \
                and self.recarga_item <= 0 and self.vely == 0 and not travado:
            self.dir_animacao = self.direcao
            self.item()
            self.usando_i = True
            self.recarga_item = 8
            travado = True
        self.usar_item_agora = False

        # USAR MAGIA
        if teclado.key_pressed(contrl["magia"]) and self.recarga_magia <= 0 and not travado and self.magia_equip != 4:
            self.dir_animacao = self.direcao
            if self.magia_equip == 0:
                self.raio(obj)
            elif self.magia_equip == 1:
                self.escudo(obj)
            elif self.magia_equip == 2:
                self.onda(obj)
            elif self.magia_equip == 3:
                self.foco(obj)
            self.usando_m = True
            self.recarga_magia = 7
            travado = True

        # PULO DUPLO --- (baseado em h2, pois era uma habilidade) ---
        if colisoes["Chão"]:
            self.pulou_duplo = False
        if teclado.key_pressed(contrl["pular"]) and not colisoes["Chão"] and not self.pulou_duplo and not self.pulado:
            self.pulado = True
            self.pulou_duplo = True
            self.usando_h2 = True
        else:
            self.usando_h2 = False

        # USAR HABILIDADE
        if teclado.key_pressed(contrl["habilidade"]) and self.recarga_habilidade <= 0 and not travado:
            if self.habilidades[0]:
                self.dir_animacao = self.direcao
                self.vely = 0
                self.usando_h1 = True
                self.recarga_habilidade = 5
                travado = True

        # TOMAR DANO
        '''TIRAR ISSO AQUI DEPOIS QUE OS INIMIGOS JA CONSEGUIREM CAUSAR DANO'''
        if teclado.key_pressed("p") and self.recarga_dano <= 0:
            if not self.tomando:
                self.hp -= 1
            self.tomando = True
            self.recarga_dano = 0.5
            travado = True

        # ----------------------------- AÇÕES SEM RECARGA --------------------------- #

        # MORRER
        if self.hp == 0 and not self.morrendo:
            print("passou")
            travado = True
            self.morrendo = True
            self.animacoes[f"morte_{self.direcao}"].set_curr_frame(0)

        '''repare que para o jogador não ser combado e ficar imobilizado, ser acertado garante um pouco de
        invencibilidade a ele, isso não pode ser esquecido ao projetar a função de causar dano dos projéteis
        dos inimigos'''

        # TOMAR DANO
        if self.acertado:
            self.hp -= 1
            self.invencivel = True
            self.recarga_invenc = 2
            self.animacoes[f"dano_{self.direcao}"].set_curr_frame(0)
            self.acertado = False
            self.tomando = True
            travado = True

        # ABAIXAR
        self.abaixado = False
        if teclado.key_pressed(contrl["abaixar"]) and self.vely == 0 and not travado:
            self.hitbox_abaixado.x = self.hitbox.x
            self.hitbox_abaixado.y = self.hitbox.y + 23
            self.abaixado = True
            travado = True

        # ---------------------------- AÇÕES DE MOVIMENTAÇÃO ------------------------ #

        # MOVIMENTO HORIZONTAL
        self.velx = 0
        self.correndo = False
        if not travado and not self.usando_h1 and not self.atacando:
            if teclado.key_pressed(contrl["direita"]) and teclado.key_pressed(contrl["esquerda"]):
                self.velx = 0
            elif teclado.key_pressed(contrl["esquerda"]) and not colisoes["Esquerda"]:
                self.velx = -250 * time
                self.correndo = True
            elif teclado.key_pressed(contrl["direita"]) and not colisoes["Direita"]:
                self.velx = 250 * time
                self.correndo = True
            self.hitbox.x += self.velx

        # MOVIIMENTO HORIZONTAL (HABILIDADE 1)
        if self.usando_h1 and self.dir_animacao == "esq" and not colisoes["Esquerda"]:
            self.velx = - 600 * time
            self.hitbox.x += self.velx
        if self.usando_h1 and self.dir_animacao == "dir" and not colisoes["Direita"]:
            self.velx = 600 * time
            self.hitbox.x += self.velx

        # MOVIMENTO VERTICAL
        gravidade = 3000

        if colisoes["Chão"] and self.vely >= 0:
            self.vely = 0
            self.pulando = False
            self.caindo = False
            if teclado.key_pressed(contrl["pular"]) and not travado and not self.pulado:
                self.pulado = True
                self.animacoes[f"pulo_{self.direcao}"].set_curr_frame(0)
                self.vely = -700
                self.hitbox.y += self.vely * time + gravidade * -.5 * time * time

        if colisoes["Teto"] and self.vely <= 0:
            self.vely = 0
            self.hitbox.y += 1

        if self.usando_h2 and not colisoes["Chão"]:
            self.vely = -700

        if ((not colisoes["Chão"] or (colisoes["Chão"] and self.vely < 0))
                and not self.usando_h1 and not time > 1):
            self.vely += time * gravidade
            if self.vely > 1000:
                self.vely = 1000
            self.hitbox.y += self.vely * time + gravidade * -.5 * time * time

            if self.vely >= 0:
                self.caindo = True
            else:
                self.pulando = True

        # ------------------------------- CONTROLE DO PULO -------------------------------- #

        if self.pulado and not teclado.key_pressed(contrl["pular"]):
            self.pulado = False

        # -------------------------------- RECUPERAR MANA --------------------------------- #
        self.mana_regen -= time
        if self.mana_regen <= 0:
            self.mana_regen = 20
            if self.mana < self.manamax:
                self.mana += 1

        # -------------------------------- AÇÕES PAUSANTES -------------------------------- #

        # PAUSAR ----------------------------------------------------------------------------

        sair = False
        if teclado.key_pressed(contrl["pausa"]):

            # mouse
            mouse = Window.get_mouse()

            # caixa
            caixa = GameImage("Assets/Imagens/Menus/Botoes/caixa_pausa.png")
            caixa.x = 376
            caixa.y = 224

            # boão sair
            bot_sair = Botao("Botoes/bot_sair(jogo)", 380, 338)

            # botão continuar
            bot_continuar = Botao("Botoes/bot_continuar", 380, 268)

            clicado = True
            while True:

                if mouse.is_button_pressed(1) and not clicado:

                    if mouse.is_over_object(bot_continuar.image) or sair:
                        break

                    if mouse.is_over_object(bot_sair.image):

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
                                    pygame.time.delay(250)
                                    break

                                if mouse.is_over_object(bot_sim.image):
                                    sair = True
                                    pygame.time.delay(250)
                                    break

                            if mouse.is_button_pressed(1):
                                clicado_outro = True
                            else:
                                clicado_outro = False

                            caixa_confirm.draw()

                            bot_sim.desenhar(som)
                            bot_nao.desenhar(som)

                            janela.update()

                    if mouse.is_over_object(bot_continuar.image) or sair:
                        break

                if mouse.is_button_pressed(1):
                    clicado = True
                else:
                    clicado = False

                caixa.draw()

                bot_continuar.desenhar(som)
                bot_sair.desenhar(som)

                janela.update()

            if sair:
                self.sair = True

        # ABRIR MAPA ------------------------------------------------------------------------

        # ABRIR MOCHILA ---------------------------------------------------------------------

        if teclado.key_pressed(contrl["mochila"]):
            mouse = Window.get_mouse()

            # itens no inventário
            itens = []
            x = 352
            y = 218
            for i in range(len(self.itens)):

                ''' essa primeira condição não testa se a quantidade do item é 0,
                quando i == 1, isso significao item inexistente'''
                if i == 0:
                    itens.append(GameImage(f"Assets/Imagens/Itens/{itens_dict["1"]}.png"))
                    itens[i].x = -64
                    itens[i].y = -64

                elif self.itens[i] > 0:
                    itens.append(GameImage(f"Assets/Imagens/Itens/{itens_dict[str(i)]}.png"))
                    itens[i].x = x
                    itens[i].y = y
                    if x >= 352 + 3 * 64:
                        x = 352
                        y += 64
                    else:
                        x += 64
                else:
                    itens.append(GameImage(f"Assets/Imagens/Itens/{itens_dict["1"]}.png"))
                    itens[i].x = -64
                    itens[i].y = -64

            # caixa do inventário
            inventario = GameImage("Assets/Imagens/Outros/mochila.png")
            inventario.x = 280
            inventario.y = 58

            # botão usar agora
            bot_usar = Botao("Botoes/bot_usar_agora", 280, 492)

            # botão selecionar
            bot_selec = Botao("Botoes/bot_escolher_item", 482, 492)

            # botão fechar inventário
            bot_fechar = Botao("Botoes/fechar_mochila", 216, 82)

            # indicadores do inventário
            item_selecionado = GameImage("Assets/Imagens/Outros/selecionado.png")
            item_mostrando = GameImage("Assets/Imagens/Outros/mostrando.png")
            item_sobre = GameImage("Assets/Imagens/Outros/mouse_sobre.png")

            # legenda sobre os indicadores
            legenda = GameImage("Assets/Imagens/Outros/legenda.png")
            legenda.x = 684
            legenda.y = 82

            principal = 0

            while True:

                # clicar nas coisas:

                if mouse.is_button_pressed(1):

                    for i in range(len(itens)):
                        if mouse.is_over_object(itens[i]):
                            principal = itens[i]

                    if mouse.is_over_object(bot_fechar.image):
                        break

                    if (mouse.is_over_object(bot_selec.image) and principal != 0
                            and itens.index(principal) <= 12):
                        self.item_selec = itens.index(principal)

                    if (mouse.is_over_object(bot_usar.image) and principal != 0
                            and itens.index(principal) <= 12):
                        self.item_selec = itens.index(principal)
                        self.usar_item_agora = True
                        break

                # desenhar as coisas

                fundo_pausado(obj, janela, contrl, ini_anim, anim)

                inventario.draw()
                for i in range(len(itens)):
                    if itens[i] is not None:
                        itens[i].draw()

                        if mouse.is_over_object(itens[i]):
                            item_sobre.x = itens[i].x
                            item_sobre.y = itens[i].y
                            item_sobre.draw()

                        elif i == self.item_selec:
                            item_selecionado.x = itens[i].x
                            item_selecionado.y = itens[i].y
                            item_selecionado.draw()

                        elif itens[i] == principal:
                            item_mostrando.x = itens[i].x
                            item_mostrando.y = itens[i].y
                            item_mostrando.draw()

                        janela.draw_text(f"x{self.itens[i]}", itens[i].x + 40, itens[i].y + 40, 20,
                                         (0, 0, 0), "Arial", False, False)

                if principal != 0:
                    destaque = GameImage(f"Assets/Imagens/Itens/{itens_dict[str(itens.index(principal))]}_aum.png")
                    destaque.x = 290
                    destaque.y = 92
                    destaque.draw()
                    janela.draw_text(f"{itens_texto[str(itens.index(principal))][0]}", 426, 100, 20,
                                     (224, 132, 132), "Arial", True, False)
                    for i in range(len(itens_texto[str(itens.index(principal))]) - 1):
                        janela.draw_text(f"{itens_texto[str(itens.index(principal))][i + 1]}", 426, 130 + 15 * i, 15,
                                         (0, 0, 0), "Arial", False, False)

                bot_usar.desenhar(som)
                bot_fechar.desenhar(som)
                bot_selec.desenhar(som)

                legenda.draw()
                janela.draw_text("Item Escolhido", 684, 146, 40,
                                 (234, 232, 201), "Arial", False, False)
                janela.draw_text("Item Mostrado", 684, 274, 40,
                                 (234, 232, 201), "Arial", False, False)
                janela.draw_text("Item sob o mouse", 684, 402, 40,
                                 (234, 232, 201), "Arial", False, False)

                # atualizar janela

                janela.update()

        # RETORNAR ANIMAÇÃO EM ORDEM DE PRIORIDADE

        if self.morrendo:
            return f"morte_{self.direcao}"
        elif self.tomando:
            return f"dano_{self.direcao}"
        elif self.atacando:
            return f"atacando_{self.dir_animacao}"
        elif self.usando_i:
            return f"item_{self.dir_animacao}"
        elif self.usando_h1:
            return f"habilidade1_{self.dir_animacao}"
        elif self.usando_h2:
            return f"habilidade2_{self.direcao}"
        elif self.caindo:
            return f"caindo_{self.direcao}"
        elif self.pulando:
            return f"pulo_{self.direcao}"
        elif self.correndo:
            return f"corr_{self.direcao}"
        elif self.abaixado:
            return f"abaixar_{self.direcao}"
        else:
            return f"parado_{self.direcao}"

    # FAZER A ANIMAÇÃO---------------------
    def desenhar(self, anim, janela, mov):

        self.animacoes[f"{anim}"].x = self.hitbox.x - 82
        self.animacoes[f"{anim}"].y = self.hitbox.y - 120
        if mov:
            self.animacoes[f"{anim}"].update()
        self.hitbox.draw()
        self.animacoes[f"{anim}"].draw()
        if self.abaixado:
            self.hitbox_abaixado.draw()

        if not self.hud == 0:

            self.hud["imagem"].draw()

            for i in range(len(self.hud["vida_gasta"])):
                self.hud["vida_gasta"][i].draw()

            for i in range(len(self.hud["vida_cheia"])):
                self.hud["vida_cheia"][i].draw()

            for i in range(len(self.hud["mana_gasta"])):
                self.hud["mana_gasta"][i].draw()

            for i in range(len(self.hud["mana_cheia"])):
                self.hud["mana_cheia"][i].draw()

            for i in range(len(self.hud["armadura_gasta"])):
                self.hud["armadura_gasta"][i].draw()

            for i in range(len(self.hud["armadura_cheia"])):
                self.hud["armadura_cheia"][i].draw()

        self.cooldowns["moldura_h"].draw()
        self.cooldowns["moldura_m"].draw()
        self.cooldowns["moldura_i"].draw()

        self.cooldowns["habilidade"].draw()
        self.cooldowns["magia"].draw()
        self.cooldowns["item"].draw()

        # TEXTOS DA HABILIDADE -------------------------
        if not (self.habilidades[0] == self.habilidades[1] == False or self.recarga_habilidade <= 0):
            self.cooldowns["indisponivel_h"].draw()
            janela.draw_text(f"{int(self.recarga_habilidade) + 1}", 732 + 15, 12 - 5, 60,
                             (224, 132, 132), "Arial", True, False)

        # TEXTOS DA MAGIA -------------------------------
        if not self.recarga_magia <= 0:
            self.cooldowns["indisponivel_m"].draw()
            janela.draw_text(f"{int(self.recarga_magia) + 1}", 810 + 15, 12 - 5, 60,
                             (224, 132, 132), "Arial", True, False)

        # TEXTO DO ITEM ----------------------------------
        if not self.recarga_item <= 0:
            self.cooldowns["indisponivel_i"].draw()
            janela.draw_text(f"{int(self.recarga_item) + 1}", 888 + 15, 12 - 5, 60,
                             (224, 132, 132), "Arial", True, False)

    # ----------------------------------- ITENS ------------------------------- #
    def pocao_cura(self, tamanho):
        self.hp += tamanho
        if self.hp > self.hpmax:
            self.hp = self.hpmax

    def pocao_mana(self, tamanho):
        self.mana += tamanho
        if self.mana > self.manamax:
            self.mana = self.manamax

    def pocao_completa(self, tamanho):
        self.hp += tamanho
        if self.hp > self.hpmax:
            self.hp = self.hpmax
        self.mana += tamanho
        if self.mana > self.manamax:
            self.mana = self.manamax

    def pergaminho_reparo(self, qualidade):
        self.armadura += qualidade
        if self.armadura > self.armaduramax:
            self.armadura = self.armaduramax

    def item(self):

        if self.item_selec == 0:
            pass

        elif self.item_selec == 1:
            self.itens[self.item_selec] -= 1
            self.pocao_cura(1)
        elif self.item_selec == 2:
            self.itens[self.item_selec] -= 1
            self.pocao_cura(2)
        elif self.item_selec == 3:
            self.itens[self.item_selec] -= 1
            self.pocao_cura(3)

        elif self.item_selec == 4:
            self.itens[self.item_selec] -= 1
            self.pocao_mana(1)
        elif self.item_selec == 5:
            self.itens[self.item_selec] -= 1
            self.pocao_mana(2)
        elif self.item_selec == 6:
            self.itens[self.item_selec] -= 1
            self.pocao_mana(3)

        elif self.item_selec == 7:
            self.itens[self.item_selec] -= 1
            self.pocao_completa(1)
        elif self.item_selec == 8:
            self.itens[self.item_selec] -= 1
            self.pocao_completa(2)
        elif self.item_selec == 9:
            self.itens[self.item_selec] -= 1
            self.pocao_completa(3)

        elif self.item_selec == 10:
            self.itens[self.item_selec] -= 1
            self.pergaminho_reparo(1)
        elif self.item_selec == 11:
            self.itens[self.item_selec] -= 1
            self.pergaminho_reparo(2)
        elif self.item_selec == 12:
            self.itens[self.item_selec] -= 1
            self.pergaminho_reparo(3)
