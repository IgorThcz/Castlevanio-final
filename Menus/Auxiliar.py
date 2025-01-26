from PPlay.gameimage import *
from PPlay.window import *

# --------------------------------------------- janela e mouse --------------------------------------------- #
janela = Window(960, 640)


# =========================== CLASSE DO CAMPO QUE MOSTRA INFORMAÇÃO ======================================== #
class Display:
    def __init__(self, x, y, texto):
        self.imagem = GameImage("Assets/Imagens/Menus/botoes/controles_info.png")
        self.imagem.x = x
        self.imagem.y = y
        self.texto = texto

    def desen(self):

        self.imagem.draw()

        if self.texto == "space":
            janela.draw_text(f"{self.texto}",
                             self.imagem.x + 20 - 10,
                             self.imagem.y + 6 + 10,
                             20,
                             (0, 0, 0),
                             "Arial",
                             False,
                             False
                             )
        elif self.texto == "esc":
            janela.draw_text(f"{self.texto}",
                             self.imagem.x + 20 - 10,
                             self.imagem.y + 6 + 5,
                             30,
                             (0, 0, 0),
                             "Arial",
                             False,
                             False
                             )
        else:
            janela.draw_text(f"{self.texto}",
                             self.imagem.x + 20,
                             self.imagem.y + 6,
                             40,
                             (0, 0, 0),
                             "Arial",
                             False,
                             False
                             )



