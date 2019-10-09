from Defaults import *

def slider(posX, posY, cor, val):
    if cor == "r":
        cor = 255, 50, 50

    elif cor == "g":
        cor = 50, 255, 50

    else:
        cor = 50, 50, 255

    branco = 255, 255, 255

    displayVal = engine.font.Font.render(fonte, str(val), True, branco)
    rect = [posX, posY, resolucao[0] * 0.24, resolucao[1] * 0.05]
    rect[0] = posX - rect[2] / 2
    

    rectPointer = [posX - rect[2] / 2, rect[1], rect[2] * 0.046, rect[3]]
    pointerDiv = rect[2] / 265
    rectPointer[0] += pointerDiv * val

    dentro = engine.draw.rect(tela, cor, rect)
    borda = engine.draw.rect(tela, branco, rect, 2)

    mPos = engine.mouse.get_pos()

    if dentro.collidepoint(mPos) or borda.collidepoint(mPos):
        if engine.mouse.get_pressed()[0]:
            rectPointer[0] = mPos[0] - rectPointer[2] / 2
            val = int((rectPointer[0] - rect[0]) / pointerDiv)
            if val < 0:
                val = 0

    engine.draw.rect(tela, branco, rectPointer)
    displayVal = engine.font.Font.render(fonte, str(val), True, branco)
    tela.blit(displayVal, (posX - displayVal.get_size()[0] / 2, posY - rect[3]))


    return val 