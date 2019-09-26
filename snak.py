import pygame as engine
from time import sleep
from threading import Thread as th
from os import _exit

def render():
    while(True):
        tela.fill(0)
        engine.draw.rect(tela, branco, rectCobra)
        autoRun()

        engine.display.update()
        sleep(0.001)

def autoRun():
    global direction

    if direction == "x+":
        rectCobra[0] += vel

    elif direction == "x-":
        rectCobra[0] -= vel

    elif direction == "y+":
        rectCobra[1] += vel

    elif direction == "y-":
        rectCobra[1] -= vel


engine.init()   

getRes = engine.display.Info()
resolucao = [int(getRes.current_w / 1.5), int(getRes.current_h / 1.5)]
tela = engine.display.set_mode(resolucao)

tam = [int(resolucao[0] * 0.02)] * 2

rectCobra = [(resolucao[0] // 2) - tam[0] // 2, (resolucao[1] // 2) - tam[1] // 2, tam[0], tam[1]]

vel = resolucao[0] * 0.0007

branco = 255, 255, 255

direction = "x+"

th(target=render).start()

while(True):

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
            
    sleep(0.00001)
