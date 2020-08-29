def vsota(n):
    vsota = 0
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
            vsota += i
    return vsota

vsota(1000)