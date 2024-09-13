"""
code qui retourne tous les nombres premiers de 0 a 100
"""

from math import sqrt

#### Fonction secondaire


def isprime(p):
    "verifie si le nombre p recu est premier ou pas"
    l = int(sqrt(p))
    if p == 0 :
        return False
    if p == 1 :
        return False
    for i in range (2,l+1):
        if (p%i) == 0 :
            return False
    return True


#### Fonction principale


def main():

    # vos appels à la fonction secondaire ici

    "fonction principale qui va appeler isprime et tester chaque nombre de 0 a 100"

    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
