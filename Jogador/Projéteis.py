from PPlay.gameimage import *


class Projetil_Jogador:
    def __init__(self, arquivo, x, y, vel, dano, tempo, tipo):

        self.imagem = GameImage(arquivo)
        self.imagem.x = x
        self.imagem.y = y

        self.vel = vel
        self.dano = dano

        self.tempo = tempo
        self.tipo = tipo
        self.aux = 0

    def atualizar(self, obj, time):

        self.imagem.x += self.vel * time
        self.tempo -= time
        # PROJÉTEIS TIRO ----------------------------------------------------------
        if self.tipo == "Tiro":

            # bater no inimigo
            for i in range(len(obj["inimigos"])):
                if type(obj["inimigos"][i]) != int and\
                        obj["inimigos"][i].tipo.hitbox.collided(self.imagem) and not obj["inimigos"][i].tipo.invulneravel and \
                        obj["jogador"].direcao != obj["inimigos"][i].tipo.direcao:
                    obj["projeteis_player"].pop(obj["projeteis_player"].index(self))
                    obj["inimigos"][i].tipo.hp -= self.dano
                    obj["inimigos"][i].tipo.tomando_dano = True
                    return 1

            # sumir na parede
            for i in range(len(obj["tiles_simples"])):
                if obj["tiles_simples"][i].sprite.collided(self.imagem):
                    obj["projeteis_player"].pop(obj["projeteis_player"].index(self))
                    return 1

        # PROJÉTEIS ESCUDO -----------------------------------------------------------
        elif self.tipo == "Escudo":

            # sumir com projetes inimigos
            '''incluir isso na atualização dos projeteis inimigos'''


        # PROJÉTEIS PARALIZADOR -------------------------------------------------------------
        elif self.tipo == "Paralizante":

            # bater no inimigo e paralizar
            for i in range(len(obj["inimigos"])):
                if obj["inimigos"][i].tipo.hitbox.collided(self.imagem):
                    obj["projeteis_player"].pop(obj["projeteis_player"].index(self))
                    obj["inimigos"][i].tipo.paralizado = True
                    return 1

            # sumir na parede
            for i in range(len(obj["tiles_simples"])):
                if obj["tiles_simples"][i].sprite.collided(self.imagem):
                    obj["projeteis_player"].pop(obj["projeteis_player"].index(self))
                    return 1


        # PROJÉTEIS ONDA -------------------------------------------------------------
        elif self.tipo == "Onda":

            # sumir na parede
            for i in range(len(obj["tiles_simples"])):
                if obj["tiles_simples"][i].sprite.collided(self.imagem):
                    obj["projeteis_player"].pop(obj["projeteis_player"].index(self))
                    return 1

            # bater no inimigo
            for i in range(len(obj["inimigos"])):
                if obj["inimigos"][i].tipo.hitbox.collided(self.imagem):
                    obj["projeteis_player"].pop(obj["projeteis_player"].index(self))
                    obj["inimigos"][i].hp -= self.dano
                    obj["inimigos"][i].tipo.tomando_dano = True
                    return 1

            # sumir com projetes inimigos
            '''incluir isso na atualização dos projeteis inimigos'''

        # sumir por tempo (obrigatório)
        if self.tempo <= 0:
            obj["projeteis_player"].pop(obj["projeteis_player"].index(self))
            return 1

        return 0

    def desenhar(self):
        self.imagem.draw()
