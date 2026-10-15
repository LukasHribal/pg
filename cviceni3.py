def my_range_while(start, stop, step=1):
    #pomocí while udělej funkci range
    vysledek = []
    x = start
    while (x < stop if step < 0 else x < stop):
        vysledek.append(x)
        x += step
    return vysledek

    
def my_enumerate_for(iterable, start=0):
    #implementujte funkci enumerate pomocí cylku for
    vysledek = []
    for x in range(start, len(iterable)):
        vysledek.append((x+start, iterable[x]))
    return vysledek    


def my_enumerate_for2(iterable, start = 0):
    vysledek = []
    for value in iterable:
        vysledek.append((start, value))
        start += 1
    return vysledek

def my_enumerate_while(iterable, start = 0):
    #implemetuj funkci enumerate pomocí while
    vysledek = []
    i = 0
    while i < len(iterable):
        vysledek.append(i+start, iterable[i])
        i += 1
    return vysledek


def my_zip(*iterables):

    iterables = [
         ["alice", "bob", "karel", "eva", "martin"],
         [30,       20,     24,     18,      27   ],
         [50,       80,     90,     55,      67   ]
    ]

    results = [
        ("alice", 30, 50),
        ("bob0", 20, 80),
        ("karel", 24, 90),
        ("eva", 18, 55),
        ("martin", 27, 67),
    ]
    vysledek = []
    lenght = min(len(iterables) for iterable in iterables)
    i = 0
    while i < lenght:
        value = []
        for iterable in iterables:
            value.append(iterable[i])
        vysledek.append(value)
        i += 1
    return vysledek



if __name__ == "__main__":

    #print(list(range(10, 1,-1)))
    #print(my_range_while(10, 1, -1))

    #print(list(enumerate(["aaa", "bbb", "ccc"], 100)))
    #print(my_enumerate_for(["aaa", "bbb", "ccc"], 100))
    #print(my_enumerate_for2(["aaa", "bbb", "ccc"], 100))
    #print(my_enumerate_while(["aaa", "bbb", "ccc"], 100))


    #print(list(zip(
    #    ["alice", "bob", "eva"],
    #    [24, 25, 20],   
    #    ["praha", "ceske budejovice", "pisek"]
    #)))


    jmena = ["alice", "bob", "karel", "eva", "martin"]
    vek =   [30,       20,     24,     18,      27   ]
    vaha =  [50,       80,     90,     55,      67   ]

    vysledek = list( zip(jmena, vek, vaha) )
    print(vysledek)


    vysledek = my_zip(jmena, vek, vaha)
    print(vysledek)