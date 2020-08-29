

def vsotakvadratov(n):    #vsotakvadratov prvih n stevil
    vsota = 0
    for i in range(1, n + 1):
        vsota += i ** 2
    return vsota

def kvadratvsote(n): #kvadratvsote prvih n stevil
    vsota = 0
    for i in range(1, n + 1):
        vsota += i
    return vsota ** 2

def razlikaprvih(n):
    rezultat = kvadratvsote(n) - vsotakvadratov(n)
    print(rezultat)
    return rezultat



razlikaprvih(100)
