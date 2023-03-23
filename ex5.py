def printRecurs(n):
    if n == 0:
        print(n)
    else:
        printRecurs(n - 1)
        print(n)

valor = 4
printRecurs(valor)