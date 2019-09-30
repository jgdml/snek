import pygame as engine
from os import _exit
from random import randint
from time import sleep

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


def aumentar():
    global calda
    calda.append(0)


def novaComida():
    global posComida
    posComida = [randint(tamComida[0], resolucao[0] - tamComida[0]), randint(tamComida[1], resolucao[1] - tamComida[1]), tamComida[0], tamComida[1]]


def colisaoComida(obj1, obj2):
    global vel
    if obj1.colliderect(obj2):
        aumentar()
        novaComida()
        vel += tam[0] * 0.02


def paredeTeleporte():
    global rectPlayer
    ## esses ifs sao para teleportar o player
    ## quando ele toca a parede
    if rectPlayer[0] > resolucao[0] + 1:
        rectPlayer[0] = 2

    if rectPlayer[0] < 1:
        rectPlayer[0] = resolucao[0]

    if rectPlayer[1] > resolucao[1] + 1:
        rectPlayer[1] = 2

    if rectPlayer[1] < 1:
        rectPlayer[1] = resolucao[1]

    return False


def paredeMorte(rect):
    val = False

    ## esses sao para finalizar o jogo quando
    ## o player toca a parede
    if rect[0] > resolucao[0] or rect[0] < 1:
        val = True

    if rect[1] > resolucao[1] or rect[1] < 1:
        val = True

    return val


def colisaoParede(rect):

    ## morrer quando tocar a parede
    return paredeMorte(rect)

    ## teleporte quando tocar a parede
    # return paredeTeleporte()


def keyPress(tecla):
    global reset

    if tecla == engine.K_r and fim:
        reset = True

    else:
        movimentos(tecla)


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
    if direcao[0] != "y":
        if tecla == engine.K_UP:
            direcao = "y-"
        elif tecla == engine.K_DOWN:
            direcao = "y+"


def bot():
    global direcao

    if rectPlayer[0] > posComida[0]:
        direcao = "x-"

        if rectPlayer[1] > posComida[1]:
            direcao = "y-"

    else:
        direcao = "x+"

        if rectPlayer[1] < posComida[1]:
            direcao = "y+"


def resetAll():
    global rectPlayer, fim, reset, direcao, vel

    fim = False
    reset = False
    direcao = "nulo"
    vel = tam[0] * 0.2
    rectPlayer = [(resolucao[0] // 2) - tam[0] // 2, (resolucao[1] // 2) - tam[1] // 2, tam[0], tam[1]]
    novaComida()

def render():
    global calda, fim

    def gameover():
        ## tela de gameover
        player = engine.draw.rect(tela, playerCor, rectPlayer)
        comida = engine.draw.rect(tela, comidaCor, posComida)
        tela.blit(score, posScore)
        tela.blit(restart, posRestart)
        engine.display.update()

    def drawCalda():
        for i in range(0, len(calda)):

            ## desenhar cada parte da calda
            c = engine.draw.rect(tela, caldaCor, arr[len(arr) - delayCalda * (i + 1)])

            ## checar se o player colidiu com a calda
            if player.colliderect(c) and i > 10:
                return True

            ## deletar elementos da array
            ## para ela nao ficar muito grande
            if len(arr) > len(calda):
                arr.pop(0)


    arr = [rectPlayer] * tamInicial
    calda = [0] * tamInicial


    while(True):
        ## pintar a tela de preto
        tela.fill(0)

        player = engine.draw.rect(tela, playerCor, rectPlayer)
        arr.append(player)


        if drawCalda() or colisaoParede(player):
            fim = True
            gameover()

            while(True):

                if reset:
                    resetAll()
                    arr = [rectPlayer] * tamInicial
                    calda = [0] * tamInicial
                    break


        ## desenhar a cobra denovo
        ## pra ficar em cima da calda
        player = engine.draw.rect(tela, playerCor, rectPlayer)

        ## desenhar comida
        comida = engine.draw.rect(tela, comidaCor, posComida)

        ## dando update no score
        score = fonte.render(str((len(calda) - tamInicial) * 500), True, caldaCor)

        ## update na posiçao do score
        posScore = (resolucao[0] / 2) - score.get_size()[0] / 2, 0

        ## colocando score na tela
        tela.blit(score, ((resolucao[0] / 2) - score.get_size()[0] / 2, 0))


        ## fazer a cobra andar um pouco a cada frame
        autoRun()

        ## chama essa funcao a cada frame
        ## pro bot analisar e decidir oq fazer
        # bot()

        ## checa se o player colidiu com a comida
        colisaoComida(player, comida)

        ## checa se algo colidiu com a parede
        ## nesse caso o player

        ## fazer um update senao fica td bugado
        engine.display.update()

        ## esse relogio.tick substitui o sleep
        ## o parametro dele é o máximo de fps que o jogo vai rodar
        relogio.tick_busy_loop(limiteFps)

    # gameover()

## inicia tudo do pygame
engine.init()

engine.display.set_caption("Snek")

## pega informaçao do display
getRes = engine.display.Info()

## guarda a res do display numa array
resolucao = [int(getRes.current_w / 1.5), int(getRes.current_h / 1.5)]

##inicia a tela com a resolucao
tela = engine.display.set_mode(resolucao)

## definindo relogio como uma variável para ficar mais fácil
relogio = engine.time.Clock()

limiteFps = 200

## define o tamanho da cobra de acordo com o display
## nesse caso o tamanho eh 2% do tamanho do display
tam = [int(resolucao[0] * 0.02)] * 2

tamComida = tam

## [0, 1] sao as posiçoes da cobra e [2, 3] eh o tamanho
rectPlayer = [(resolucao[0] // 2) - tam[0] // 2, (resolucao[1] // 2) - tam[1] // 2, tam[0], tam[1]]

## calcula a velocidade da cobra com base no tamanho do player
## vel eh 20% do tamanho
vel = tam[0] * 0.15

# o delay q a calda vai ter
# para pegar a posicao do player
delayCalda = 1
tamInicial = 10

playerCor = 50, 255, 50
caldaCor = 255, 255, 255
comidaCor = 255, 100, 100
## a variavel q vai definir pra onde a cobra vai se mexer
direcao = "nulo"

## tipo de fonte e tamanho dela
fonte = engine.font.SysFont("monospace_bold", int(resolucao[0] * 0.04))

## fazer um texto predefinido para renderizar depois
restart = fonte.render("R = Reset", True, caldaCor)

## posição do texto de restart
posRestart = (resolucao[0] / 2) - restart.get_size()[0] / 2, resolucao[1] - restart.get_size()[1]

novaComida()

## pra resetar o jogo se o usuario
## apertar R
reset = False

## pra informar que o jogo acabou
fim = False