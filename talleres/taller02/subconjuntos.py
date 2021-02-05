def subconjuntos(s):
    return subconjuntosBase("", s)


def subconjuntosBase(base, t):
    if(len(t) == 0):
        return base + " "
     
    a = subconjuntosBase(base + t[0:1], t[1: len(t)])
    b = subconjuntosBase(base, t[1: len(t)])
    return a + b    

print(subconjuntos("Santi"))