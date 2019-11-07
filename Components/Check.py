from Defaults import *

def Check(title, event, posX, posY, var):
    
    corX = branco
    rect = posX, posY, resolucao[1] * 0.06, resolucao[1] * 0.06
    title = fonte.render(title, True, branco)

    linePos = [[posX*1.01, posY*1.005], [posX+rect[2]*0.9, posY+rect[3]*0.96]]

    caixa = engine.draw.rect(tela, branco, rect, 2)
    texto = tela.blit(title, (posX * 1.03 + rect[2], posY*1.01))

    if caixa.collidepoint(engine.mouse.get_pos()) or texto.collidepoint(engine.mouse.get_pos()):
        engine.draw.rect(tela, branco, rect)
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
