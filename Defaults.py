import pygame as engine
from os import path

## pegar o diretorio do arquivo
root = path.dirname(path.abspath(__file__)) + "\\"

## inicia tudo do pygame
engine.init()

engine.display.set_caption("Snek")

## pega informaçao do display
getRes = engine.display.Info()

config = open(root+"config.txt", "r")
full = config.readline()

if "1" in full:
    resolucao = [int(getRes.current_w), int(getRes.current_h)]
    flags = engine.FULLSCREEN | engine.DOUBLEBUF

    tela = engine.display.set_mode(resolucao, flags)
    
else:
    resolucao = [int(getRes.current_w / 1.5), int(getRes.current_h / 1.5)]
    flags = engine.DOUBLEBUF

    tela = engine.display.set_mode(resolucao, flags)

config.close()

tela.set_alpha(None)

posCaixa = []
for i in range(1, 21):
    posCaixa.append((resolucao[1] / 20) * i)

## definindo relogio como uma variável para ficar mais fácil
relogio = engine.time.Clock()

limiteFps = 120

## define o tamanho da cobra de acordo com o display
## nesse caso o tamanho eh 2% do tamanho do display
tam = [int(resolucao[0] * 0.02)] * 2

tamComida = tam

## [0, 1] sao as posiçoes da cobra e [2, 3] eh o tamanho
rectPlayer = [(resolucao[0] // 2) - tam[0] // 2, (resolucao[1] // 2) - tam[1] // 2, tam[0], tam[1]]

## calcula a velocidade da cobra com base no tamanho do player
## vel eh 20% do tamanho
vel = tam[0] * 0.2

# o delay q a calda vai ter
# para pegar a posicao do player
delayCalda = 1
tamInicial = 10

bg = 10, 10, 10
branco = 255, 255, 255
vermelho = 255, 100, 100
verde = 0, 255, 102
verde2 = 92, 255, 158
verde3 = 149, 255, 192
verde4 = 205, 255, 226
azul = 127, 178, 255
highlight = 150, 150, 150

## a variavel q vai definir pra onde a cobra vai se mexer
direcao = "nulo"

## tipo de fonte e tamanho dela
fonte = engine.font.Font(root+"Font\\Font2.otf", int(resolucao[0] * 0.0225))
fonteTitulo = engine.font.Font(root+"Font\\Font2.otf", int(resolucao[0] * 0.0565))
ultra = engine.font.Font(root+"Font\\Font2.otf", int(resolucao[0] * 0.07))

## fazer um texto predefinido para renderizar depois
restart = fonte.render("R = Reset", True, branco)

## posição do texto de restart
posRestart = (resolucao[0] / 2) - restart.get_size()[0] / 2, resolucao[1] - restart.get_size()[1]


sair = fonte.render("ESC = Menu", True, branco)

posSair = (resolucao[0] / 2 - sair.get_size()[0] / 2, posRestart[1] - sair.get_size()[1])


ultra = ultra.render("Ultra Snake", True, branco)

## pra resetar o jogo se o usuario
## apertar R
reset = False

## pra informar que o jogo acabou
fim = False

upload = False
