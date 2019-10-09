from Defaults import *

def boxMenu(texto, evento, posX, posY, func):

    txtSize = fonte.size(texto)
    txt = engine.font.Font.render(fonte, texto, True, (0, 0, 0))

    rectTam = txtSize[0] + resolucao[0] * 0.1, txtSize[1] + resolucao[1] * 0.027

    caixa = [posX - rectTam[0] // 2, posY - rectTam[1] // 2, rectTam[0], rectTam[1]]

    caixa = engine.draw.rect(tela, branco, caixa)
    engine.draw.rect(tela, branco, caixa, 4)
    

    if caixa.collidepoint(engine.mouse.get_pos()):
        caixa[0] -= (caixa[2] * 0.2) / 2
        caixa[2] *= 1.2
        caixa = engine.draw.rect(tela, (150, 150, 150), caixa)
        engine.draw.rect(tela, (150, 150, 150), caixa, 4)
        txt = engine.font.Font.render(fonte, texto, True, bg)

        if evento != None and evento.type == engine.MOUSEBUTTONDOWN:
            return func()

    
    tela.blit(txt, (posX - txtSize[0] / 2, posY - txtSize[1] / 2))