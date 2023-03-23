def powpow(x, y):
    if y == 0:
        return 1
    else:
        return x * powpow(x, y - 1)
    
resultado = powpow(3, 3)
print(resultado)