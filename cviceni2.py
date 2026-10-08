def vynasob_xty_prvek(seznam, x, nasobek):
    if len(seznam) < x:
        print("není dostatek prvků")
        return(seznam)


    x -= 1
    if x < 0:
        print("index mnesi nez 0")
        return (seznam)

    seznam[x] = seznam[x] * nasobek
    return seznam


def spocitej_prumer(seznam):
   pocet = len(seznam)
   if pocet <= 0:
      print("prazndy seznam")
      return None #pro zaračení funkce
   suma = sum(seznam)

   return suma / pocet 

def formatuj_text(student):
   znamky = student["jmeno"]
   prumer = spocitej_prumer(znamky)
   prumer = round(prumer, 1)
   return f"student {student ["jmeno"]} {student ["primeni"]}, vek: {student ["vek"]}, prumer: {prumer}"
   
    

if __name__ == "__main__":


    student = { 
        "jmeno" : "jan",
        "primeni" : "Novak",
        "vek": 21,
        "znamky": [1, 2, 1, 1 ,3, 2]    
    }
    print(formatuj_text(student)) 
    
    
    
    #seznam = vynasob_xty_prvek([1, 2, 3, 4, 5], 3, 10)
    #print(seznam)

    
    #prumer = spocitej_prumer(seznam)
    #print(prumer)

    #vek = input("zadej svuj vek :")

    #vek = int(vek)
    
    #if vek >= 21:
        #print ("muzes pit v USA")
    #else:
        #print("dej si colu")

    #prin(f"za rok ti bude {vek + 1}")

    #seznam = [1, 2, 3, "ctyri", 5 ]
    #print(seznam)
    #seznam.append("ahoj")
    #print(seznam[2])