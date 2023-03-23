def soma(x, y):
    if y == 0:
        return 0
    else:
        return x + soma(x, y - 1)
    
resultado = soma(2, 3)
print(resultado)