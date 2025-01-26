from PPlay.gameimage import *

correspondencia = [
    "dir_pri"
    "dir_sec"
    "esq_pri"
    "esq_sec"
]


class Elementos_de_sala:
    def __init__(self, x, y):
        self.sprite = GameImage(f"Assets/Imagens/Cenario/tiletest.png")
        self.sprite.x = x * 32
        self.sprite.y = y * 32

    # -------------------------- FUNÇÃO IDENTIFICAR LADO ----------------------#

    '''ESSA FUNÇÃO É MUITO IMPORTANTE, QUANDO O JOGADOR COLIDE COM ALGUM TILE
    ESSA FUNÇÃO IDENTIFICA DE ONDE VEM A COLISÃO E COM ISSO É POSSÍVEL MUDAR
    A VELOCODADE A MOVIMENTAÇÃO DE FORMA ADEQUADA'''

    def identificar_lado(self, hitbox):


        calculo = [
            self.sprite.y + 32 - hitbox.y,
            self.sprite.x + 32 - hitbox.x,
            hitbox.x + 28 - self.sprite.x,
            hitbox.y + 72 - self.sprite.y
        ]

        resposta = [
            "Teto",
            "Esquerda",
            "Direita",
            "Chão"
        ]

        return resposta[calculo.index(min(calculo))]


class Porta:
    def __init__(self, cod, x, y, novo_x, novo_y):
        self.id = cod
        self.sprite = GameImage("Assets/Imagens/Hitboxes/porta.png")
        self.sprite.x = x * 32
        self.sprite.y = y * 32
        self.x = novo_x
        self.y = novo_y


class Ponto_salvamento:
    def __init__(self, x, y, cod, novo_x, novo_y):
        self.sprite = GameImage("Assets/Imagens/Hitboxes/interagivel.png")
        self.sprite.x = x * 32 - 16
        self.sprite.y = y * 32
        self.cod = cod
        self.novo_x = novo_x
        self.novo_y = novo_y
