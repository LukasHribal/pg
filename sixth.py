import sys
import requests


def download_url_and_get_all_hrefs(url):
    
    """
    Funkce stahne url predanou v parametru url pomoci volani response = requests.get(),
    zkontroluje navratovy kod response.status_code, ktery musi byt 200,
    pokud ano, najdete ve stazenem obsahu stranky response.content vsechny vyskyty
    <a href="url">odkaz</a> a z nich nactete url, ktere vratite jako seznam pomoci return
    """
    r = requests.get(url)
    if r.status_code != 200:
        return []
    
    else:

        content = r.text
        hrefs = []
        start = 0
        
        while True:
            link = content.find('<a href="', start)
            if link ==-1:
                break

            zacatek_url = link+ len('<a href="')
            konec_url = content.find('"', zacatek_url)


            if zacatek_url == -1 or konec_url==-1:
                break

            href = content[zacatek_url:konec_url]
            hrefs.append(href)

            start = konec_url +1
        return hrefs

if __name__ == "__main__":
    try:
        url = sys.argv[1]
        hrefr = download_url_and_get_all_hrefs(url)
        print (hrefr)
    # osetrete potencialni chyby pomoci vetve except
    except Exception as e:
        print(f"Chyba: {e}")
