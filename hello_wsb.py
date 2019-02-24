# -*- coding: utf-8 -*-
import unittest

# Zaimportowanie niezbednych bibliotek
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

# Tworze klase wsbPlCheck dziedziczaca po TestCase z modulu unittest
class GooCheck(unittest.TestCase):
#Instrukcje wykonuje sie przed kazdym testem
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
#Sprzatanie po testach
    def tearDown(self):
        self.driver.quit() #quit zamyka wszystkie strony, a close tylko jedna
#Metody rozpoczynajace sie od slowa test to nasze testy
    def test_wsb_pl_(self):
        driver = self.driver
        driver.get("http://www.wsb.pl")
#sprawdzam czy Wyzsze Szkoly Bankowe Znajduja sie w tytule strony

    def test_link_(self):
        driver = self.driver
        driver.get("http://www.wsb.pl")
#sprawdzam czy Wyzsze Szkoly Bankowe Znajduja sie w tytule strony
        driver.find_element_by_link_text('Czym jest sukces?').click()
        time.sleep(3) #jeżeli damy from time import sleep to tu starczy sleep(5)

    def test_partial_link_(self):
        driver = self.driver
        driver.get("http://www.wsb.pl")
#sprawdzam czy Wyzsze Szkoly Bankowe Znajduja sie w tytule strony
        driver.find_element_by_partial_link_text('Czym jest').click()#partial wyszukuje czesci tresci
        time.sleep(3) #jeżeli damy from time import sleep to tu starczy sleep(5)
#zakomentowanie bloku lCtrl+?
#2.3
    def test_select_(self):
        driver = self.driver
        driver.get("http://www.wsb.pl")
        select_univercity = Select(driver.find_element_by_id("edit-city"))#obiekt instancji select
#pusta lista ma dostępne opcje
        act_option = []
        for option in select_univercity.options:
            print option.get_attribute("text")
#sprawdz czy wybrana jest 11 opcja
        self.assertEqual(11, len(select_univercity.options))

#porownanie miast czy sa takie jak chcemy
    def test_cities_(self):
        driver = self.driver
        driver.get("http://www.wsb.pl")
        select_univercity = Select(driver.find_element_by_id("edit-city"))#obiekt instancji select
        act_option = []
        exp_option = [u'Wybierz miasto',u'Bydgoszcz',u'Chorzów/Katowice',u'Gdańsk',u'Gdynia',u'Opole',u'Poznań',u'Szczecin',u'Toruń',u'Warszawa',u'Wrocław']#u jako unicode
        for option in select_univercity.options:
            act_option.append(option.get_attribute("text"))
        self.assertEqual(exp_option, act_option)

#    def test_pierwszy(self):
#        self.assertEqual(2,2)

#    def test_drugi(self):
#        assert 2==2

#poczatek mojego programu
#wysoluje funkcje main() z modulu unittest,
#która zresztą zrobi za mnie automatycznie
#__main__ to nazwa danego modulu z ktorego odpalamy program
#- sprawdzamy ponizej czy program odpalany jest z tego wlasnie pliku
#mozemy zamiast ponizszego ifa wpisac w interpreterze pythona python -m unittest i nazwa skryptu
if __name__ == '__main__':
    unittest.main(verbosity=2)
