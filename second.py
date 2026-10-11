def cislo_text(cislo):
    cislo = int(cislo)
    cisla1 = {
                 0: "nula", 1: "jeden", 2: "dva", 3: "tři", 4: "čtyři", 5: "pět", 6: "šest", 7: "sedm", 8: "osm", 9: "devět", 10: "deset",
                 11: "jedenáct", 12: "dvanáct", 13: "třináct", 14: "čtrnáct", 15: "patnáct", 16: "šestnáct", 17: "sedmnáct", 18: "osmnáct", 19: "devatenáct" 
                 }
    cisla10 = {
        2: "dvacet", 3: "třicet", 4: "čtyřicet", 5: "padesát",
        6: "šedesát", 7: "sedmdesát", 8: "osmdesát", 9: "devadesát"
        }

    if cislo in cisla1 :
        return (cisla1[cislo])

    if (cislo == 100) :
        return "sto"

    if (cislo > 100) :
        return "mimo rozsah"

    desitka = cislo // 10
    jednotka = cislo % 10

    if jednotka == 0 :
        return (cisla10[desitka])
    else :
        return (f"{cisla10[desitka]} {cisla1[jednotka]}")

if __name__ == "__main__":
    cislo = input("Zadej číslo: ")
    text = cislo_text(cislo)
    print(text)