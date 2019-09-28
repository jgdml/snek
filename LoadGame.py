import pygame as engine
from os import _exit
from random import randint

def autoRun():
    ## a direçao eh global pra agnt poder mudar ela fora da funçao
    global direcao

    if direcao == "x+":
        rectPlayer[0] += vel

    elif direcao == "x-":
        rectPlayer[0] -= vel

    elif direcao == "y+":
        rectPlayer[1] += vel

    elif direcao == "y-":
        rectPlayer[1] -= vel


def movimentos(tecla):
    global direcao

    ## se ele nao estiver andando na horizontal
    ## troque a posiçao horizontal

    if direcao[0] != "x":
        if tecla == engine.K_RIGHT:
            direcao = "x+"
        elif tecla == engine.K_LEFT:
            direcao = "x-"

    ## se ele nao estiver andando na vertical
    ## troque a posiçao vertical
    else:
        if tecla == engine.K_UP:
            direcao = "y-"
        elif tecla == engine.K_DOWN:
            direcao = "y+"

def aumentar():
    global calda 
    calda.append(0)


def novaComida():
    global posComida
    posComida = [randint(tamComida[0], resolucao[0] - tamComida[0]), randint(tamComida[1], resolucao[1] - tamComida[1]), tamComida[0], tamComida[1]]


def colisaoComida(obj1, obj2):
    if obj1.colliderect(obj2):
        aumentar()
        novaComida()
    

def colisaoParede(rect):
    if rect[0] > resolucao[0] or rect[0] < 1:
        _exit(0)

    if rect[1] > resolucao[1] or rect[0] < 1:
        _exit(0)


def render():
    global calda
    arr = [rectPlayer] * 12
    calda = [0] * 2
    while(True):
        ## pintar a tela de preto
        tela.fill(0)

        ## desenhar a cobra
        player = engine.draw.rect(tela, playerCor, rectPlayer)
        arr.append(player)

        for i in range(0, len(calda)):
            engine.draw.rect(tela, playerCor, arr[len(arr) - 11 * (i +1)])

        comida = engine.draw.rect(tela, playerCor, posComida)

        ## fazer a cobra andar um pouco a cada frame
        autoRun()
        colisaoComida(player, comida)
        colisaoParede(player)

        ## fazer um update senao fica td bugado
        engine.display.update()

        ## esse relogio.tick substitui o sleep
        ## o parametro dele é o máximo de fps que o jogo vai rodar
        relogio.tick(240)

## inicia tudo do pygame
engine.init()   

## pega informaçao do display
getRes = engine.display.Info()

## guarda a res do display numa array
resolucao = [int(getRes.current_w / 1.5), int(getRes.current_h / 1.5)]

##inicia a tela com a resolucao
tela = engine.display.set_mode(resolucao)

## definindo relogio como uma variável para ficar mais fácil
relogio = engine.time.Clock()

## define o tamanho da cobra de acordo com o display
## nesse caso o tamanho eh 2% do tamanho do display
tam = [int(resolucao[0] * 0.02)] * 2

tamComida = tam
## [0, 1] sao as posiçoes da cobra e [2, 3] eh o tamanho
rectPlayer = [(resolucao[0] // 2) - tam[0] // 2, (resolucao[1] // 2) - tam[1] // 2, tam[0], tam[1]]

## calcula a velocidade da cobra com base na resoluçao da tela
## vel eh 0,7% da resoluçao
vel = resolucao[0] * 0.0012

playerCor = 255, 255, 255

## a variavel q vai definir pra onde a cobra vai se mexer
direcao = "x+"

novaComida()
