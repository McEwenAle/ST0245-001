
def equilibrio(l):
    suma = 0
    for e in l:
        suma += e

    m = float('inf')
    ind = -1
    suma2 = 0
    for i in range(len(l)):
        suma -= l[i]
        if abs(suma - suma2) < m:
            ind = i
            m = abs(suma - suma2)
        suma2 += l[i]
    return ind
l = [10, 20, 5, 3, 20, 10]
print(equilibrio(l))


