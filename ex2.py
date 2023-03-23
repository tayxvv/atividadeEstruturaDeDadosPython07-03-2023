import math
def expRecurs(n):
    if n == 0:
        return 0
    else:
        return pow(n, 3) + expRecurs(n-1)
    
resultado = expRecurs(2)

print(resultado)