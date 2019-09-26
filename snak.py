import pygame as engine
from time import sleep
from threading import Thread as th
from os import _exit

def render():
    while(True):
        ## pintar a tela de preto
        tela.fill(0)

        ## desenhar a cobra
        engine.draw.rect(tela, branco, rectCobra)

        ## fazer a cobra andar um pouco a cada frame
        autoRun()

        ## fazer um update senao fica td bugado
        engine.display.update()

        ## esse relogio.tick substitui o sleep
        ## o parametro dele é o máximo de fps que o jogo vai rodar
        relogio.tick(240)

def autoRun():
    ## a direçao eh global pra agnt poder mudar ela fora da funçao
    global direction

    if direction == "x+":
        rectCobra[0] += vel

    elif direction == "x-":
        rectCobra[0] -= vel

    elif direction == "y+":
        rectCobra[1] += vel

    elif direction == "y-":
        rectCobra[1] -= vel

## inicia tudo do pygame
engine.init()   

## pega informaçao do display
getRes = engine.display.Info()

## guarda a res do display numa array
resolucao = [int(getRes.current_w / 1.5), int(getRes.current_h / 1.5)]

##inicia a tela com a resolucao
tela = engine.display.set_mode(resolucao)

## define o tamanho da cobra de acordo com o display
## nesse caso o tamanho eh 2% do tamanho do display
tam = [int(resolucao[0] * 0.02)] * 2

## [0, 1] sao as posiçoes da cobra e [2, 3] eh o tamanho
rectCobra = [(resolucao[0] // 2) - tam[0] // 2, (resolucao[1] // 2) - tam[1] // 2, tam[0], tam[1]]

## calcula a velocidade da cobra com base na resoluçao da tela
## vel eh 0,7% da resoluçao
vel = resolucao[0] * 0.0007

branco = 255, 255, 255

## definindo relogio como uma variável para ficar mais fácil
relogio = engine.time.Clock()

## a variavel q vai defini pra onde a cobra começa a se mexe
direction = "x+"

## iniciando a funçao render numa thread separada pra ficar menos marofa
th(target=render).start()

while(True):
    
    ## print pra ver o fps
    ## o end = "\r" serve para 
    ## ele n printar em outra linha
    print("\t", int(relogio.get_fps()), end="\r")

    for event in engine.event.get():
        if event.type == engine.KEYDOWN:
            if event.key == engine.K_RIGHT:
                direction = "x+"
            if event.key == engine.K_LEFT:
                direction = "x-"
            if event.key == engine.K_UP:
                direction = "y-"
            if event.key == engine.K_DOWN:
                direction = "y+"

        elif event.type == engine.QUIT:
            _exit(0)
            
