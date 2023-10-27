import time
from app.repository import consult
from app.repository import update
from app.view import home


def updateDataProcess():
    while True:
        print("=======================" * 2, "SISTEMA DE CONTROLE PROCESSUAL", "=======================" * 2, "\n")

        print("Processos existentes: \n")

        print("ID| PROCESSO|   CLIENTE\n")

        consult.dataConsult()

        while True:

            idToSearch = input("\nDigite o ID númerico do processo: \n")

            if idToSearch.isdigit():
                break
            else:
                print("ID númerico inválido!\n")

        while True:
            processToChange = input("Por favor, digite o número do process com 8 dígitos numéricos: \n\n")

            if processToChange.isdigit() and len(processToChange) == 8:
                break
            else:
                print("O número do processo deve conter exatamente 8 dígitos numéricos. Tente novamente.\n")

        while True:
            nameToChange = input("Por favor, digite o nome do cliente: \n")

            if nameToChange.replace(" ","").isalpha():
                break
            else:
                print("O nome do cliente não pode conter números, apenas letras.\n")

        update.dataUpdate(idToSearch, processToChange, nameToChange)

        break

    time.sleep(2)

    home.home()
