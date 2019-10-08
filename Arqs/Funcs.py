from Defaults import engine, resolucao
from Arqs.User import jogoSair


def event():
    for event in engine.event.get():
        
        if event.type == engine.QUIT:
            jogoSair()

        return event



def resetJogar():
    global reset
    reset = True
    fim = False
    return True



def quebra():
    return True



def paredeMorte(rect):
    val = False

    ## esses sao para finalizar o jogo quando
    ## o player toca a parede
    if rect[0] > resolucao[0] - rect[2] or rect[0] < 1:
        val = True

    if rect[1] > resolucao[1] - rect[3] or rect[1] < 1:
        val = True

    return val



def colisaoParede(rect):

    ## morrer quando tocar a parede
    return paredeMorte(rect)

    ## teleporte quando tocar a parede
    # return paredeTeleporte()

