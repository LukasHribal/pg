from sixth import download_url_and_get_all_hrefs
from unittest.mock import MagicMock
import requests


def test_download_url_and_get_all_hrefs():
    data = '<html><body><a id="1" href="https://www.jcu.cz">odkaz</a><div><a href="http://ef.jcu.cz/kontakty">kontakty</a></div></body></html>'

    response = MagicMock()
    response.status_code = 200
    response.text = data

    requests.get = MagicMock(return_value=response)
    
    requests.get = MagicMock(return_value = ("data", "test"))

    href = download_url_and_get_all_hrefs(data)


    assert href == ['https://www.jcu.cz', 'http://ef.jcu.cz/kontakty']




#def prevod_c_na_f(stupne):
#    return (stupne * 9/5) + 32


#def test_prevod_c_na_f():
#    assert prevod_c_na_f(100) == 212
#    assert prevod_c_na_f(0) == 32


#def nejvetsi(seznam_cisel):
#    if not seznam_cisel:
#        return None
#    return max(seznam_cisel)


#def test_nejvetsi():
#    assert nejvetsi([1,2,3,4,5]) == 5
#    assert nejvetsi([100, 50, 30, 10]) == 100
#    assert nejvetsi([]) == None



