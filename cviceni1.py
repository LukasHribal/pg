def add(a, b):
    c = a + b
    return c

def mul(a, b, c):
    výsledek = a * b *c
    return výsledek

def div(a, b):
    if b == 0:
         výsledek = 0
    else:
        výsledek = a / b
    return výsledek


def je_delitelne_beze_zbytku(a, b):
    x = a % b
    if x == 0:
        return "je delitelne beze zbytku"
    else:
        return "neni delitelne beze zbytku"


def je_delitelne_3(a):
    return je_delitelne_beze_zbytku(a, 3)
        


if __name__ == "__main__":
   # x = add(1, 2)
   # x = mul(100, 2, 3)
   # x = div(10,2)
   # výsledek = je_delitelne_beze_zbytku(10,3)
   výsldek = je_delitelne_3(10)
   print(výsledek)
