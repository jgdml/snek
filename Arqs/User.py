import sqlite3
from os import _exit
from datetime import datetime
import hashlib
from Defaults import root


def criarTabelas():

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuario (
        idUser INTEGER PRIMARY KEY,
        login TEXT NOT NULL,
        senha TEXT NOT NULL
    );""")


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS highscores (
        idHigh INTEGER PRIMARY KEY,
        score INT NOT NULL,
        data DATE NOT NULL,
        idUser INTEGER,
        FOREIGN KEY (idUser) REFERENCES usuario(idUser)
    );""")


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS skin (
        idSkin INTEGER PRIMARY KEY,    
        idUser INTEGER UNIQUE,
        FOREIGN KEY (idUser) REFERENCES usuario(idUser)
    );""")


    cursor.execute("""CREATE TABLE IF NOT EXISTS base(
        idBase INTEGER PRIMARY KEY,
        r TEXT NOT NULL,
        g TEXT NOT NULL,
        b TEXT NOT NULL,
        idSkin INTEGER UNIQUE,
        FOREIGN KEY (idSkin) REFERENCES usuario(idSkin)
    )""")


    cursor.execute("""CREATE TABLE IF NOT EXISTS borda(
        idBase INTEGER PRIMARY KEY,
        r TEXT NOT NULL,
        g TEXT NOT NULL,
        b TEXT NOT NULL,
        idSkin INTEGER UNIQUE,
        FOREIGN KEY (idSkin) REFERENCES usuario(idSkin)
    )""")


    cursor.execute("""CREATE TABLE IF NOT EXISTS sessao(
        id INTEGER NOT NULL
    )""")



def cadastro(login, senha):

    senha = doHash(senha)

    checkLogin = f"""
    SELECT login, idUser FROM usuario
    WHERE login == "{login}";
    """

    cadastrar = f"""
    INSERT INTO usuario 
    VALUES (null, "{login}", "{senha}");
    """

    cursor.execute(checkLogin)
    resultado = cursor.fetchall()

    if resultado == [] and login != "" and senha != "":
        cursor.execute(cadastrar)
        conn.commit()

        cursor.execute(checkLogin)
        res = cursor.fetchall()

        iduser = res[0][1]

        cursor.execute(f"""
        INSERT INTO skin 
        VALUES (null, {iduser})
        """)

        cursor.execute(f"""
        INSERT INTO base 
        VALUES (null, "255", "255", "255", {iduser})
        """)

        cursor.execute(f"""
        INSERT INTO borda 
        VALUES (null, "255", "255", "255", {iduser})
        """)

        conn.commit()
        return f"O login {login} foi cadastrado com sucesso."

    elif login == "":
        return "Digite um login."

    elif senha == "":
        return "Digite uma senha."

    else:
        return "Este login ja existe, digite outro."


def login(login, senha, keep):
    global iduser

    if login == None:
        return False

    if senha == None:
        return False

    selectLogin = f"""
    SELECT idUser, login, senha FROM usuario
    WHERE login == "{login}";
    """

    cursor.execute(selectLogin)
    resultado = cursor.fetchall()

    if resultado != []:

        if senha == resultado[0][2] or doHash(senha) == resultado[0][2]:
            iduser = resultado[0][0]
            if keep:
                logSessao()
            return True

        else:
            return "Senha incorreta, tente novamente"

    else:
        return "Este login não existe, digite outro"


def mudarSkin(base, borda):
    
    cursor.execute(f"""
    UPDATE base
    SET r = "{base[0]}", g = "{base[1]}", b = "{base[2]}"
    WHERE idSkin = {iduser}
    """)
    conn.commit()

    cursor.execute(f"""
    UPDATE borda
    SET r = "{borda[0]}", g = "{borda[1]}", b = "{borda[2]}"
    WHERE idSkin = {iduser}
    """)
    conn.commit()

    return True
    

def getCor(tabela):
    cursor.execute(f"""
    SELECT r, g, b FROM {tabela}
    WHERE idSkin = {iduser};
    """)

    resultado = cursor.fetchall()

    rgb = []
    for i in range (0, len(resultado[0])):
        rgb.append(int(resultado[0][i]))
    
    return rgb


def logSessao():
    cursor.execute(f"""INSERT INTO sessao
    VALUES({iduser})""")

    conn.commit()


def checkSessao():
    cursor.execute("""
    SELECT login, senha FROM usuario 
    INNER JOIN sessao
    ON sessao.id = usuario.idUser
    """)

    res = cursor.fetchall()
    
    if res != []:
        return login(res[0][0], res[0][1], False)

    else:
        return False

def delSessao():
    cursor.execute("""
    DELETE FROM sessao""")
    conn.commit()


def uploadScore(score):

    cursor.execute(f"""
    INSERT INTO highscores
    VALUES (null, "{score}", DATE("now"), "{iduser}")
    """)
    conn.commit()


def mostrarScores(tempo):
    
    cursor.execute(f"""
    SELECT MAX(idUser) FROM usuario
    """)

    topScores = []

    if tempo == 0:
        condicao = f"AND highscores.data BETWEEN DATE('now', '-7 days') AND DATE('now')"

    elif tempo == 1:
        condicao = f"AND highscores.data BETWEEN DATE('now', '-30 days') AND DATE('now')"

    elif tempo == 2:
        condicao = ""



    for i in range(1, cursor.fetchall()[0][0] + 1):

        cursor.execute(f"""
        SELECT usuario.login, MAX(highscores.score), highscores.idUser, highscores.data FROM highscores
        INNER JOIN usuario
        ON usuario.idUser = highscores.idUser
        WHERE highscores.idUser = {i} {condicao}""")

        score = cursor.fetchall()[0]
        

        if score[0] and score[1] and score[3]:
            data = score[3].split("-")
            troca = data[0]
            data[0] = data[2]
            data[2] = troca 
            data = "/".join(data)
            
            if score[2] != iduser:
                score = [score[0], score[1], False, data]
            else:
                score = [score[0], score[1], iduser, data]

            topScores.append(score)
    
    
    for y in range(0, len(topScores)):
        for i in range(0, len(topScores)-1):

            if topScores[i][1] < topScores[i+1][1]:
                troca = topScores[i]
                topScores[i] = topScores[i+1]
                topScores[i+1] = troca

    
    return topScores
    
    
def jogoSair():
    conn.close()
    _exit(0)


def doHash(string):
    h1 = hashlib.sha256()
    h2 = hashlib.md5()
    h3 = hashlib.sha256()

    h1.update(bytes(string, encoding="utf-8"))

    h2.update(bytes(str(h1.digest())+"fazendohash", encoding="utf-8"))

    h3.update(bytes("string3?"+str(h2.digest())+"string2", encoding="utf-8"))


    return str(h3.digest())


conn = sqlite3.connect(root+"banco")
cursor = conn.cursor()
criarTabelas()