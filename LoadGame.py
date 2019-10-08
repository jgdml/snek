from os import _exit
from random import randint
from time import sleep
from User import login, getCor, cadastro, mudarSkin, uploadScore, mostrarScores, logSessao, delSessao, jogoSair
from Components.BoxMenu import boxMenu
from Components.Slider import slider
from Components.TextInput import textInput
from Arqs.Defaults import *
from Arqs.Funcs import *



def resetJogar():
    global reset
    reset = True
    fim = False
    return True


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


def inicio():

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
    global corCobra, corBorda    
    corCobra = getCor("base")
    corBorda = getCor("borda")

    while(True):
        tela.fill(bg)
        evento = event()

        if boxMenu("Jogar", evento, resolucao[0] / 2, posCaixa[11], resetJogar):
            break

        boxMenu("Opções", evento, resolucao[0] / 2, posCaixa[13], opcoes)

        boxMenu("Sair", evento, resolucao[0] / 2, posCaixa[16], jogoSair)

        engine.display.update()
        
    
    
    
def opcoes():
    log = True

    while(True):
        tela.fill(bg)
        eventos = event()

        boxMenu("Highscores", eventos, resolucao[0] / 2, posCaixa[11], telaScores)

        boxMenu("Skin", eventos, resolucao[0] / 2, posCaixa[13], mudarCores)

        if boxMenu("Logout", eventos, resolucao[0] / 2, posCaixa[15], quebra):
            log = False
            break
        
        if boxMenu("<", eventos, resolucao[0] * 0.06, resolucao[1] * 0.962, quebra):
            break

        engine.display.update()

    if log != True:
        logoutConta()




def telaScores():

    topScores = mostrarScores()



    while(True):
        tela.fill(bg)
        eventos = event()


        if boxMenu("<", eventos, resolucao[0] * 0.06, resolucao[1] * 0.962, quebra):
            break
        engine.display.update()


def mudarCores():
    global corCobra, corBorda
    vals = [corCobra, corBorda]
    

    while(True):
        tela.fill(bg)
        eventos = event()

        

        if boxMenu("<", eventos, resolucao[0] * 0.06, resolucao[1] * 0.962, quebra):
            break

        slider(resolucao[0] / 2, resolucao[1] / 2, "r", vals[0][0])

        engine.display.update()

def logoutConta():
    delSessao()
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


def gameover(score):
    global upload
    posScore = (resolucao[0] / 2) - score.get_size()[0] / 2, 0
    upload = True
    ## tela de gameover
    player = engine.draw.rect(tela, corCobra, rectPlayer)
    comida = engine.draw.rect(tela, vermelho, posComida)
    engine.draw.rect(tela, vermelho, comida, 3)
    tela.blit(score, posScore)
    tela.blit(restart, posRestart)
    tela.blit(sair, posSair)
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
            tela.fill(bg)

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
