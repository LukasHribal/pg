class InvalidData(Exception):
    pass


import json

class Osoba:
    def __init__(self, jmeno, telefon, email):
        self.jmeno = jmeno
        self.telefon = telefon
        self.email = email

    @property
    def jmeno(self):
        return self.__jmeno


    @property
    def telefon(self):
        return self.__telefon

    @property
    def email(self):
        return self.__email

    
    @jmeno.setter
    def jmeno(self, hodnota):
        if hodnota.replace(" ", "").isalpha():
            self.__jmeno = hodnota
        else:
            raise InvalidData("jmeno nene")

    @telefon.setter
    def telefon(self, hodnota):
        if hodnota.isnumeric():
            self.__telefon = hodnota
        else:
            raise InvalidData("telefon nene")


    @email.setter
    def email(self, hodnota):
        if "@" not in hodnota:
            raise InvalidData("email nemá @")
        if "." not in hodnota:
            raise InvalidData("email nemá tecku")
        if hodnota.replace("@" , "").replace(".", "").isalnum():
            self.__email = hodnota
        else :
            raise InvalidData ("kek u suck")
    
    def __str__(self):
        return f"Osoba: {self.jmeno}, {self.telefon}, {self.email}"
    
    @classmethod
    def load_json_data(cls, data):
        if "jmeno" not in data or "telefon" not in data or "email" not in data:
            return None
        return cls(data['jmeno'], data['telefon'], data['email'])
    
if __name__ == "__main__":
    #o = Osoba("jan novak", "004225877845", "jan@novak.cz")
    #o.jmeno = "4357253"
    #o.telefon = "asdfjlklh"
    #o.email = "xxx1"

    osoby = []


    with open("data.json",) as fp:
        data = json.loads(fp.read())
        print(data)
        for record in data:
            osoby.append(Osoba.load_json_data(record))
    print(osoby)