from Defaults import *

def Check(title, event, posX, posY, var):
    
    corX = branco
    title = fonte.render(title, True, branco)
    titleSize = title.get_size()
    rect = [resolucao[1] * 0.06, resolucao[1] * 0.06]

    caixa = [posX - rect[0]/2 - titleSize[0]/2, posY - rect[1]/2, rect[0], rect[1]]

    linePos = [[caixa[0]*1.01, caixa[1]], [(caixa[0]+rect[0])/1.01, caixa[1]+rect[1]]]

    caixa = engine.draw.rect(tela, branco, caixa, 2)
    texto = tela.blit(title, (caixa[0] *1.11, caixa[1]))

    if caixa.collidepoint(engine.mouse.get_pos()) or texto.collidepoint(engine.mouse.get_pos()):
        engine.draw.rect(tela, branco, caixa)
        corX = bg
        if event and event.type == engine.MOUSEBUTTONDOWN:
            if var:
                var = False
            else:
                var = True

    if var:
        engine.draw.line(tela, corX, linePos[0], linePos[1], 6)
        engine.draw.line(tela, corX, (linePos[1][0], linePos[0][1]), (linePos[0][0], linePos[1][1]), 6)

    return var
