from Defaults import *

def boxMenu(texto, evento, posX, posY, func):

    txtSize = fonte.size(texto)
    txt = engine.font.Font.render(fonte, texto, True, branco)

    rectTam = txtSize[0] + resolucao[0] * 0.1, txtSize[1] + resolucao[1] * 0.027

    caixa = [posX - rectTam[0] // 2, posY - rectTam[1] // 2, rectTam[0], rectTam[1]]

    caixa = engine.draw.rect(tela, branco, caixa, 2)
    

    if caixa.collidepoint(engine.mouse.get_pos()):
        caixa = engine.draw.rect(tela, branco, caixa)
        txt = engine.font.Font.render(fonte, texto, True, bg)
        if evento != None and evento.type == engine.MOUSEBUTTONDOWN:
            return func()
    
    tela.blit(txt, (posX - txtSize[0] / 2, posY - txtSize[1] / 2))