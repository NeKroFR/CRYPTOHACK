def egcd(p,q):
    if p == 0:
        return (q, 0, 1)
    
    gcd, u, v = egcd(q % p, p)
    return (gcd, v - (q // p) * u, u)

p = 26513
q = 32321

gcd, u, v = egcd(p, q)
print("gcd:",gcd,"\nu:", u,"\nv:", v)