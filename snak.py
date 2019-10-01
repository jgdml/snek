from os import _exit
from time import sleep
from threading import Thread as th
from LoadGame import render, relogio, keyPress, engine
from User import cadastro, login

cadastro()

## iniciando a funçao render numa thread separada pra n ficar td junto
th(target=render).start()

while(True):
    
    ## print pra ver o fps
    ## o end = "\r" serve para 
    ## ele n printar em outra linha
    print("\t", int(relogio.get_fps()), end="\r")

    ## se tiver eventos acontecendo ele vai pegar o evento
    for event in engine.event.get():

        ## ai ele vai ver a categoria/tipo do evento
        if event.type == engine.KEYDOWN:
            
            ## quando o evento é tecla pressionada
            ## ele manda a tecla pra uma funçao q vai ver qual tecla
            ## q o cara aperto
            keyPress(event.key)

        ## se for sair ele fecha tudo
        elif event.type == engine.QUIT:
            _exit(0)
            
