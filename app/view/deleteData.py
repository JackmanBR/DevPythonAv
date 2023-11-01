import time
from app.repository import consult
from app.repository import delete
from app.view import home
#TELA DE DELETAR DADOS
def deleteDataProcess():
    while True:
        print("=======================" * 2, "SISTEMA DE CONTROLE PROCESSUAL", "=======================" * 2, "\n")

        print("Processos existentes: \n")

        print("ID| PROCESSO|   CLIENTE\n")

        consult.dataConsult()

        while True:

            idToSearch = input("\nDigite o ID númerico do processo para excluir: \n")

            if idToSearch.isdigit():

                delete.deleteDataProcess(idToSearch)
                time.sleep(1)
                print("Dado apagado, retornando ao menu iniciar!")
                time.sleep(1)
                home.home()
                break

            else:
                print("ID númerico inválido!\n")

