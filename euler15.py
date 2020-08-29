def fakulteta(n):
    return 1 if n == 0 else fakulteta(n-1) * n

def binomski(n, k):
    return fakulteta(n) // (fakulteta(k) * fakulteta(n-k))

def stevilo_poti(st):            #st je tolko kot je stranica kvadrata (blokcov)
    a = 2 * st                   #a = 2 * st, saj je natanko 2 krat toliko potez (st desno in st dol), da pridemo do diagonale
    return binomski(a, st)       #izmed teh je ravno polovica (toje pa st) takih, kjer nardimo isto potezo in nam zato za drugo potezo desno/dol ostane le ena moznost.
                                 #vseh moznosti je zato ravno 40 nad 20, saj uzmed 40 potez izbiramo samo med 20 kdaj in kje jih nardimo ter glede na te premike storimo na en sam način še preostale poteze
print(stevilo_poti(20))
137846528820