
def vsota_sodih_fib(n):
    a, b = 1, 2
    vsota = 0
    while b < n:
        if b % 2 == 0:
            vsota += b
        a, b = b, a + b
    return vsota


print(vsota_sodih_fib(4000000))