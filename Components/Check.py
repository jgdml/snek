from Defaults import *

def Check(title, event, posX, posY, var):
    

    rect = posX, posY, resolucao[1] * 0.06, resolucao[1] * 0.06
    title = fonte.render(title, True, branco)


    engine.draw.rect(tela, branco, rect, 2)
    tela.blit(title, (posX * 1.03 + rect[2], posY + title.get_size()[1]/ 3.1))

    return var
