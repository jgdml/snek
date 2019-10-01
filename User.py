import sqlite3
from tkinter.colorchooser import *
from tkinter import Tk, simpledialog

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
    azul TEXT NOT NULL
);""")


def cadastro():
    while(True):

        login = simpledialog.askstring(title = "", prompt="Informe um login")
        senha = simpledialog.askstring(title = "", prompt="Informe uma senha", show="*")

        checkLogin = f"""
        SELECT login FROM usuario
        WHERE login == "{login}";
        """

        cadastrar = f"""
        INSERT INTO usuario 
        VALUES (null, "{login}", "{senha}");
        """

        cursor.execute(checkLogin)
        resultado = cursor.fetchall()

        if resultado == []:
            print("===Cadastrado com sucesso")
            cursor.execute(cadastrar)
            conn.commit()
            break

        else:
            print("===Este login já existe")


def login():
    while(True):
        login = input("Login: ")
        senha = input("Senha: ")
        print()

        selectLogin = f"""
        SELECT nome, senha, login FROM usuario
        WHERE login == "{login}";
        """

        cursor.execute(selectLogin)
        resultado = cursor.fetchall()

        if resultado != []:

            if senha == resultado[0][1]:

                print("===Bem vindo", resultado[0][0])
                loginOpcoes(resultado[0][0], resultado[0][2], resultado[0][1])
                break

            else:
                print("===Senha incorreta")

        else:
            print("===Este login não existe")


def loginOpcoes(nome, login, senha):
    print(nome, senha, login)
    while(True):
        print("\nMenu\n\n1 - Alterar Nome\n2 - Deletar conta\n3 - Deslogar\n")

        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            nomeNovo = input("Digite seu novo nome: ")
            script = f"""
            UPDATE usuario SET nome = '{nomeNovo}'
            WHERE login = '{login}';
            """
            cursor.execute(script)
            print("Nome alterado para ", nomeNovo)

        elif opcao == 2:

            confirmacao = input(
                "Tem certeza que deseja excluir sua conta?\nDigite sua senha para continuar: ")
            script = f"""
            DELETE FROM usuario
            WHERE login = '{login}'
            """

            if confirmacao == senha:
                cursor.execute(script)
                conn.commit()
                print("\n===Conta Excluída")
                break
            else:
                print("\n===Senha incorreta")

        elif opcao == 3:
            break

        else:
            print("Opção inválida")



def fechar():
    conn.close()
