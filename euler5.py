



#pomožna funkcija, ki nam bo povedala ali je neko st deljivo z vsemi od 1 do 20

def deljivo1do20(n):
    for i in range(1, 21):
        if n % i != 0:
            return False
    return True


#zacnemo z 20 (lahko tudi z 1) in ponavljamo zanko dokler ne najdemo stevila, ki je deljivo z vsemi od 1 do 20
n = 1
while True:
    if deljivo1do20(n):
        break
    n += 1

print(n)
  
 
