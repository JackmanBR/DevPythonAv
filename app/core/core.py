def checkProcessNumber(process):
    processLenght = len(process)

    if process.isdigit() and processLenght == 8 and all(char.isdigit() for char in processLenght):
        print(1)
