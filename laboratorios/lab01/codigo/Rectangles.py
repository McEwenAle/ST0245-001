def formas(n):
    if n == 0:
        return 1
    a = 0
    if n>1:
        a = formas(n-2)

    return  a + formas(n-1)


print(formas(4))