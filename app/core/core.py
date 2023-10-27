from app.view import home
import time
def registerArchivrOfData():
    import datetime
    import os

    currentHour = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    archivePath = os.path.join("C:\\projetos\\python\\arquivos teste", "registro.txt")

    conteudoFinal = "Obrigado."

    with open(archivePath, 'w') as arquivo:
        arquivo.write(
            "Olá usuário, \n\nSeu uso do sistema foi salvo no arquivo de registro nomeado como -registro.txt-, datado em:\n\n" + currentHour + "\n\nObrigado pelo uso deste sistema!\nPaulo Guerra.\n"+conteudoFinal)

    print(f'Registro de uso salvo em: {archivePath}\n')

    time.sleep(2)

    home.home()
