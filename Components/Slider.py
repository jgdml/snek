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
    rect = [posX, posY, resolucao[0] * 0.2, resolucao[1] * 0.02]
    rect[0] = posX - rect[2] / 2
    

    rectPointer = [(posX - rect[0]), posY, rect[2] * 0.046, rect[3]]
    rectPointer[0] = int(rectPointer[0] * val)

    engine.draw.rect(tela, cor, rect)
    engine.draw.rect(tela, branco, rect, 2)
    tela.blit(displayVal, (rect[0], rect[1] - 30))
    engine.draw.rect(tela, branco, rectPointer)

    return val