import time
from app.entities import process
from app.repository import insert
from app.repository import consult
from app.view import home

def consultDataProcess():
    while True:
        print("=======================" * 2, "SISTEMA DE CONTROLE PROCESSUAL", "=======================" * 2, "\n")

        print("Iniciando carregamento dos resultados: ")
        i=0
        while i<=3:
            print("."*i)
            time.sleep(1)
            i+=1

        print("ID| PROCESSO|   CLIENTE\n")

        consult.dataConsult()

        print("\n")

        while True:
            optionConsult= input("Aperte 0 para voltarao menu inicial!")

            #option = int(option)
            if optionConsult.isdigit():
                optionConsult = int(optionConsult)

                if( optionConsult != 0):

                    print("Opção inválida, você deve apertar 0 para voltar!\n")

                if  optionConsult == 0:
                    break
            else:
                print("Opção inválida, você deve apertar 0 para voltar!\n")

        time.sleep(2)

        home.home()
