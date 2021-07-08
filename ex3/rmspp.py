import random

def mode(number, attempts):
    
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    s = number - 1
    r = 0
    while s % 2 == 0:
        r += 1
        s //= 2
    while attempts:
        a = random.randint(1, number - 1)
        if modExponent(a, s, number) != 1:
            for j in range(0,r):
                if modExponent(a,(2**j)*s,number) == number - 1:
                    break
        else:
            return False
            attempts -= 1
            continue
    return True