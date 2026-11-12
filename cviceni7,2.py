class MoJeVyjimka(Exception):
    

class BankovniUcet:
    def __init__(self, jmeno, urok):
        self.jmeno = jmeno
        self.urok = urok
        self.__zustatek = 0

    def vloz(self, castka):
        if castka <= 0:
            raise MoJeVyjimka("xxx")
        self.__zustatek += castka

    def vybrat(self, castka):
        if castka <= 0:
            raise MoJeVyjimka("xxx")
        if castka > self.__zustatek:
            raise MoJeVyjimka("xxx")
        self.__zustatek -= castka


    def pricti_uroky(self):
        self.__zustatek += self.__zustatek * self.urok



if __name__ == "__main__":
    ucet = BankovniUcet("sporici", 0.05)
    ucet.vloz(200)
    ucet.vybrat(100)
    ucet.pricti_uroky()
    print(ucet)