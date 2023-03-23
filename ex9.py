def recursSoma(n):
    if n == 0:
        return 0
    else:
        return 1 / n + recursSoma(n - 1);


resultado = recursSoma(4)
print(resultado)