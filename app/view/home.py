import time
from app.view import insertData
from app.view import consultData
from app.view import updateData
from app.view import deleteData
from app.core import core
from app.view import home
def home():
    while True:
        print("======================="*2, "SISTEMA DE CONTROLE PROCESSUAL","======================="*2, "\n")
        print("1.Cadastrar processo.\n2.Consultar processo.\n3.Atualizar processo\n4.Deletar processo.\n5.Salvar registro em disco.\n6.Sair\n")
        option = input("Bem vindo, por favor, digite a opcao desejada: \n\n")

        if option.isdigit():
            option = int(option)
            if option >= 1 and option <= 6:
                if option == 1:
                    insertData.insertDataProcess()
                if option == 2:
                    consultData.consultDataProcess()
                if option == 3:
                    updateData.updateDataProcess()
                if option == 4:
                    deleteData.deleteDataProcess()
                if option == 5:
                    core.registerArchivrOfData()
                    time.sleep(1)
                if option == 6:
                    exit()
            else:
                print("Entrada inválida. Por favor, digite um número entre 1 e 6.\n")
                time.sleep(1)
        else:
            print("Entrada inválida. Por favor, digite um número entre 1 e 5.\n")
            time.sleep(1)