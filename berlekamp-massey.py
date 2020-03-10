import random
#Generation  des valeurs aleatoires binaire
def genererListe(L):
        myList = []
        for i in range(0,L):
                x = random.randint(0,1)
                myList.append(x)
        return myList

#Produire aleatoirement un polynome de retroaction binaire
def random_polynomial(L):
        myList = []
        for i in range(0,L):
                x = random.randint(0,1)
                myList.append(x)
        return myList

#Prendre en parametre le coefficient du registre 
def cofficient_LFSR(seq, P, L):
        m=[]
        for i in range (L):
                m.append(seq[i]*P[i])
        return m 
       
#Prendre en parametre le registre qui donne le contenu du registre a l'etat courant, le polynome de retroaction P, la longueur du registre L.     
        
def clock_LFSR(register,P,L):
        m = cofficient_LFSR(register,P,L)
        inValue = sum(m) % 2
        output = register[L-1]
        for i in range (L-1,1,-1):
             register[i] = register[i-1]
             register[0] = inValue
        return inValue


# BerlekampMassey(sequence) applique l'algorithme de Berlekamp-Massey a une sequence binaire sequence. 

def Berlekamp_Massey(sequence):
    n = len(sequence)
    f = [1]
    L = 0
    m = -1
    g = [1]
    for N in range (n):
        # s = sum_{i=1}^{L} (f_{i} * s[N-i])            
        s = sum([f[i] * sequence[N - i] for i in range(1, L + 1)])
        d = (sequence[N] + s) % 2
        if (d == 1):
            t = list(f)
            f = add_polynomial(f, mul_polynomial(g, N - m))
            if (2 * L <= N):
                L = N + 1 - L
                m = N
                g = list(t)
    return f



def mul_polynomial(f, d):
    tmpF = list(f)
    deg_f = len(tmpF) - 1
    if (d == 0):
        return tmpF
    elif (d >= 0):
        for j in range (deg_f + 1, deg_f + 1 + d):
            tmpF.append(0)
        for i in reversed(range(len(tmpF) - d)):
            tmpF[i + d] = tmpF[i]
            tmpF[i] = 0
    else:
        for i in range(len(tmpF) + d):
            tmpF[i] = tmpF[i + d]
            tmpF[i + d] = 0
        tmpF = tmpF[0:deg_f + d + 1]
        
    return tmpF




def add_polynomial(f, g):
    tmpF = list(f)
    tmpG = list(g)
    deg_f = len(f) - 1
    deg_g = len(g) - 1
    deg_res = max(deg_f, deg_g)
    res = [None] * (deg_res + 1)
    # si les fonctions sont de degres differents, on fait les calculs sur des fonctions de tailles similaires.
    if (deg_f < deg_g):
        for i in range (deg_f, deg_g):
            tmpF.append(0)
    elif (deg_g < deg_f):
        for i in range (deg_g, deg_f):
            tmpG.append(0)
    for i in range (len(res)):
        res[i] = (tmpF[i] + tmpG[i]) % 2
        
    return res






L = 5

reg = genererListe(L)
print "seq = ", reg

P = genererListe(L)
print "P   = ", P

print "1 clock : ", clock_LFSR(reg, P, L)

print Berlekamp_Massey([0,0,1,1,0,1,1,1,0])




