def naslednji_clen(n):
    if n % 2 == 0:
        return n / 2 
    else:
        return n * 3 + 1

def dolzina_zaporedja(n):
    dolzina = 0
    while n != 1:
        dolzina += 1
        n = naslednji_clen(n)
    return dolzina + 1

def st_z_najdaljso_dolzin(n):

    dolzina = 0
    indeks = 0
    for i in range(n):
        if dolzina_zaporedja(i) > dolzina:
            dolzina = dolzina_zaporedja(i)
            indeks = i
        return indeks

print(st_z_najdaljso_dolzin(1000000))
837799