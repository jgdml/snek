import sqlite3
from tkinter.colorchooser import *
from tkinter import Tk, simpledialog, colorchooser

Tk().withdraw()


conn = sqlite3.connect("BD")
cursor = conn.cursor()

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
    data DATE NOT NULL
);""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS skins (
    idSkin INTEGER PRIMARY KEY,
    vermelho TEXT NOT NULL,
    verde TEXT NOT NULL,
    azul TEXT NOT NULL,
    idUser INTEGER UNIQUE,
    FOREIGN KEY (idUser) REFERENCES usuario(idUser)
);""")


def cadastro():
    msg = "Informe um login"

    while(True):

        login = simpledialog.askstring(title = "Login", prompt=msg)
        if login == None:
            return False
        senha = simpledialog.askstring(title = "Senha", prompt="Digite uma senha", show="\u2022")

        if senha == None:
            return False

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
            INSERT INTO skins 
            VALUES (null, "255", "255", "255", {iduser})
            """)
            conn.commit()
            break

        elif login == "" or senha == "":
            msg = "Dados inválidos, digite um login"

        else:
            msg = "Este login ja existe, digite outro"


def login():
    msg = "Digite seu login"
    msgSenha = "Digite sua senha"

    while(True):
        login = simpledialog.askstring(title = "Login", prompt=msg)
        if login == None:
            return False
        senha = simpledialog.askstring(title = "Senha", prompt=msgSenha, show="\u2022")

        if senha == None:
            return False

        selectLogin = f"""
        SELECT idUser, login, senha FROM usuario
        WHERE login == "{login}";
        """

        cursor.execute(selectLogin)
        resultado = cursor.fetchall()

        if resultado != []:

            if senha == resultado[0][2]:
                return resultado[0][2]

            else:
                msgSenha = "Senha incorreta, tente novamente"
    
        else:
            msg = "Este login não existe, digite outro"


def mudarSkin():
    res = colorchooser.askcolor()

    if res[0] != None:
        rgb = []
        for i in range(0, len(res[0])):
            rgb.append(int(res[0][i]))

        cursor.execute(f"""
        UPDATE skins SET vermelho = "{rgb[0]}", verde = "{rgb[1]}", azul = "{rgb[2]}" 
        """)
        conn.commit()
    

def getCor():
    cursor.execute("""
    SELECT vermelho, verde, azul FROM skins 
    INNER JOIN usuario
    ON usuario.idUser = skins.idUser""")

    resultado = cursor.fetchall()
    rgb = []
    for i in range (0, len(resultado[0])):
        rgb.append(int(resultado[0][i]))
    
    return rgb


def mostrarScores():
    print("a")