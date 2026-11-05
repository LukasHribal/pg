import requests
import json
import sys

url = "https://www.jcu.cz/cz"
url1 = 'https://data.carnewschina.com/suggest?q='
url2 = 'http://www.cnb.cz/cs/financni_trhy/devizovy_trh/kurzy_devizoveho_trhu/denni_kurz.txt'


def get_model_names(prefix):
    url = url1 + prefix
    print(url)
    r = requests.get(url)
    if r.status_code != 200:
        print(f"stahovaní skončilo chybou: {r.status_code}")
        return []
    data = json.loads(r.content)
    model_names = []
    for model in data["models"]:
        model_names.append(model["name"])
    return model_names


def download_rates():
   
   r = requests.get(url2)
   if r.status_code != 200:
        return ()
   data= r.text
   lines = data.splitlines()[2:]
   vysledek = {}
   for line in lines:
       hodnoty = line.split("!")
       print (hodnoty)
       vysledek[hodnoty[3]]) hodnoty[4].replace(",", ".")  #nah its just fucked kek
   return vysledek
    
       










if __name__ =="__main__":
    #sponce = requests.get(url1)
    #f responce.status_code == 200:
    #   print(responce.json)




 #  if len(sys.argv) < 2:
 #      print(f"Usage: {sys.argv[0]} prefix")
 #       sys.exit()
#
 #      prefix = sys.argv[1]
  #     models = get_model_names(prefix)
  #     for model in models:
  #         print(model)