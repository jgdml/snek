from os import _exit
from random import randint
from time import sleep

from Arqs.User import *
from Components.BoxMenu import boxMenu
from Components.Slider import slider
from Components.TextInput import textInput
from Defaults import *
from Arqs.Funcs import *

def blitNome():
    tela.blit(ultra, (resolucao[0] / 2 - ultra.get_size()[0] / 2, ultra.get_size()[1] / 2))


def blitBg():
    tela.fill(bg)


def logoutConta():
    delSessao()
    telaInicial()
    telaMenu()


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



def gameover(score):
    global upload
    posScore = (resolucao[0] / 2) - score.get_size()[0] / 2, 0
    upload = True
    ## tela de gameover
    player = engine.draw.rect(tela, corCobra, rectPlayer)
    comida = engine.draw.rect(tela, vermelho, posComida)
    engine.draw.rect(tela, vermelho, comida, 1)
    tela.blit(score, posScore)
    tela.blit(restart, posRestart)
    tela.blit(sair, posSair)
    engine.display.update()



def resetJogar():
    global reset
    reset = True
    fim = False
    return True



def telaCadastro():
    loginTxt = ""
    senhaTxt = ""
    resultado = ""
    resRender = engine.font.Font.render(fonte, resultado, True, vermelho)
    while(True):
        blitBg()
        
        blitNome()

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
    
        if boxMenu("<", evento, resolucao[0] * 0.06, resolucao[1] * 0.962, quebra):
            break

        engine.display.update()


def telaInicial():

    loginTxt = ""
    senhaTxt = ""
    resultado = ""

    while(True):
        blitBg()

        blitNome()

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

        boxMenu("Cadastrar-se", evento, resolucao[0] * 0.146, resolucao[1] * 0.962, telaCadastro)

        engine.display.update()
        
    

def telaMenu():
    global corCobra, corBorda    
    corCobra = getCor("base")
    corBorda = getCor("borda")

    while(True):
        blitBg()
        evento = event()

        blitNome()

        if boxMenu("Jogar", evento, resolucao[0] / 2, posCaixa[11], resetJogar):
            break

        boxMenu("Highscores", evento, resolucao[0] / 2, posCaixa[13], telaScores)

        boxMenu("Opções", evento, resolucao[0] / 2, posCaixa[15], telaOpcoes)

        boxMenu("Sair", evento, resolucao[0] / 2, posCaixa[17], jogoSair)

        engine.display.update()

    
    
def telaScores():

    topScores = mostrarScores()
    renderScores = []
    titulo = engine.font.Font.render(fonteTitulo, "Highscores", True, branco)

    for i in range(0, len(topScores)):
        renderScores.append([engine.font.Font.render(fonte, topScores[i][0], True, branco), engine.font.Font.render(fonte, str(topScores[i][1]), True, branco)])
    
    rectLinha = [resolucao[0] * 0.55, resolucao[1] * 0.01]

    while(True):
        blitBg()
        eventos = event()

        tela.blit(titulo, (resolucao[0] / 2 - titulo.get_size()[0] / 2, titulo.get_size()[1] / 2))


        for i in range(0, len(renderScores)):

            if i == 0:
                corLinha = verde
                
            elif i == 1:
                corLinha = verde2

            elif i == 2:
                corLinha = verde3

            else:
                corLinha = verde4

            if len(topScores[i]) > 2:
                corLinha = azul
            
            size = [renderScores[i][0].get_size()[0], renderScores[i][1].get_size()[0]]

            tela.blit(renderScores[i][0], (resolucao[0] / 2 - size[0] / 2 - resolucao[0] * 0.10, posCaixa[i+3]))
            tela.blit(renderScores[i][1], (resolucao[0] / 2 - size[1] / 2 + resolucao[0] * 0.10, posCaixa[i+3]))
            engine.draw.rect(tela, corLinha, (resolucao[0] / 2 - rectLinha[0] / 2, posCaixa[i+4] - 10, rectLinha[0], rectLinha[1]))
            

        if boxMenu("<", eventos, resolucao[0] * 0.06, resolucao[1] * 0.962, quebra):
            break

        engine.display.update()



def telaOpcoes():
    log = True

    while(True):
        blitBg()
        eventos = event()

        boxMenu("Skin", eventos, resolucao[0] / 2, posCaixa[13], telaSkin)

        if boxMenu("Logout", eventos, resolucao[0] / 2, posCaixa[15], quebra):
            log = False
            break
        
        if boxMenu("<", eventos, resolucao[0] * 0.06, resolucao[1] * 0.962, quebra):
            break

        engine.display.update()

    if log != True:
        logoutConta()



def telaSkin():
    global corCobra, corBorda
    vals = [corCobra, corBorda]
    rect = rectPlayer[2] * 2, rectPlayer[3] * 2
    pos = rectPlayer[0] * 0.5, rectPlayer[1] * 1.5

    while(True):
        blitBg()
        eventos = event()

        if boxMenu("<", eventos, resolucao[0] * 0.06, resolucao[1] * 0.962, quebra):
            break

        vals[0][0] = slider(resolucao[0] / 2, resolucao[1] / 2, "r", vals[0][0])


        for i in range(0, 15):
            player = engine.draw.rect(tela, vals[0], (pos[0] + rect[0] * i / 3, pos[1], rect[0], rect[1]))
            engine.draw.rect(tela, corBorda, player, 3)
        
        engine.display.update()



def drawCalda(arr, player):
    for i in range(0, calda):

        ## desenhar cada parte da calda
        c = engine.draw.rect(tela, corCobra, arr[len(arr) - delayCalda * (i + 1)])
        engine.draw.rect(tela, corBorda, c, 3)

        ## checar se o player colidiu com a calda
        if player.colliderect(c) and i > 9:
            return True



def render():
    global calda, fim

    ## array que vai ter as posições
    ## passadas do player
    arr = [rectPlayer] * tamInicial

    ## tamanho da calda
    calda = tamInicial

    if fim != True:
        while(True):
            ## pintar a tela de preto
            blitBg()

            ## desenhar player
            player = engine.draw.rect(tela, corCobra, rectPlayer)

            ## colocar a posiçao da cobra 
            ## em um array para usar para
            ## desenhar a calda
            arr.append(player)

            ## deletar elementos da array
            ## para ela nao ficar muito grande
            if len(arr) > calda:
                arr.pop(0)

            ## se uma dessas funçoes retornar true
            ## significa que o player encostou na calda
            ## ou colidiu ocm a parede
            if drawCalda(arr, player) or colisaoParede(player):
                fim = True
                gameover(score)

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


novaComida()
