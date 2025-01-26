from PPlay.gameimage import *


class Projetil_Inimigo:
    def __init__(self, arquivo, x, y, vel, dano, tempo, tipo, id):

        self.imagem = GameImage(arquivo)
        self.imagem.x = x
        self.imagem.y = y

        self.vel = vel
        self.dano = dano

        self.tempo = tempo
        self.tipo = tipo
        self.aux = 0
        self.id = id

    def atualizar(self, obj, time):

        self.imagem.x += self.vel * time
        self.tempo -= time

        # PROJÉTEIS VISÃO --------------------------------------------------------------------
        if self.tipo == "Visão":

            # bater no jogador
            if obj["jogador"].hitbox.collided(self.imagem):
                if obj["inimigos"][self.id] != 0:
                    obj["inimigos"][self.id].tipo.vendo = True
                obj["projeteis_inimig"].pop(obj["projeteis_inimig"].index(self))
                return 1

            # sumir na parede
            for i in range(len(obj["tiles_simples"])):
                if obj["tiles_simples"][i].sprite.collided(self.imagem):
                    obj["projeteis_inimig"].pop(obj["projeteis_inimig"].index(self))
                    return 1

        # PROJÉTEIS TIRO ---------------------------------------------------------------------
        if self.tipo == "Tiro":

            # bater no jogador
            if obj["jogador"].hitbox.collided(self.imagem):
                if not obj["jogador"].abaixado:
                    obj["projeteis_inimig"].pop(obj["projeteis_inimig"].index(self))
                    if not obj["jogador"].invencivel:
                        obj["jogador"].acertado = True
                        obj["jogador"].invencivel = True
                    return 1
                elif obj["jogador"].hitbox_abaixado.collided(self.imagem):
                    obj["projeteis_inimig"].pop(obj["projeteis_inimig"].index(self))
                    if not obj["jogador"].invencivel:
                        obj["jogador"].acertado = True
                        obj["jogador"].invencivel = True
                    return 1

            # sumir na parede
            for i in range(len(obj["tiles_simples"])):
                if obj["tiles_simples"][i].sprite.collided(self.imagem):
                    obj["projeteis_inimig"].pop(obj["projeteis_inimig"].index(self))
                    return 1

            # sumir no escudo
            for i in range(len(obj["projeteis_player"])):
                if obj["projeteis_player"][i].imagem.collided(self.imagem) and obj["projeteis_player"][i].tipo == "Escudo":
                    obj["projeteis_player"].pop(obj["projeteis_player"].index(self))
                    return 1

        # sumir por tempo (obrigatório)
        if self.tempo <= 0:
            obj["projeteis_inimig"].pop(obj["projeteis_inimig"].index(self))
            return 1

        return 0

    def desenhar(self):
        self.imagem.draw()
