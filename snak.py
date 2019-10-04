from os import _exit
from time import sleep
from threading import Thread as th
from LoadGame import render, relogio, keyPress, engine, inicio, menu, checkScore
from User import checkSessao

if checkSessao() != True:
    inicio()

menu()

## iniciando a funçao render numa thread separada pra n ficar td junto
th(target=render).start()

while(True):
    
    ## print pra ver o fps
    ## o end = "\r" serve para 
    ## ele n printar em outra linha
    print("\t", int(relogio.get_fps()), end="\r")

    checkScore()

    ## se tiver eventos acontecendo ele vai pegar o evento
    for event in engine.event.get():

        ## ai ele vai ver a categoria/tipo do evento
        if event.type == engine.KEYDOWN:
            
            ## quando o evento é tecla pressionada
            ## ele manda a tecla pra uma funçao q vai ver qual tecla
            ## q o cara aperto
            if keyPress(event.key) == "esc":
                menu()
    

        ## se for sair ele fecha tudo
        elif event.type == engine.QUIT:
            _exit(0)
            
