import time
from app.view import insertData
from app.view import consultData
def home():
    while True:
        print("======================="*2, "SISTEMA DE CONTROLE PROCESSUAL","======================="*2, "\n")
        print("1.Cadastrar processo.\n2.Consultar processo.\n3.Atualizar processo\n4.Deletar processo.\n5.Sair\n")
        option = input("Bem vindo, por favor, digite a opcao desejada: \n\n")

        if option.isdigit():
            option = int(option)
            if option >= 1 and option <= 5:
                if option == 1:
                    insertData.insertDataProcess()
                if option == 2:
                    consultData.consultDataProcess()
                if option == 3:
                    break
                if option == 4:
                    break
                if option == 5:
                    exit()
            else:
                print("Entrada inválida. Por favor, digite um número entre 1 e 5.\n")
                time.sleep(1)
        else:
            print("Entrada inválida. Por favor, digite um número entre 1 e 5.\n")
            time.sleep(1)