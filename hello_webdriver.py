# -*- coding: utf-8 -*-
# Zaimportowanie niezbednych bibliotek
from selenium import webdriver
import time
# Stworz nowy sterownik do Chrome
driver = webdriver.Firefox()
# Maksymalizujemy okno
driver.maximize_window()
# Przejdz do strony wsb.pl
driver.get("http://www.wsb.pl")
# Wyswietl tytul strony
print(driver.title)
# Poczekaj 5 sekund, by nacieszyc oczy
# UWAGA!!
time.sleep(5)
# Zamknij przegladarke
driver.quit()
