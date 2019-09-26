import pygame as engine
from time import sleep
from threading import Thread as th
from os import _exit

def render():
    while(True):
        tela.fill(0)
        engine.draw.rect(tela, branco, rectCobra)
        movimento()

        engine.display.update()
        sleep(0.00000001)

def autoRun(direction):
    if direction == "x+":
        rectCobra[0] += vel

    elif direction == "x-":
        rectCobra[0] -= vel

    elif direction == "y+":
        rectCobra[1] += vel

    elif direction == "y-":
        rectCobra[1] -= vel

def movimento():
    for event in engine.event.get():
        if event.type == engine.KEYDOWN:
            if event.KEY == engine.K_RIGHT:
                autoRun("x+")


movimento()

engine.display.init()   

getRes = engine.display.Info()
resolucao = [int(getRes.current_w / 1.5), int(getRes.current_h / 1.5)]
tela = engine.display.set_mode(resolucao)

tam = [int(resolucao[0] * 0.02)] * 2

rectCobra = [(resolucao[0] // 2) - tam[0] // 2, (resolucao[1] // 2) - tam[1] // 2, tam[0], tam[1]]

vel = 0.3

branco = 255, 255, 255

th(target=render).start()

while(True):

    for event in engine.event.get():
        if event.type == engine.QUIT:
            _exit(0)
    sleep(0.00001)
