import random
import pygame.time
from Jogador.jogador_final import itens_texto, magias_dict, itens_dict
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.window import *
from Menus.Botoes import Botao

mouse = Window.get_mouse()

preco_dict = {
    "0": 0,

    "1": 30,
    "2": 55,
    "3": 80,

    "4": 30,
    "5": 55,
    "6": 80,

    "7": 60,
    "8": 110,
    "9": 160,

    "10": 50,
    "11": 90,
    "12": 130,

    "13": 0,
    "14": 0
}

magias_icones_dict = {
    "0": "icone_raio",
    "1": "icone_escudo",
    "2": "icone_onda",
    "3": "icone_foco"
}

magias_texto = {
    "0": ["Disparo Arcano",
          "Atire uma quantidade de energia mágica",
          "para frente, causando danos moderados ao",
          "inimigo sem gastar muita mana"
          ],
    "1": ["Escudo Mágico",
          "Posicione um escudo que bloqueia projéteis",
          "inimigos, é muito útil para se proteger em",
          "longas distâncias"
          ],
    "2": ["Onda Mística",
          "Atire uma larga onda de magia refinada",
          "que causa altos danos aos inimigos em",
          "custo de grandes quantidades de mana"
          ],
    "3": ["Esfera de Energia",
          "Dispare magia concentrada que causa baixos",
          "danos aos inimigos mas ao acertar deixa-os",
          "paralizados"
          ],
}

preco_magias = {
    "0": 0,
    "1": 100,
    "2": 400,
    "3": 900
}

dialogos_c = {
    "intro_1": [
        "Olá, seja bem vindo à vila, meu nome é Vianne"
    ],
    "intro_2": [
        "A julgar por sua aparência você é parte do grupo",
        "enviado para resolver o problema do castelo. Pera aí,",
        "só enviaram você???"
    ],
    "intro_3": [
        "Pode ser uma tarefa muito difícil,",
        "se precisar, alguns itens podem ser bem úteis"
    ],
    "padrao_1": [
        "Precisando de uma poção?"
    ],
    "padrao_2": [
        "temos pergaminhos em ótimo estado!"
    ],
    "padrao_3": [
        "barato, barato, leve 3, pague 4!"
    ]
}

dialogos_f = {
    "intro_1": [
        "Olá, forasteiro, sou Canley quem é você?"
    ],
    "intro_2": [
        "Vâino? não me soa estranho..."
    ],
    "intro_3": [
        "Ah, sim, o encarregado do castelo"
    ],
    "intro_4": [
        "Olha só, dizem que o castelo tem equipamentos",
        "antigos esquecidos, se por acaso achar algum",
        "eu ficaria muito feliz em restaurar uma peça",
        "rara"
    ],
    "padrao_1": [
        "Achou algo?"
    ],
    "padrao_2": [
        "Bom dia!"
    ],
    "padrao_3": [
        "Como vai, cara? Tudo certo?"
    ],
    "bota_1": [
        "Espere..."
    ],
    "bota_2": [
        "Isso aí é uma bota antiga do cartelo?"
    ],
    "bota_3": [
        "Eu esperei muito tempo por uma",
        "oportunidade como essa!"
    ],
    "bota_4": [
        "Vou restaurar essa bota para você",
        "sem cobrar nada!"
    ]
}

dialogos_m = {
    "intro_1": [
        "Oi, você é o Vanio, certo?"
    ],
    "intro_2": [
        "Veio para lidar com o problema do castelo não é?"
    ],
    "intro_3": [
        "Meu nome é Nancen"
    ],
    "intro_4": [
        "Eu já estive lá no castelo, como usuária de magia",
        "eu pensei que poderia resolver o problema",
        "mas aquele lugar é perigoso demais até para mim"
    ],
    "intro_5": [
        "Ao menos eu aprendi que em um ambiente como aquele,",
        "magias podem ser a direrença entre morrer ou viver.",
        "Talvez você deva aprender algumas magias básicas,",
        "eu posso te ensinar as mais úteis"
    ],
    "intro_6": [
        "A primeira magia eu posso ensinar de graça!"
    ],
    "padrao_1": [
        "Tem praticado suas magias?"
    ],
    "padrao_2": [
        "Próxima aula?"
    ],
    "padrao_3": [
        "Como vai? Tendo sorte no castelo?"
    ]
}


def dialogo(strings, janela, arquivo, audio):
    mouse = Window.get_mouse()

    segurado = True
    if not mouse.is_button_pressed(1):
        segurado = False

    retrato = GameImage(f"Assets/Imagens/Outros/retrato_{arquivo}.png")
    retrato.x = 10
    retrato.y = 428

    caixa = GameImage("Assets/Imagens/Outros/caixa_dialogo.png")
    caixa.x = 164
    caixa.y = 428

    bot_pular = Botao("Botoes/bot_pular", 846, 458)

    retrato.draw()

    for i in range(len(strings)):

        # ir escrevendo com delay
        for j in range(len(strings[i])):

            # caixa e botao
            caixa.draw()
            bot_pular.desenhar(audio[1])

            # texto anterior
            if i > 0:
                for a in range(i):
                    janela.draw_text(f"{strings[a]}",
                                     200,
                                     450 + a * 30,
                                     30,
                                     (0, 0, 0),
                                     "Arial",
                                     False,
                                     False
                                     )

            # delay
            pygame.time.delay(40)

            # texto atual (cada vez maior)
            janela.draw_text(f"{strings[i][0:j + 1]}",
                             200,
                             450 + i * 30,
                             30,
                             (0, 0, 0),
                             "Arial",
                             False,
                             False
                             )
            janela.update()

            # se apertar para pular vai sair do loop
            if not mouse.is_button_pressed(1):
                segurado = False
            if mouse.is_button_pressed(1) and not segurado and mouse.is_over_object(bot_pular.image):
                break
        if mouse.is_button_pressed(1) and not segurado:
            break

    segurado = True
    while True:

        # caixa e botao
        caixa.draw()
        bot_pular.desenhar(audio[1])

        # no final o texto inteiro é escrito denovo
        for i in range(len(strings)):
            janela.draw_text(f"{strings[i][0:len(strings[i])]}",
                             200,
                             450 + i * 30,
                             30,
                             (0, 0, 0),
                             "Arial",
                             False,
                             False
                             )

        # precisa apertar o botão para ir para o proximo texto
        if not mouse.is_button_pressed(1):
            segurado = False
        elif mouse.is_button_pressed(1) and not segurado and mouse.is_over_object(bot_pular.image):
            break
        janela.update()


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
            obj["inimigos"][i].tipo.desenhar(ini_anim)

    for i in range(len(obj["npcs"])):
        obj["npcs"][i].desenhar(obj, janela, contrl, False)

    for i in range(len(obj["projeteis_player"])):
        obj["projeteis_player"][i].desenhar()

    for i in range(len(obj["projeteis_inimig"])):
        obj["projeteis_inimig"][i].desenhar()

    obj["jogador"].desenhar(anim, janela, False)


class Maga:
    def __init__(self, x, y):
        self.sprite = Sprite("Assets/Imagens/Sprites/NPCs/Maga.png", 5)
        self.sprite.set_total_duration(1000)
        self.sprite.x = x * 32
        self.sprite.y = x * 32 - 106
        self.hitbox = GameImage("Assets/Imagens/Hitboxes/hitbox_npc.png")
        self.hitbox.x = x * 32
        self.hitbox.y = y * 32 - 106

    def magias(self, obj, janela, contrl, audio, ini_anim, anim):
        mouse = Window.get_mouse()

        # caixa do inventário
        caixa = GameImage("Assets/Imagens/Outros/magias.png")
        caixa.x = 280
        caixa.y = 58

        # botão usar agora
        bot_aprender = Botao("Botoes/bot_comprar", 280, 492)

        # botão selecionar
        bot_selecionar = Botao("Botoes/bot_escolher_item", 482, 492)

        # botão fechar inventário
        bot_fechar = Botao("Botoes/fechar_mochila", 216, 82)

        # indicadores do inventário
        item_mostrando = GameImage("Assets/Imagens/Outros/mostrando_dobro.png")
        item_sobre = GameImage("Assets/Imagens/Outros/mouse_sobre_dobro.png")
        item_selecionado = GameImage("Assets/Imagens/Outros/selecionado_dobro.png")

        # magias bloqueadas
        bloq = []
        bloq.append(GameImage(f"Assets/Imagens/Magias/icone_bloqueado.png"))
        bloq[0].x = 354
        bloq[0].y = 222
        bloq.append(GameImage(f"Assets/Imagens/Magias/icone_bloqueado.png"))
        bloq[1].x = 354
        bloq[1].y = 222 + 130
        bloq.append(GameImage(f"Assets/Imagens/Magias/icone_bloqueado.png"))
        bloq[2].x = 354 + 130
        bloq[2].y = 222
        bloq.append(GameImage(f"Assets/Imagens/Magias/icone_bloqueado.png"))
        bloq[3].x = 354 + 130
        bloq[3].y = 222 + 130
        # magias
        magias = []
        magias.append(GameImage(f"Assets/Imagens/Magias/icone_raio.png"))
        magias[0].x = 354
        magias[0].y = 222
        magias.append(GameImage(f"Assets/Imagens/Magias/icone_escudo.png"))
        magias[1].x = 354
        magias[1].y = 222 + 130
        magias.append(GameImage(f"Assets/Imagens/Magias/icone_onda.png"))
        magias[2].x = 354 + 130
        magias[2].y = 222
        magias.append(GameImage(f"Assets/Imagens/Magias/icone_foco.png"))
        magias[3].x = 354 + 130
        magias[3].y = 222 + 130
        magias.append(None)

        principal = 4

        clicado = True
        while True:

            # calcular preço da proxima magia:
            preco = 0
            for i in range(4):
                if obj["jogador"].magias[i]:
                    preco += 1

            # clicar nas coisas:

            if mouse.is_button_pressed(1):

                for i in range(len(magias)-1):
                    if mouse.is_over_object(magias[i]):
                        principal = i

                if mouse.is_over_object(bot_fechar.image):
                    break

                if (mouse.is_over_object(bot_selecionar.image) and principal != 4
                        and not clicado and obj["jogador"].magias[principal]):
                    obj["jogador"].magia_equip = principal

                if (mouse.is_over_object(bot_aprender.image) and not clicado
                    and not obj["jogador"].magias[principal]) and obj["jogador"].itens[14] >= preco_magias[str(principal)]:
                    obj["jogador"].magias[principal] = True
                    obj["jogador"].itens[14] -= preco_magias[str(principal)]

            # clique aprimorado
            if not mouse.is_button_pressed(1):
                clicado = False
            else:
                clicado = True

            # desenhar as coisas

            fundo_pausado(obj, janela, contrl, ini_anim, anim)

            caixa.draw()

            if principal != 4:
                destaque = GameImage(f"Assets/Imagens/Magias/{magias_icones_dict[str(principal)]}.png")
                destaque.x = 290
                destaque.y = 92
                destaque.draw()
                janela.draw_text(f"{magias_texto[str(principal)][0]}", 426, 100, 20,
                                 (224, 132, 132), "Arial", True, False)
                aux = 0
                for i in range(len(magias_texto[str(principal)]) - 1):
                    aux += 1
                    janela.draw_text(f"{magias_texto[str(principal)][i + 1]}", 426, 130 + 15 * i,
                                     15,
                                     (0, 0, 0), "Arial", False, False)
                janela.draw_text(
                    f"Custo de Aprendizado: {preco_magias[str(principal)]} | Você tem {obj["jogador"].itens[14]}",
                    426, 130 + (15 * aux),
                    15,
                    (0, 0, 0), "Arial", False, False)

            for i in range(len(magias)-1):
                magias[i].draw()

            for i in range(len(bloq)):
                if not obj["jogador"].magias[i]:
                    bloq[i].draw()

            bot_aprender.desenhar(audio[1])
            bot_fechar.desenhar(audio[1])
            bot_selecionar.desenhar(audio[1])

            for i in range(len(magias)-1):
                if mouse.is_over_object(magias[i]):
                    item_sobre.x = magias[i].x - 2
                    item_sobre.y = magias[i].y - 2
                    item_sobre.draw()

                elif i == obj["jogador"].magia_equip:
                    item_selecionado.x = magias[i].x - 2
                    item_selecionado.y = magias[i].y - 2
                    item_selecionado.draw()

                elif i == principal:
                    item_mostrando.x = magias[i].x - 2
                    item_mostrando.y = magias[i].y - 2
                    item_mostrando.draw()

            # atualizar janela

            janela.update()

    def atualizar(self, obj, janela, contrl, teclado, audio, ini_anim, anim):

        if teclado.key_pressed(f"{contrl["abaixar"]}") and self.hitbox.collided(obj["jogador"].hitbox):

            if not obj["jogador"].interacoes["Maga"]:
                dialogo(dialogos_m["intro_1"], janela, "maga", audio)
                dialogo(dialogos_m["intro_2"], janela, "maga", audio)
                dialogo(dialogos_m["intro_3"], janela, "maga", audio)
                dialogo(dialogos_m["intro_4"], janela, "maga", audio)
                dialogo(dialogos_m["intro_5"], janela, "maga", audio)
                dialogo(dialogos_m["intro_6"], janela, "maga", audio)
                obj["jogador"].interacoes["Maga"] = True

            else:
                num = int(random.random() * 3)
                if num == 0:
                    dialogo(dialogos_m["padrao_1"], janela, "maga", audio)
                elif num == 1:
                    dialogo(dialogos_m["padrao_2"], janela, "maga", audio)
                else:
                    dialogo(dialogos_m["padrao_3"], janela, "maga", audio)

                # inserir interface aqui
                self.magias(obj, janela, contrl, audio, ini_anim, anim)


class Ferreiro:
    def __init__(self, x, y):
        self.sprite = Sprite("Assets/Imagens/Sprites/NPCs/Ferreiro.png", 6)
        self.sprite.set_total_duration(600)
        self.sprite.x = x * 32
        self.sprite.y = y * 32 - 106
        self.hitbox = GameImage("Assets/Imagens/Hitboxes/hitbox_npc.png")
        self.hitbox.x = x * 32
        self.hitbox.y = y * 32 - 106

    def atualizar(self, obj, janela, contrl, teclado, audio, ini_anim, anim):

        if teclado.key_pressed(f"{contrl["abaixar"]}") and self.hitbox.collided(obj["jogador"].hitbox):

            if not obj["jogador"].interacoes["Ferreiro"]:
                dialogo(dialogos_f["intro_1"], janela, "ferreiro", audio)
                dialogo(dialogos_f["intro_2"], janela, "ferreiro", audio)
                dialogo(dialogos_f["intro_3"], janela, "ferreiro", audio)
                dialogo(dialogos_f["intro_4"], janela, "ferreiro", audio)
                obj["jogador"].interacoes["Ferreiro"] = True

            elif obj["jogador"].itens[13] == 1:
                dialogo(dialogos_f["bota_1"], janela, "ferreiro", audio)
                dialogo(dialogos_f["bota_2"], janela, "ferreiro", audio)
                dialogo(dialogos_f["bota_3"], janela, "ferreiro", audio)
                dialogo(dialogos_f["bota_4"], janela, "ferreiro", audio)
                obj["jogador"].itens[13] = 0
                obj["jogador"].habilidades[0] = True

            else:
                num = int(random.random() * 3)
                if num == 0:
                    dialogo(dialogos_f["padrao_1"], janela, "ferreiro", audio)
                elif num == 1:
                    dialogo(dialogos_f["padrao_2"], janela, "ferreiro", audio)
                else:
                    dialogo(dialogos_f["padrao_3"], janela, "ferreiro", audio)

                # inserir interface aqui


class Comerciante:
    def __init__(self, x, y):
        self.sprite = Sprite("Assets/Imagens/Sprites/NPCs/Comerciante.png", 10)
        self.sprite.set_total_duration(1000)
        self.sprite.x = x * 32
        self.sprite.y = y * 32 - 106
        self.hitbox = GameImage("Assets/Imagens/Hitboxes/hitbox_npc.png")
        self.hitbox.x = x * 32
        self.hitbox.y = y * 32 - 106

    def mochila(self, obj, janela, audio, contrl, ini_anim, anim):

        mouse = Window.get_mouse()

        # caixa do inventário
        inventario = GameImage("Assets/Imagens/Outros/vendas.png")
        inventario.x = 280
        inventario.y = 58

        # botão usar agora
        bot_loja = Botao("Botoes/bot_loja", 280, 492)

        # botão selecionar
        bot_vender = Botao("Botoes/bot_vender", 482, 492)

        # botão fechar inventário
        bot_fechar = Botao("Botoes/fechar_mochila", 216, 82)

        # indicadores do inventário
        item_mostrando = GameImage("Assets/Imagens/Outros/mostrando.png")
        item_sobre = GameImage("Assets/Imagens/Outros/mouse_sobre.png")

        principal = 0

        clicado = True
        while True:

            # itens no inventário
            itens = []
            x = 352
            y = 218
            for i in range(len(obj["jogador"].itens)):

                ''' essa primeira condição não testa se a quantidade do item é 0,
                quando i == 1, isso significao item inexistente'''
                if i == 0:
                    itens.append(GameImage(f"Assets/Imagens/Itens/{itens_dict["1"]}.png"))
                    itens[i].x = -64
                    itens[i].y = -64

                elif obj["jogador"].itens[i] > 0:
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

            # clicar nas coisas:

            if mouse.is_button_pressed(1):

                for i in range(len(itens)):
                    if mouse.is_over_object(itens[i]):
                        principal = i

                if mouse.is_over_object(bot_fechar.image):
                    return "sair"

                if (mouse.is_over_object(bot_vender.image) and principal != 0
                    and principal <= 12) and not clicado and obj["jogador"].itens[principal] > 0:
                    obj["jogador"].itens[14] += int(preco_dict[str(principal)] / 5)
                    obj["jogador"].itens[principal] -= 1

                if mouse.is_over_object(bot_loja.image) and not clicado:
                    return "loja"

            # clique aprimorado

            if not mouse.is_button_pressed(1):
                clicado = False
            else:
                clicado = True

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

                    elif i == principal:
                        item_mostrando.x = itens[i].x
                        item_mostrando.y = itens[i].y
                        item_mostrando.draw()

                    janela.draw_text(f"x{obj["jogador"].itens[i]}", itens[i].x + 40, itens[i].y + 40, 20,
                                     (0, 0, 0), "Arial", False, False)

            if principal != 0:
                destaque = GameImage(f"Assets/Imagens/Itens/{itens_dict[str(principal)]}_aum.png")
                destaque.x = 290
                destaque.y = 92
                destaque.draw()
                janela.draw_text(f"{itens_texto[str(principal)][0]}", 426, 100, 20,
                                 (224, 132, 132), "Arial", True, False)
                aux = 0
                for i in range(len(itens_texto[str(principal)]) - 1):
                    aux += 1
                    janela.draw_text(f"{itens_texto[str(principal)][i + 1]}", 426, 130 + 15 * i,
                                     15,
                                     (0, 0, 0), "Arial", False, False)
                janela.draw_text(f"Preço de venda: {int(preco_dict[str(principal)] / 5)}", 426, 130 + (15 * aux),
                                 15,
                                 (0, 0, 0), "Arial", False, False)

            bot_loja.desenhar(audio[1])
            bot_fechar.desenhar(audio[1])
            bot_vender.desenhar(audio[1])

            # atualizar janela

            janela.update()

    def loja(self, obj, janela, audio, contrl, ini_anim, anim):

        mouse = Window.get_mouse()

        # caixa do inventário
        inventario = GameImage("Assets/Imagens/Outros/loja.png")
        inventario.x = 280
        inventario.y = 58

        # botão usar agora
        bot_loja = Botao("Botoes/bot_vendas", 280, 492)

        # botão selecionar
        bot_vender = Botao("Botoes/bot_comprar", 482, 492)

        # botão fechar inventário
        bot_fechar = Botao("Botoes/fechar_mochila", 216, 82)

        # indicadores do inventário
        item_mostrando = GameImage("Assets/Imagens/Outros/mostrando.png")
        item_sobre = GameImage("Assets/Imagens/Outros/mouse_sobre.png")

        # itens a venda
        itens = []
        x = 352
        y = 218
        for i in range(len(obj["jogador"].itens)):

            ''' essa primeira condição não testa se a quantidade do item é 0,
            quando i == 1, isso significao item inexistente'''
            if i == 0 or i >= 13:
                itens.append(GameImage(f"Assets/Imagens/Itens/{itens_dict["1"]}.png"))
                itens[i].x = -64
                itens[i].y = -64

            else:
                itens.append(GameImage(f"Assets/Imagens/Itens/{itens_dict[str(i)]}.png"))
                itens[i].x = x
                itens[i].y = y
                if x >= 352 + 3 * 64:
                    x = 352
                    y += 64
                else:
                    x += 64

        principal = 0

        clicado = True
        while True:

            # clicar nas coisas:

            if mouse.is_button_pressed(1):

                for i in range(len(itens)):
                    if mouse.is_over_object(itens[i]):
                        principal = i

                if mouse.is_over_object(bot_fechar.image):
                    return "sair"

                if (mouse.is_over_object(bot_vender.image) and principal != 0
                    and principal <= 12) and not clicado and obj["jogador"].itens[14] >= preco_dict[str(principal)]:
                    obj["jogador"].itens[14] -= preco_dict[str(principal)]
                    obj["jogador"].itens[principal] += 1

                if mouse.is_over_object(bot_loja.image) and not clicado:
                    return "moch"

            # clique aprimorado
            if not mouse.is_button_pressed(1):
                clicado = False
            else:
                clicado = True

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

                    elif i == principal:
                        item_mostrando.x = itens[i].x
                        item_mostrando.y = itens[i].y
                        item_mostrando.draw()

            if principal != 0:
                destaque = GameImage(f"Assets/Imagens/Itens/{itens_dict[str(principal)]}_aum.png")
                destaque.x = 290
                destaque.y = 92
                destaque.draw()
                janela.draw_text(f"{itens_texto[str(principal)][0]}", 426, 100, 20,
                                 (224, 132, 132), "Arial", True, False)
                aux = 0
                for i in range(len(itens_texto[str(principal)]) - 1):
                    aux += 1
                    janela.draw_text(f"{itens_texto[str(principal)][i + 1]}", 426, 130 + 15 * i,
                                     15,
                                     (0, 0, 0), "Arial", False, False)
                janela.draw_text(f"Preço de compra: {preco_dict[str(principal)]} | Você tem {obj["jogador"].itens[14]}",
                                 426, 130 + (15 * aux),
                                 15,
                                 (0, 0, 0), "Arial", False, False)

            bot_loja.desenhar(audio[1])
            bot_fechar.desenhar(audio[1])
            bot_vender.desenhar(audio[1])

            # atualizar janela

            janela.update()

    def atualizar(self, obj, janela, contrl, teclado, audio, ini_anim, anim):

        if teclado.key_pressed(f"{contrl["abaixar"]}") and self.hitbox.collided(obj["jogador"].hitbox):

            if not obj["jogador"].interacoes["Comerciante"]:
                dialogo(dialogos_c["intro_1"], janela, "comerciante", audio)
                dialogo(dialogos_c["intro_2"], janela, "comerciante", audio)
                dialogo(dialogos_c["intro_3"], janela, "comerciante", audio)
                obj["jogador"].interacoes["Comerciante"] = True

            else:
                num = int(random.random() * 3)
                if num == 0:
                    dialogo(dialogos_c["padrao_1"], janela, "comerciante", audio)
                elif num == 1:
                    dialogo(dialogos_c["padrao_2"], janela, "comerciante", audio)
                else:
                    dialogo(dialogos_c["padrao_3"], janela, "comerciante", audio)

                opcao = self.loja(obj, janela, audio, contrl, ini_anim, anim)
                while True:
                    if opcao == "loja":
                        opcao = self.loja(obj, janela, audio, contrl, ini_anim, anim)
                    elif opcao == "moch":
                        opcao = self.mochila(obj, janela, audio, contrl, ini_anim, anim)
                    else:
                        break


npcs = {
    "Maga": Maga,
    "Ferreiro": Ferreiro,
    "Comerciante": Comerciante
}


class NPC:

    def __init__(self, tipo, x, y):
        self.tipo = npcs[tipo](x, y)

    def desenhar(self, obj, janela, contrl, mov):
        if mov:
            self.tipo.sprite.update()
        self.tipo.hitbox.draw()
        self.tipo.sprite.x = self.tipo.hitbox.x + 110
        self.tipo.sprite.y = self.tipo.hitbox.y
        self.tipo.sprite.draw()

        if self.tipo.hitbox.collided(obj["jogador"].hitbox):
            janela.draw_text(f"Pressione a tecla [{contrl["abaixar"]}] para interagir",
                             10,
                             590,
                             40,
                             (200, 200, 200),
                             "Arial",
                             False,
                             False
                             )
