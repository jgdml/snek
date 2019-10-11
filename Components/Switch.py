from Defaults import *
from Components.Botao import Botao


def switch(posX, posY, opcoes, eventos, selecionado):

    tam = [resolucao[0] * 0.20, resolucao[1] * 0.08]
    rect = [posX - tam[0] / 2, posY - tam[1] / 2, tam[0], tam[1]]

    txt = fonte.render(str(opcoes[selecionado]), True, bg)
    posTxt = posX - txt.get_size()[0] / 2, posY - txt.get_size()[1] / 2

    mais = fonte.render(">", True, bg)
    menos = fonte.render("<", True, bg)

    centros = [
        [mais.get_size()[0] / 2, mais.get_size()[1] / 2],
        [menos.get_size()[0] / 2, menos.get_size()[1] / 2]
    ]

    posMais = (posX + rect[3] * 2) - centros[0][0], posY - centros[0][1]
    posMenos = (posX - rect[3] * 2) - centros[1][0], posY - centros[1][1]


    container = engine.draw.rect(tela, branco, rect)
    engine.draw.rect(tela, branco, container, 3)

    mPos = engine.mouse.get_pos()


    if container.collidepoint(mPos):
        container = engine.draw.rect(tela, highlight, rect)
        engine.draw.rect(tela, highlight, container, 3)


    mais = tela.blit(mais, posMais)
    menos = tela.blit(menos, posMenos)

    tela.blit(txt, posTxt)


    if mais.collidepoint(mPos):
        if click(eventos):
            if selecionado +1 < len(opcoes):
                selecionado += 1
            else:
                selecionado = 0

    if menos.collidepoint(mPos):
        if click(eventos):
            if selecionado -1 > -1:
                selecionado -= 1
            else:
                selecionado = len(opcoes) -1
            

    return selecionado

def click(evento):
    if evento != None and evento.type == engine.MOUSEBUTTONDOWN:
        return True