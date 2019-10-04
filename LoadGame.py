import pygame as engine
from os import _exit
from random import randint
from time import sleep
from User import login, getCor, cadastro, mudarSkin, uploadScore, mostrarScores, logSessao, delSessao

def event():
    for event in engine.event.get():
        
        if event.type == engine.QUIT:
            _exit(0)

        return event


def boxMenu(texto, evento, posX, posY, func):

    txtSize = fonte.size(texto)
    txt = engine.font.Font.render(fonte, texto, True, branco)

    rectTam = txtSize[0] + resolucao[0] * 0.1, txtSize[1] + resolucao[1] * 0.027

    caixa = [posX - rectTam[0] // 2, posY - rectTam[1] // 2, rectTam[0], rectTam[1]]

    caixa = engine.draw.rect(tela, branco, caixa, 2)
    

    if caixa.collidepoint(engine.mouse.get_pos()):
        caixa = engine.draw.rect(tela, branco, caixa)
        txt = engine.font.Font.render(fonte, texto, True, bg)
        if evento != None and evento.type == engine.MOUSEBUTTONDOWN:
            return func()
    
    tela.blit(txt, (posX - txtSize[0] / 2, posY - txtSize[1] / 2))



def textInput(posX, posY, txt, evento, txtIn):
    txt = engine.font.Font.render(fonte, txt, True, branco)
    txtSize = txt.get_size()

    txtInShow = engine.font.Font.render(fonte, txtIn + "|", True, branco)
    txtInSize = txtInShow.get_size()

    rectTam = [resolucao[0] * 0.2, resolucao[1] * 0.06]
    if txtInSize[0] > rectTam[0]:
        rectTam[0] = txtInSize[0]

    tela.blit(txt, (posX - txtSize[0] / 2, posY - txtSize[1] * 2))

    caixa = [posX - rectTam[0] // 2, posY - rectTam[1] // 2, rectTam[0], rectTam[1]]
    caixa = engine.draw.rect(tela, branco, caixa, 2)

    if caixa.collidepoint(engine.mouse.get_pos()):
        txtInShow = engine.font.Font.render(fonte, (txtIn + "|"), True, bg)
        caixa = engine.draw.rect(tela, branco, caixa)
        
        if evento != None and evento.type == engine.KEYDOWN:
            return evento.key if evento.key == engine.K_BACKSPACE else evento.unicode

    tela.blit(txtInShow, (posX - txtInSize[0] / 2, posY - txtInSize[1] / 2))
    
    return ""

def quebra():
    global reset
    reset = True
    fim = False
    return True

def inicio():
    def cadastroTela():
        loginTxt = ""
        senhaTxt = ""
        resultado = ""
        resRender = engine.font.Font.render(fonte, resultado, True, vermelho)
        while(True):
            tela.fill(bg)
            

            evento = event()

            retLogin = textInput(resolucao[0] / 2, posCaixa[10], "Login", evento, loginTxt)

            if retLogin == engine.K_BACKSPACE:
                loginTxt = loginTxt[0: len(loginTxt) - 1]
            else:
                loginTxt += retLogin


            retSenha = textInput(resolucao[0] / 2, posCaixa[13], "Senha", evento, "*" * len(senhaTxt))

            if retSenha == engine.K_BACKSPACE:
                senhaTxt = senhaTxt[0: len(senhaTxt) - 1]
                
            else:
                senhaTxt += retSenha

        
            ret = boxMenu("Cadastrar", evento, resolucao[0] / 2, posCaixa[17], lambda: cadastro(loginTxt, senhaTxt))
            if ret != None:
                resultado = ret
            
            
            if ret != None and ret[0] == "O":
                resRender = engine.font.Font.render(fonte, resultado, True, verde)
            elif ret != None:  
                resRender = engine.font.Font.render(fonte, resultado, True, vermelho)

            resRenderS = resRender.get_size()
            tela.blit(resRender, (resolucao[0] / 2 - resRenderS[0] / 2, resolucao[1] * 0.4))
        
            if boxMenu("<", evento, resolucao[0] * 0.06, resolucao[1] * 0.952, quebra):
                break

            engine.display.update()


    loginTxt = ""
    senhaTxt = ""
    resultado = ""

    while(True):
        tela.fill(bg)

        evento = event()

        retLogin = textInput(resolucao[0] / 2, posCaixa[10], "Login", evento, loginTxt)

        if retLogin == engine.K_BACKSPACE:
            loginTxt = loginTxt[0: len(loginTxt) - 1]
        else:
            loginTxt += retLogin



        retSenha = textInput(resolucao[0] / 2, posCaixa[13], "Senha", evento, "*" * len(senhaTxt))

        if retSenha == engine.K_BACKSPACE:
            senhaTxt = senhaTxt[0: len(senhaTxt) - 1]
            
        else:
            senhaTxt += retSenha


        ret = boxMenu("Logar", evento, resolucao[0] / 2, posCaixa[17], lambda: login(loginTxt, senhaTxt))
        if ret == True:
            break
        elif ret != None:
            resultado = ret
        
        resRender = engine.font.Font.render(fonte, resultado, True, vermelho)
        resRenderS = resRender.get_size()
        tela.blit(resRender, (resolucao[0] / 2 - resRenderS[0] / 2, resolucao[1] * 0.4))

        boxMenu("Cadastrar-se", evento, resolucao[0] * 0.178, resolucao[1] * 0.952, cadastroTela)

        engine.display.update()
        
    

def menu():
    global corCobra
    log = True

    while(True):
        tela.fill(bg)
        evento = event()

        if boxMenu("Jogar", evento, resolucao[0] / 2, posCaixa[9], quebra):
            break

        boxMenu("Highscores", evento, resolucao[0] / 2, posCaixa[11], mostrarScores)

        boxMenu("Skin", evento, resolucao[0] / 2, posCaixa[13], mudarSkin)

        if boxMenu("Logout", evento, resolucao[0] / 2, posCaixa[15], quebra):
            log = False
            break

        boxMenu("Sair", evento, resolucao[0] / 2, posCaixa[17], lambda: _exit(0))

        engine.display.update()
        
    
    if log != True:
        delSessao()
        logoutConta()
    corCobra = getCor()
    corBorda = getCor()


def logoutConta():
    inicio()
    menu()


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


def novaComida():
    global posComida
    posComida = [randint(tamComida[0], resolucao[0] - tamComida[0]), randint(tamComida[1], resolucao[1] - tamComida[1]), tamComida[0], tamComida[1]]


def colisaoComida(obj1, obj2):
    global vel, calda

    if obj1.colliderect(obj2):
        calda += 1
        vel += resolucao[1] * 0.0001
        novaComida()


def paredeTeleporte():
    global rectPlayer
    ## esses ifs sao para teleportar o player
    ## quando ele toca a parede
    if rectPlayer[0] > resolucao[0] + 1:
        rectPlayer[0] = 1

    if rectPlayer[0] < 1:
        rectPlayer[0] = resolucao[0]

    if rectPlayer[1] > resolucao[1] + 1:
        rectPlayer[1] = 1

    if rectPlayer[1] < 1:
        rectPlayer[1] = resolucao[1]

    return False


def paredeMorte(rect):
    val = False

    ## esses sao para finalizar o jogo quando
    ## o player toca a parede
    if rect[0] > resolucao[0] - rect[2] or rect[0] < 1:
        val = True

    if rect[1] > resolucao[1] - rect[3] or rect[1] < 1:
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

    elif tecla == engine.K_ESCAPE and fim:
        return "esc"

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


def checkScore():
    global upload
    if upload:
        uploadScore((calda - tamInicial) * 450)
        upload = False


def render():
    global calda, fim

    def gameover():
        global upload
        upload = True
        ## tela de gameover
        player = engine.draw.rect(tela, corCobra, rectPlayer)
        comida = engine.draw.rect(tela, vermelho, posComida)
        engine.draw.rect(tela, vermelho, comida, 3)
        tela.blit(score, posScore)
        tela.blit(restart, posRestart)
        tela.blit(sair, posSair)
        engine.display.update()

    def drawCalda():
        for i in range(0, calda):

            ## desenhar cada parte da calda
            c = engine.draw.rect(tela, corCobra, arr[len(arr) - delayCalda * (i + 1)])
            engine.draw.rect(tela, corBorda, c, 3)

            ## checar se o player colidiu com a calda
            if player.colliderect(c) and i > 9:
                return True

            ## deletar elementos da array
            ## para ela nao ficar muito grande
            if len(arr) > calda:
                arr.pop(0)

    ## array que vai ter as posições
    ## passadas do player
    arr = [rectPlayer] * tamInicial

    ## tamanho da calda
    calda = tamInicial

    if fim != True:
        while(True):
            ## pintar a tela de preto
            tela.fill(bg)

            ## desenhar player
            player = engine.draw.rect(tela, corCobra, rectPlayer)

            ## colocar a posiçao da cobra 
            ## em um array para usar para
            ## desenhar a calda
            arr.append(player)

            ## se uma dessas funçoes retornar true
            ## significa que o player encostou na calda
            ## ou colidiu ocm a parede
            if drawCalda() or colisaoParede(player):
                fim = True
                gameover()

                while(True):

                    if reset:
                        resetAll()
                        arr = [rectPlayer] * tamInicial
                        calda = tamInicial
                        break


            ## desenhar a cobra denovo
            ## pra ficar em cima da calda
            player = engine.draw.rect(tela, corCobra, rectPlayer)

            player = engine.draw.rect(tela, corBorda, player, 3)

            ## desenhar comida
            comida = engine.draw.rect(tela, vermelho, posComida)
            engine.draw.rect(tela, vermelho, comida, 3)

            ## dando update no score
            score = fonte.render(str((calda - tamInicial) * 450), True, branco)

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

            ## fazer um update senao fica td bugado
            engine.display.update()

            ## esse relogio.tick substitui o sleep
            ## o parametro dele é o máximo de fps que o jogo vai rodar
            relogio.tick_busy_loop(limiteFps)


## inicia tudo do pygame
engine.init()

engine.display.set_caption("Snek")

## pega informaçao do display
getRes = engine.display.Info()

## guarda a res do display numa array
resolucao = [int(getRes.current_w), int(getRes.current_h)]

##inicia a tela com a resolucao
tela = engine.display.set_mode(resolucao, engine.FULLSCREEN)

posCaixa = []
for i in range(1, 21):
    posCaixa.append((resolucao[1] / 20) * i)

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

bg = 10, 10, 10
branco = 255, 255, 255
vermelho = 255, 100, 100
verde = 50, 255, 50
corBorda = 255, 255, 255

## a variavel q vai definir pra onde a cobra vai se mexer
direcao = "nulo"

## tipo de fonte e tamanho dela
fonte = engine.font.Font("font\\Font2.otf", int(resolucao[0] * 0.0265))

## fazer um texto predefinido para renderizar depois
restart = fonte.render("R = Reset", True, branco)

## posição do texto de restart
posRestart = (resolucao[0] / 2) - restart.get_size()[0] / 2, resolucao[1] - restart.get_size()[1]


sair = fonte.render("ESC = Menu", True, branco)

posSair = (resolucao[0] / 2 - sair.get_size()[0] / 2, posRestart[1] - sair.get_size()[1])


## pra resetar o jogo se o usuario
## apertar R
reset = False

## pra informar que o jogo acabou
fim = False

upload = False


novaComida()
