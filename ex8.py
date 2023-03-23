def expRecurs(n):
    if n == 0:
        return n
    else:
        return ((1 + (n * n)) / n) + expRecurs(n - 1);

resultado = expRecurs(4)
print(resultado)
