# -*- coding: utf-8 -*-
import unittest

# Zaimportowanie niezbednych bibliotek
from selenium import webdriver
import time

# Tworze klase wsbPlCheck dziedziczaca po TestCase z modulu unittest
class WsbPlCheck(unittest.TestCase):
#Instrukcje wykonuje sie przed kazdym testem
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
#Sprzatanie po testach
    def tearDown(self):
        self.driver.quit()
#Metody rozpoczynajace sie od slowa test to nasze testy
    def test_wsb_pl_(self):
        driver = self.driver
        driver.get("http://www.wsb.pl")
#sprawdzam czy Wyzsze Szkoly Bankowe Znajduja sie w tytule strony
        self.assertIn("Wyższe Szkoły Bankowe".decode("utf-8"), driver.title)
        time.sleep(5)


#    def test_pierwszy(self):
#        self.assertEqual(2,2)

#    def test_drugi(self):
#        assert 2==2

#poczatek mojego programu
#wysoluje funkcje main() z modulu unittest,
#która zresztą zrobi za mnie automatycznie
#__main__ to nazwa danego modulu z ktorego odpalamy program
#- sprawdzamy ponizej czy program odpalany jest z tego wlasnie pliku
if __name__ == '__main__':
    unittest.main()
