def je_prvocislo(cislo):

    
    cislo = int(cislo)
    if cislo <= 1:
        return False

    
    for x in range(2, int(cislo**0.5) + 1):
        if cislo % x == 0:
            return False

    return True


def vrat_prvocisla(maximum):
    maximum = int(maximum)
    prvocisla = []


    for x in range(2, maximum + 1):
        if je_prvocislo(x):
            prvocisla.append(x)
   
    return prvocisla


if __name__ == "__main__":
    cislo = input("Zadej maximum: ")
    prvocisla = vrat_prvocisla(cislo)
    print(prvocisla)