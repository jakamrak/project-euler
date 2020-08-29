    
def je_prastevilo(n):     #tle preverimo ce je prastevilo na ucinkovit nacin
    if n <= 2:
        return n == 2
    elif n % 2 == 0:
        return False
    else:
        d = 3
        while d ** 2 <= n:
            if n % d == 0:
                return False
            d += 2
        return True



def vsota_prastevil_manjsih_od_n(n):   
    vsota = 0
    for i in range(1, n + 1): #za vsako stevilo do n-tega
        if je_prastevilo(i):  #preverimo ali je to st prastevilo
            vsota += i        # ce je ga pristejemo
    return vsota

print(vsota_prastevil_manjsih_od_n(2000000))