def recurs(n):
    if n == 0:
        return 0
    else:
        return n + recurs(n - 1)
    
resultado = recurs(4)
print(resultado)