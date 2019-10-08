from Defaults import *

def textInput(posX, posY, txt, evento, txtIn):
    txt = engine.font.Font.render(fonte, txt, True, branco)
    txtSize = txt.get_size()

    txtInShow = engine.font.Font.render(fonte, txtIn + "|", True, branco)
    txtInSize = txtInShow.get_size()

    rectTam = [resolucao[0] * 0.2, resolucao[1] * 0.06]
    if txtInSize[0] > rectTam[0]:
        rectTam[0] = txtInSize[0]

    tela.blit(txt, (posX - txtSize[0] / 2, posY - txtSize[1] * 2))

    caixa = [posX - rectTam[0] // 2, posY - rectTam[1] // 2, rectTam[0], rectTam[1]]
    caixa = engine.draw.rect(tela, branco, caixa, 2)

    if caixa.collidepoint(engine.mouse.get_pos()):
        txtInShow = engine.font.Font.render(fonte, (txtIn + "|"), True, bg)
        caixa = engine.draw.rect(tela, branco, caixa)
        
        if evento != None and evento.type == engine.KEYDOWN:
            return evento.key if evento.key == engine.K_BACKSPACE else evento.unicode

    tela.blit(txtInShow, (posX - txtInSize[0] / 2, posY - txtInSize[1] / 2))
    
    return ""