from Arqs.Defaults import engine
from User import jogoSair


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