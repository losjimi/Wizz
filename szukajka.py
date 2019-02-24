# -*- coding: utf-8 -*-
import unittest

# Zaimportowanie niezbednych bibliotek
from selenium import webdriver
import time

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
        driver.get("https://www.google.pl")
#sprawdzam czy Wyzsze Szkoly Bankowe Znajduja sie w tytule strony
        input = driver.find_element_by_name('q')
        input.send_keys("tester hmmm")
        time.sleep(2)
        input.submit()
        time.sleep(5) #jeżeli damy from time import sleep to tu starczy sleep(5)


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
