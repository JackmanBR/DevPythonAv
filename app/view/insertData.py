import time
from app.entities import process
from app.repository import insert
from app.view import home

processOne = process


def insertDataProcess():
    while True:
        print("=======================" * 2, "SISTEMA DE CONTROLE PROCESSUAL", "=======================" * 2, "\n")

        while True:
            processToInsert = input("Por favor, digite o número do process com 8 dígitos numéricos: \n\n")

            if processToInsert.isdigit() and len(processToInsert) == 8:
                break
            else:
                print("O número do processo deve conter exatamente 8 dígitos numéricos. Tente novamente.\n")

        while True:
            client = input("Por favor, digite o nome do cliente: \n")

            if client.replace(" ","").isalpha():
                break
            else:
                print("O nome do cliente não pode conter números, apenas letras.\n")

        insert.dataInsert(processToInsert, client)

        print("Dados inseridos com sucesso!\n")

        time.sleep(2)

        home.home()
