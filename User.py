import sqlite3
from tkinter.colorchooser import *
from tkinter import Tk, simpledialog, colorchooser, messagebox
from datetime import datetime

root = Tk()
root.withdraw()

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
    data DATE NOT NULL,
    idUser INTEGER,
    FOREIGN KEY (idUser) REFERENCES usuario(idUser)
);""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS skin (
    idSkin INTEGER PRIMARY KEY,
    vermelho TEXT NOT NULL,
    verde TEXT NOT NULL,
    azul TEXT NOT NULL,
    idUser INTEGER UNIQUE,
    FOREIGN KEY (idUser) REFERENCES usuario(idUser)
);""")


def cadastro():

    while(True):

        login = simpledialog.askstring(title = "Login", prompt="Informe um login")
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
            INSERT INTO skin 
            VALUES (null, "255", "255", "255", {iduser})
            """)
            conn.commit()

            messagebox.showinfo("Sucesso", f"{login} cadastrado com sucesso")
            break

        elif login == "":
            messagebox.showerror("Erro", "Digite um login")

        elif senha == "":
            messagebox.showerror("Erro", "Digite uma senha")

        else:
            messagebox.showerror("Erro", "Este login ja existe, digite outro")


def login():
    global iduser

    while(True):
        login = simpledialog.askstring(title = "Login", prompt="Digite seu login")
        if login == None:
            return False
        senha = simpledialog.askstring(title = "Senha", prompt="Digite sua senha", show="\u2022")

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
                iduser = resultado[0][0]
                return True

            else:
                messagebox.showerror("Erro", "Senha incorreta, tente novamente")
    
        else:
            messagebox.showerror("Erro", "Este login não existe, digite outro")


def mudarSkin():
    res = colorchooser.askcolor()

    if res[0] != None:
        rgb = []
        for i in range(0, len(res[0])):
            rgb.append(int(res[0][i]))

        cursor.execute(f"""
        UPDATE skin 
        SET vermelho = "{rgb[0]}", verde = "{rgb[1]}", azul = "{rgb[2]}"
        WHERE idUser = {iduser}
        """)
        conn.commit()
    

def getCor():
    cursor.execute(f"""
    SELECT vermelho, verde, azul FROM skin 
    WHERE idUser = {iduser};
    """)

    resultado = cursor.fetchall()

    rgb = []
    for i in range (0, len(resultado[0])):
        rgb.append(int(resultado[0][i]))
    
    return rgb

def uploadScore(score):
    print(score)
    cursor.execute(f"""
    INSERT INTO highscores
    VALUES (null, "{score}", {datetime.now().strftime("%d%m%Y")}, "{iduser}")
    """)
    conn.commit()

    cursor.execute("SELECT * FROM highscores")
    print(cursor.fetchall())

def mostrarScores():
    print("a")