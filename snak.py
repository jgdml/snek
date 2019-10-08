from os import _exit
from time import sleep
from threading import Thread as th
from Arqs.LoadGame import render, relogio, keyPress, engine, telaInicial, telaMenu, checkScore
from Arqs.User import checkSessao, jogoSair
from Arqs.Funcs import event

if checkSessao() != True:
    telaInicial()

telaMenu()

## pegar o diretorio do arquivo

## iniciando a funçao render numa thread separada pra n ficar td junto
th(target=render).start()

while(True):
    
    checkScore()

    ## se tiver eventos acontecendo ele vai pegar o evento
    for eventos in engine.event.get():
    
        ## ai ele vai ver a categoria/tipo do evento
        if eventos.type == engine.KEYDOWN:
            
            ## quando o evento é tecla pressionada
            ## ele manda a tecla pra uma funçao q vai ver qual tecla
            ## q o cara aperto
            if keyPress(eventos.key) == "esc":
                telaMenu()
            
