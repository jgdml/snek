from Defaults import *

def Check(title, event, posX, posY, var):
    

    rect = posX, posY, resolucao[1] * 0.06, resolucao[1] * 0.06
    title = fonte.render(title, True, branco)

    linePos = [[posX*1.01, posY*1.005], [posX+rect[2]*0.9, posY+rect[3]*0.95]]

    caixa = engine.draw.rect(tela, branco, rect, 2)
    tela.blit(title, (posX * 1.03 + rect[2], posY + title.get_size()[1]/ 3.1))

    if caixa.collidepoint(engine.mouse.get_pos()):
        engine.draw.rect(tela, branco, rect)
        if event and event.type == engine.MOUSEBUTTONDOWN:
            if var:
                var = False
            else:
                var = True

    if var:
        engine.draw.line(tela, branco, linePos[0], linePos[1], 6)
        engine.draw.line(tela, branco, (linePos[1][0], linePos[0][1]), (linePos[0][0], linePos[1][1]), 6)

    return var
