# --------------------------------- IMPORTAÇÕES ------------------------------------#
from PPlay.gameimage import *
from PPlay.window import *
from PPlay.sound import *

# ----------------------------- ALGUMAS OUTRAS COISAS ----------------------------- *
janela = Window(960, 640)
mouse = Window.get_mouse()

no_botao = Sound("Assets/Audio/Fantasy_UI (1).wav")
no_botao.set_volume(40)


# ===============================✩✩ CLASSE BOTÃO ✩✩=============================== #
class Botao:

    def __init__(self, nome, x, y):

        self.image = GameImage(f"Assets/Imagens/Menus/{nome}.png")
        self.image.x = x
        self.image.y = y

        self.image_var = GameImage(f"Assets/Imagens/Menus/{nome}_var.png")
        self.image_var.x = x
        self.image_var.y = y

        self.was_over = False

    # FUNÇÃO DESENHAR ----------------------------------------------------
    '''ISSO SERVE PARA DEIXAR O BOTÃO AMARELO CASO O USUÁRIO PASSE O MOUSE
    ENCIMA DELE'''

    def desenhar(self, ativado):
        if mouse.is_over_object(self.image):
            self.image_var.draw()
            if ativado == "1" and not self.was_over:
                no_botao.play()
                self.was_over = True
        else:
            self.image.draw()
            self.was_over = False
