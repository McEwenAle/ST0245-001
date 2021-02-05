def gcd_euclid(p, q):
    if(p == 0):
        return q
    elif(q == 0):
        return p
    
    if(p>q):
        return gcd_euclid(p %q, q)
    else:
        return gcd_euclid(q %p, p)


print(gcd_euclid(60, 48))