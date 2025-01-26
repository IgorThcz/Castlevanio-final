import pygame.time

from PPlay.gameimage import *
from PPlay.sprite import *
from Inimigosvanio.Projéteis import *
import random


class Goblin:
    def __init__(self, index, x, y):

        self.index = index

        self.hitbox = GameImage("Assets/Imagens/Hitboxes/Hitbox.png")
        self.hitbox.x = x * 32
        self.hitbox.y = y * 32

        self.velx = 100
        self.vely = 0
        self.dir = -1
        self.direcao = "esq"

        self.hp = 5
        self.paralizado = False
        self.tomando_dano = False

        self.pulso_visao = 0
        self.vendo = False
        self.desver = 0

        self.pulso_ataque = 0
        self.atacando = False
        self.prepataque = False
        self.atacou = False
        self.andando = False
        self.invulneravel = False

        self.animacoes = {
            "andando_esq": Sprite("Assets/Imagens/Sprites/Inimigos/Goblin/andando_esq.png", 8),
            "andando_dir": Sprite("Assets/Imagens/Sprites/Inimigos/Goblin/andando_dir.png", 8),
            "pulando_esq": Sprite("Assets/Imagens/Sprites/Inimigos/Goblin/pulando_esq.png", 3),
            "pulando_dir": Sprite("Assets/Imagens/Sprites/Inimigos/Goblin/pulando_dir.png", 3),
            "tomando_esq": Sprite("Assets/Imagens/Sprites/Inimigos/Goblin/tomando_esq.png", 4),
            "tomando_dir": Sprite("Assets/Imagens/Sprites/Inimigos/Goblin/tomando_dir.png", 4),
            "atacando_esq": Sprite("Assets/Imagens/Sprites/Inimigos/Goblin/atacando_esq.png", 4),
            "atacando_dir": Sprite("Assets/Imagens/Sprites/Inimigos/Goblin/atacando_dir.png", 4),
            "morrendo_esq": Sprite("Assets/Imagens/Sprites/Inimigos/Goblin/morrendo_esq.png", 10),
            "morrendo_dir": Sprite("Assets/Imagens/Sprites/Inimigos/Goblin/morrendo_dir.png", 10),
            "caindo_esq": Sprite("Assets/Imagens/Sprites/Inimigos/Goblin/caindo_esq.png", 1),
            "caindo_dir": Sprite("Assets/Imagens/Sprites/Inimigos/Goblin/caindo_dir.png", 1),
            "parado_esq": Sprite("Assets/Imagens/Sprites/Inimigos/Goblin/parado_esq.png", 4),
            "parado_dir": Sprite("Assets/Imagens/Sprites/Inimigos/Goblin/parado_dir.png", 4)
        }

        self.animacoes["andando_esq"].set_total_duration(1000)
        self.animacoes["andando_dir"].set_total_duration(1000)
        self.animacoes["pulando_esq"].set_total_duration(1000)
        self.animacoes["pulando_dir"].set_total_duration(1000)
        self.animacoes["tomando_esq"].set_total_duration(1000)
        self.animacoes["tomando_dir"].set_total_duration(1000)
        self.animacoes["atacando_esq"].set_total_duration(300)
        self.animacoes["atacando_dir"].set_total_duration(300)
        self.animacoes["morrendo_esq"].set_total_duration(1000)
        self.animacoes["morrendo_dir"].set_total_duration(1000)
        self.animacoes["caindo_esq"].set_total_duration(1000)
        self.animacoes["caindo_dir"].set_total_duration(1000)
        self.animacoes["parado_esq"].set_total_duration(800)
        self.animacoes["parado_dir"].set_total_duration(800)

    def atualizar(self, obj, time, lista_x, lista_y):

        if self.velx > 0:
            self.direcao = "dir"
        elif self.velx < 0:
            self.direcao = "esq"

        colisoes = {
            "Teto": 0,
            "Esquerda": 0,
            "Direita": 0,
            "Chão": 0
        }

        colidiu = False
        for i in range(len(obj["tiles_ini"])):
            if self.hitbox.collided(obj["tiles_ini"][i].sprite):
                colidiu = True

        for i in range(len(obj["tiles_simples"])):
            if self.hitbox.collided(obj["tiles_simples"][i].sprite):
                direcao = obj["tiles_simples"][i].identificar_lado(self.hitbox)

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
                    colisoes[direcao] += 1

        '''verificar se está perto o suficiente do jogador para poder parar de andar'''
        perto = False
        if self.vendo and - 70 <= (self.hitbox.x + self.hitbox.width) - (
                obj["jogador"].hitbox.x + obj["jogador"].hitbox.width) <= 70:
            perto = True

        # ATACAR ------------------------------------------------------------------------------------

        if self.pulso_ataque > 0:
            self.pulso_ataque -= time

        if self.prepataque:
            if self.pulso_ataque <= 2.5:
                self.atacando = True
                self.prepataque = False

        if self.atacando:
            self.pulso_ataque -= time
            if self.pulso_ataque <= 2:
                self.atacando = False

        if self.pulso_ataque <= 0 and perto:
            self.prepataque = True
            self.atacou = False
            self.pulso_ataque = 3

        if self.atacando and not self.atacou:
            self.atacou = True
            if self.direcao == "esq":
                obj["projeteis_inimig"].append(Projetil_Inimigo(
                    "Assets/Imagens/Pojéteis/goblin_ataque.png",
                    self.hitbox.x - 61,
                    self.hitbox.y + 12,
                    0,
                    1,
                    0,
                    "Tiro",
                    self.index
                ))
            else:
                obj["projeteis_inimig"].append(Projetil_Inimigo(
                    "Assets/Imagens/Pojéteis/goblin_ataque.png",
                    self.hitbox.x - 61,
                    self.hitbox.y + 12,
                    0,
                    1,
                    0,
                    "Tiro",
                    self.index
                ))

        # ANDAR DE UM LADO PARA O OUTRO --------------------------------------------------------------

        # visão --------------------------------
        if self.desver <= 0:
            self.desver = 2
            self.vendo = False
        if self.vendo:
            self.desver -= time
            if obj["jogador"].hitbox.x + obj["jogador"].hitbox.width / 2 < self.hitbox.x + self.hitbox.width / 2:
                self.dir = -1
            else:
                self.dir = 1

        # padrão ------------------------------
        naparede = False
        if ((self.velx > 0 and colisoes["Direita"] >= 1)
                or (self.velx < 0 and colisoes["Esquerda"] >= 1)):
            naparede = True
        if (((self.velx > 0 and colisoes["Direita"] > 1) or (self.velx < 0 and colisoes["Esquerda"] > 1))
                and not self.vendo) or colidiu:
            self.dir *= -1
        self.velx = 100 * time * self.dir
        if not naparede and not time >= 1 and not self.paralizado and not self.tomando_dano \
                and not (self.prepataque or self.atacando) and not perto:
            self.andando = True
            self.hitbox.x += self.velx
        else:
            self.andando = False

        # VISÃO ------------------------ (via pojétil) --------------------------------------------------

        self.pulso_visao -= time
        if self.pulso_visao <= 0:
            self.pulso_visao = 0.2
            obj["projeteis_inimig"].append(Projetil_Inimigo(
                "Assets/Imagens/Pojéteis/visao.png",
                self.hitbox.x + self.hitbox.width / 2,
                self.hitbox.y + self.hitbox.height / 2,
                1000,
                0,
                0.2,
                "Visão",
                self.index
            ))
            obj["projeteis_inimig"].append(Projetil_Inimigo(
                "Assets/Imagens/Pojéteis/visao.png",
                self.hitbox.x + self.hitbox.width / 2,
                self.hitbox.y + self.hitbox.height / 2,
                -1000,
                0,
                0.2,
                "Visão",
                self.index
            ))

        # MOVIMENTAÇÃO VERTICAL -------------------------------------------------------------------------
        gravidade = 3000

        if (colisoes["Esquerda"] == 1 or colisoes["Direita"] == 1) and not self.tomando_dano:
            self.animacoes[f"pulando_{self.direcao}"].set_curr_frame(0)
            self.vely = -500
            self.hitbox.y += self.vely * time + gravidade * -.5 * time * time

        if colisoes["Teto"] >= 1 and self.vely <= 0:
            self.vely = 0
            self.hitbox.y += 1

        if colisoes["Chão"] >= 1 and self.vely >= 0:
            self.vely = 0

        if (colisoes["Chão"] == 0 or (colisoes["Chão"] >= 1 and self.vely < 0)) and not time > 1:
            self.vely += time * gravidade
            if self.vely > 1000:
                self.vely = 1000
            self.hitbox.y += self.vely * time + gravidade * -.5 * time * time

        # MORRER ------------------------------------------------------------------------------------
        tirar = False
        if self.hp <= 0 and self.animacoes[
            f"morrendo_{self.direcao}"].get_curr_frame() == 9:  # varia de inimigo para inimigo
            self.animacoes[f"morrendo_{self.direcao}"].set_curr_frame(0)
            tirar = True

            # dropar
            moedas = int(random.random() * 15) + 16
            sorteio = int(random.random() + 100) + 1
            if sorteio <= 5 and (obj["jogador"][14] == 1 or obj["jogador"].habilidades[1]):
                obj["jogador"].itens[13] += 1
            else:
                obj["jogador"].itens[14] += moedas

        # TOMAR DANO --------------------------------------------------------------------------------
        if self.tomando_dano and self.animacoes[
            f"tomando_{self.direcao}"].get_curr_frame() == 3:  # varia de inimigo para inimigo
            self.animacoes[f"tomando_{self.direcao}"].set_curr_frame(0)
            self.tomando_dano = False

        # ESCOLHER ANIMAÇÃO -------------------------------------------------------------------------

        if tirar:
            return 1
        elif self.hp <= 0:
            return f"morrendo_{self.direcao}"
        elif self.atacando:
            return f"atacando_{self.direcao}"
        elif self.vely < 0 and not self.tomando_dano:
            return f"pulando_{self.direcao}"
        elif self.vely > 0 and not self.tomando_dano:
            return f"caindo_{self.direcao}"
        elif self.tomando_dano:
            return f"tomando_{self.direcao}"
        elif self.andando:
            return f"andando_{self.direcao}"
        else:
            return f"parado_{self.direcao}"

    def desenhar(self, anim, mov):

        self.animacoes[f"{anim}"].x = self.hitbox.x - 61
        self.animacoes[f"{anim}"].y = self.hitbox.y - 18
        if mov:
            self.animacoes[f"{anim}"].update()
        self.hitbox.draw()
        self.animacoes[f"{anim}"].draw()


class Esqueleto:
    def __init__(self, index, x, y):

        self.index = index

        self.hitbox = GameImage("Assets/Imagens/Hitboxes/hitbox_esqueleto.png")
        self.hitbox.x = x * 32
        self.hitbox.y = y * 32

        self.velx = 100
        self.vely = 0
        self.dir = -1
        self.direcao = "esq"

        self.hp = 5
        self.paralizado = False
        self.tomando_dano = False

        self.pulso_visao = 0
        self.vendo = False
        self.desver = 0

        self.pulso_ataque = 0
        self.atacando = False
        self.prepataque = False
        self.atacou = False
        self.andando = False
        self.defendendo = False
        self.invulneravel = False

        self.animacoes = {
            "andando_esq": Sprite("Assets/Imagens/Sprites/Inimigos/Esqueleto/andando_esq.png", 4),   # ok
            "andando_dir": Sprite("Assets/Imagens/Sprites/Inimigos/Esqueleto/andando_dir.png", 4),   # ok
            "pulando_esq": Sprite("Assets/Imagens/Sprites/Inimigos/Esqueleto/parado_esq.png", 5),    # ok
            "pulando_dir": Sprite("Assets/Imagens/Sprites/Inimigos/Esqueleto/parado_dir.png", 5),    # ok
            "tomando_esq": Sprite("Assets/Imagens/Sprites/Inimigos/Esqueleto/tomando_esq.png", 5),   # ok
            "tomando_dir": Sprite("Assets/Imagens/Sprites/Inimigos/Esqueleto/tomando_dir.png", 5),   # ok
            "atacando_esq": Sprite("Assets/Imagens/Sprites/Inimigos/Esqueleto/atacando_esq.png", 4), # ok
            "atacando_dir": Sprite("Assets/Imagens/Sprites/Inimigos/Esqueleto/atacando_dir.png", 4), # ok
            "morrendo_esq": Sprite("Assets/Imagens/Sprites/Inimigos/Esqueleto/morrendo_esq.png", 8), # ok
            "morrendo_dir": Sprite("Assets/Imagens/Sprites/Inimigos/Esqueleto/morrendo_dir.png", 8), # ok
            "caindo_esq": Sprite("Assets/Imagens/Sprites/Inimigos/Esqueleto/parado_esq.png", 5),     # ok
            "caindo_dir": Sprite("Assets/Imagens/Sprites/Inimigos/Esqueleto/parado_dir.png", 5),     # ok
            "parado_esq": Sprite("Assets/Imagens/Sprites/Inimigos/Esqueleto/parado_esq.png", 5),     # ok
            "parado_dir": Sprite("Assets/Imagens/Sprites/Inimigos/Esqueleto/parado_dir.png", 5),     # ok
            "defendendo_esq": Sprite("Assets/Imagens/Sprites/Inimigos/Esqueleto/defesa_esq.png", 4), # ok
            "defendendo_dir": Sprite("Assets/Imagens/Sprites/Inimigos/Esqueleto/defesa_dir.png", 4)  # ok
        }

        self.animacoes["andando_esq"].set_total_duration(500)
        self.animacoes["andando_dir"].set_total_duration(500)
        self.animacoes["pulando_esq"].set_total_duration(1000)
        self.animacoes["pulando_dir"].set_total_duration(1000)
        self.animacoes["tomando_esq"].set_total_duration(1000)
        self.animacoes["tomando_dir"].set_total_duration(1000)
        self.animacoes["atacando_esq"].set_total_duration(500)
        self.animacoes["atacando_dir"].set_total_duration(500)
        self.animacoes["morrendo_esq"].set_total_duration(1000)
        self.animacoes["morrendo_dir"].set_total_duration(1000)
        self.animacoes["caindo_esq"].set_total_duration(1000)
        self.animacoes["caindo_dir"].set_total_duration(1000)
        self.animacoes["parado_esq"].set_total_duration(800)
        self.animacoes["parado_dir"].set_total_duration(800)
        self.animacoes["defendendo_esq"].set_total_duration(1000)
        self.animacoes["defendendo_dir"].set_total_duration(1000)

    def atualizar(self, obj, time, lista_x, lista_y, janela):

        if self.velx > 0:
            self.direcao = "dir"
        elif self.velx < 0:
            self.direcao = "esq"

        colisoes = {
            "Teto": 0,
            "Esquerda": 0,
            "Direita": 0,
            "Chão": 0
        }

        colidiu = False
        for i in range(len(obj["tiles_ini"])):
            if self.hitbox.collided(obj["tiles_ini"][i].sprite):
                colidiu = True

        for i in range(len(obj["tiles_simples"])):
            if self.hitbox.collided(obj["tiles_simples"][i].sprite):
                direcao = obj["tiles_simples"][i].identificar_lado(self.hitbox)

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
                    colisoes[direcao] += 1

        '''verificar se está perto o suficiente do jogador para poder parar de andar'''
        perto = False
        if self.vendo and - 70 <= (self.hitbox.x + self.hitbox.width) - (
                obj["jogador"].hitbox.x + obj["jogador"].hitbox.width) <= 70:
            perto = True

        # ATACAR ------------------------------------------------------------------------------------

        if self.pulso_ataque > 0:
            self.pulso_ataque -= time

        if self.prepataque:
            if self.pulso_ataque <= 2.5:
                self.atacando = True
                self.prepataque = False

        if self.atacando:
            self.pulso_ataque -= time
            if self.pulso_ataque <= 2:
                self.atacando = False
                self.defendendo = True

        if self.pulso_ataque <= 0 and perto:
            self.prepataque = True
            self.atacou = False
            self.pulso_ataque = 3

        if self.atacando and not self.atacou:
            self.atacou = True
            if self.direcao == "esq":
                obj["projeteis_inimig"].append(Projetil_Inimigo(
                    "Assets/Imagens/Pojéteis/goblin_ataque.png",
                    self.hitbox.x - 61,
                    self.hitbox.y + 18,
                    0,
                    1,
                    0,
                    "Tiro",
                    self.index
                ))
            else:
                obj["projeteis_inimig"].append(Projetil_Inimigo(
                    "Assets/Imagens/Pojéteis/goblin_ataque.png",
                    self.hitbox.x - 61,
                    self.hitbox.y + 12,
                    0,
                    1,
                    0,
                    "Tiro",
                    self.index
                ))

        # DEFENDER

        if self.defendendo:
            self.invulneravel = True
            if self.pulso_ataque <= 1:
                self.defendendo = False
                self.invulneravel = False

        # ANDAR DE UM LADO PARA O OUTRO --------------------------------------------------------------

        # visão --------------------------------
        if self.desver <= 0:
            self.desver = 2
            self.vendo = False
        if self.vendo:
            self.desver -= time
            if obj["jogador"].hitbox.x + obj["jogador"].hitbox.width / 2 < self.hitbox.x + self.hitbox.width / 2:
                self.dir = -1
            else:
                self.dir = 1

        # padrão ------------------------------
        naparede = False
        if ((self.velx > 0 and colisoes["Direita"] >= 1)
                or (self.velx < 0 and colisoes["Esquerda"] >= 1)):
            naparede = True
        if (((self.velx > 0 and colisoes["Direita"] > 1) or (self.velx < 0 and colisoes["Esquerda"] > 1))
                and not self.vendo) or colidiu:
            self.dir *= -1
        self.velx = 100 * time * self.dir
        if not naparede and not time >= 1 and not self.paralizado and not self.tomando_dano \
                and not (self.prepataque or self.atacando) and not perto and not self.defendendo:
            self.andando = True
            self.hitbox.x += self.velx
        else:
            self.andando = False

        # VISÃO -------------------------------- (via pojétil) ---------------------------------------

        self.pulso_visao -= time
        if self.pulso_visao <= 0:
            self.pulso_visao = 0.2
            obj["projeteis_inimig"].append(Projetil_Inimigo(
                "Assets/Imagens/Pojéteis/visao.png",
                self.hitbox.x + self.hitbox.width / 2,
                self.hitbox.y + self.hitbox.height / 2,
                1000,
                0,
                0.2,
                "Visão",
                self.index
            ))
            obj["projeteis_inimig"].append(Projetil_Inimigo(
                "Assets/Imagens/Pojéteis/visao.png",
                self.hitbox.x + self.hitbox.width / 2,
                self.hitbox.y + self.hitbox.height / 2,
                -1000,
                0,
                0.2,
                "Visão",
                self.index
            ))

        # MOVIMENTAÇÃO VERTICAL -------------------------------------------------------------------------
        gravidade = 3000

        if (colisoes["Esquerda"] == 1 or colisoes["Direita"] == 1) and not self.tomando_dano:
            self.animacoes[f"pulando_{self.direcao}"].set_curr_frame(0)
            self.vely = -500
            self.hitbox.y += self.vely * time + gravidade * -.5 * time * time

        if colisoes["Teto"] >= 1 and self.vely <= 0:
            self.vely = 0
            self.hitbox.y += 1

        if colisoes["Chão"] >= 1 and self.vely >= 0:
            self.vely = 0

        if (colisoes["Chão"] == 0 or (colisoes["Chão"] >= 1 and self.vely < 0)) and not time > 1:
            self.vely += time * gravidade
            if self.vely > 1000:
                self.vely = 1000
            self.hitbox.y += self.vely * time + gravidade * -.5 * time * time

        # MORRER ------------------------------------------------------------------------------------
        tirar = False
        if self.hp <= 0 and self.animacoes[
            f"morrendo_{self.direcao}"].get_curr_frame() == 7:  # varia de inimigo para inimigo
            self.animacoes[f"morrendo_{self.direcao}"].set_curr_frame(0)
            tirar = True

            # acabar o jogo
            janela.draw_text(f"#==CONCLUÍDO==#",
                             120,
                             200,
                             100,
                             (200, 200, 200),
                             "Arial",
                             False,
                             False
                             )
            janela.update()
            pygame.time.delay(5000)

        # TOMAR DANO --------------------------------------------------------------------------------
        if self.tomando_dano and self.animacoes[
            f"tomando_{self.direcao}"].get_curr_frame() == 4:  # varia de inimigo para inimigo
            self.animacoes[f"tomando_{self.direcao}"].set_curr_frame(0)
            self.tomando_dano = False

        # ESCOLHER ANIMAÇÃO -------------------------------------------------------------------------

        if tirar:
            return 1
        elif self.hp <= 0:
            return f"morrendo_{self.direcao}"
        elif self.atacando:
            return f"atacando_{self.direcao}"
        elif self.vely < 0 and not self.tomando_dano:
            return f"pulando_{self.direcao}"
        elif self.vely > 0 and not self.tomando_dano:
            return f"caindo_{self.direcao}"
        elif self.tomando_dano:
            return f"tomando_{self.direcao}"
        elif self.andando:
            return f"andando_{self.direcao}"
        elif self.defendendo:
            return f"defendendo_{self.direcao}"
        else:
            return f"parado_{self.direcao}"

    def desenhar(self, anim, mov):

        if anim == "atacando_esq" or anim == "atacando_dir":
            self.animacoes[f"{anim}"].x = self.hitbox.x - 118
            self.animacoes[f"{anim}"].y = self.hitbox.y - 35
        else:
            self.animacoes[f"{anim}"].x = self.hitbox.x - 45
            self.animacoes[f"{anim}"].y = self.hitbox.y - 35
        if mov:
            self.animacoes[f"{anim}"].update()
        self.hitbox.draw()
        self.animacoes[f"{anim}"].draw()


class Mago:
    def __init__(self, index, x, y):

        self.index = index

        self.hitbox = GameImage("Assets/Imagens/Hitboxes/hitbox_mago.png")
        self.hitbox.x = x * 32
        self.hitbox.y = y * 32 + 12

        self.velx = 100
        self.vely = 0
        self.dir = -1
        self.direcao = "esq"

        self.hp = 5
        self.paralizado = False
        self.tomando_dano = False

        self.pulso_visao = 0
        self.vendo = False
        self.desver = 0

        self.pulso_ataque = 0
        self.atacando = False
        self.prepataque = False
        self.atacou = False
        self.andando = False
        self.invulneravel = False

        self.animacoes = {
            "tomando_esq": Sprite("Assets/Imagens/Sprites/Inimigos/Mago/tomando_dir.png", 3),
            "tomando_dir": Sprite("Assets/Imagens/Sprites/Inimigos/Mago/tomando_dir.png", 3),
            "atacando_esq": Sprite("Assets/Imagens/Sprites/Inimigos/Mago/atacando_esq.png", 5),
            "atacando_dir": Sprite("Assets/Imagens/Sprites/Inimigos/Mago/atacando_dir.png", 5),
            "morrendo_esq": Sprite("Assets/Imagens/Sprites/Inimigos/Mago/morrendo_dir.png", 7),
            "morrendo_dir": Sprite("Assets/Imagens/Sprites/Inimigos/Mago/morrendo_dir.png", 7),
            "parado_esq": Sprite("Assets/Imagens/Sprites/Inimigos/Mago/parado_esq.png", 5),
            "parado_dir": Sprite("Assets/Imagens/Sprites/Inimigos/Mago/parado_dir.png", 5)
        }

        self.animacoes["tomando_esq"].set_total_duration(600)
        self.animacoes["tomando_dir"].set_total_duration(600)
        self.animacoes["atacando_esq"].set_total_duration(300)
        self.animacoes["atacando_dir"].set_total_duration(300)
        self.animacoes["morrendo_esq"].set_total_duration(1000)
        self.animacoes["morrendo_dir"].set_total_duration(1000)
        self.animacoes["parado_esq"].set_total_duration(800)
        self.animacoes["parado_dir"].set_total_duration(800)

    def atualizar(self, obj, time, lista_x, lista_y):

        colisoes = {
            "Teto": 0,
            "Esquerda": 0,
            "Direita": 0,
            "Chão": 0
        }


        for i in range(len(obj["tiles_simples"])):
            if self.hitbox.collided(obj["tiles_simples"][i].sprite):
                direcao = obj["tiles_simples"][i].identificar_lado(self.hitbox)

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
                    colisoes[direcao] += 1

        # ATACAR ------------------------------------------------------------------------------------

        if self.pulso_ataque > 0:
            self.pulso_ataque -= time

        if self.prepataque:
            if self.pulso_ataque <= 2.5:
                self.atacando = True
                self.prepataque = False

        if self.atacando:
            self.pulso_ataque -= time
            if self.pulso_ataque <= 2:
                self.atacando = False

        if self.pulso_ataque <= 0 and self.vendo:
            self.prepataque = True
            self.atacou = False
            self.pulso_ataque = 3

        if self.atacando and not self.atacou:
            self.atacou = True
            if self.direcao == "esq":
                obj["projeteis_inimig"].append(Projetil_Inimigo(
                    f"Assets/Imagens/Pojéteis/raio_arcano_esq.png",
                    self.hitbox.x - 61,
                    self.hitbox.y + 18,
                    -300,
                    2,
                    10,
                    "Tiro",
                    self.index
                ))
            else:
                obj["projeteis_inimig"].append(Projetil_Inimigo(
                    f"Assets/Imagens/Pojéteis/raio_arcano_dir.png",
                    self.hitbox.x - 61,
                    self.hitbox.y + 18,
                    300,
                    2,
                    10,
                    "Tiro",
                    self.index
                ))

        # VISÃO ------------------------ (via pojétil) --------------------------------------------------

        self.pulso_visao -= time
        if self.pulso_visao <= 0:
            self.pulso_visao = 0.2
            obj["projeteis_inimig"].append(Projetil_Inimigo(
                "Assets/Imagens/Pojéteis/visao.png",
                self.hitbox.x + self.hitbox.width / 2,
                self.hitbox.y + self.hitbox.height / 2,
                1000,
                0,
                0.5,
                "Visão",
                self.index
            ))
            obj["projeteis_inimig"].append(Projetil_Inimigo(
                "Assets/Imagens/Pojéteis/visao.png",
                self.hitbox.x + self.hitbox.width / 2,
                self.hitbox.y + self.hitbox.height / 2,
                -1000,
                0,
                0.5,
                "Visão",
                self.index
            ))

        # visão --------------------------------
        if self.desver <= 0:
            self.desver = 2
            self.vendo = False
        if self.vendo:
            self.desver -= time
            if obj["jogador"].hitbox.x + obj["jogador"].hitbox.width / 2 < self.hitbox.x + self.hitbox.width / 2:
                self.direcao = "esq"
            else:
                self.direcao = "dir"

        # MORRER ------------------------------------------------------------------------------------
        tirar = False
        if self.hp <= 0 and self.animacoes[
            f"morrendo_{self.direcao}"].get_curr_frame() == 6:  # varia de inimigo para inimigo
            self.animacoes[f"morrendo_{self.direcao}"].set_curr_frame(0)
            tirar = True

            # dropar
            moedas = int(random.random() * 15) + 16
            obj["jogador"].itens[14] += moedas

        # TOMAR DANO --------------------------------------------------------------------------------
        if self.tomando_dano and self.animacoes[
                f"tomando_{self.direcao}"].get_curr_frame() == 2:  # varia de inimigo para inimigo
            self.animacoes[f"tomando_{self.direcao}"].set_curr_frame(0)
            self.tomando_dano = False

        # ESCOLHER ANIMAÇÃO -------------------------------------------------------------------------

        if tirar:
            return 1
        elif self.hp <= 0:
            return f"morrendo_{self.direcao}"
        elif self.atacando:
            return f"atacando_{self.direcao}"
        elif self.tomando_dano:
            return f"tomando_{self.direcao}"
        else:
            return f"parado_{self.direcao}"

    def desenhar(self, anim, mov):

        self.animacoes[f"{anim}"].x = self.hitbox.x - 61
        self.animacoes[f"{anim}"].y = self.hitbox.y - 46
        if mov:
            self.animacoes[f"{anim}"].update()
        self.hitbox.draw()
        self.animacoes[f"{anim}"].draw()



tipos = {
    "goblin": Goblin,
    "esqueleto": Esqueleto,
    "mago": Mago
}


class Inimigo:
    def __init__(self, index, tipo, x, y):
        self.tipo = tipos[tipo](index, x, y)
