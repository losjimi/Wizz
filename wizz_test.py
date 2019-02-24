# -*- coding: utf-8 -*-
#Scenariusz:
#Rejestracja nowego usera na stronie wizzair
#
# Przypadki testowe:
#
# Rejestracja pierwszego użytkownika na fakowych danych
#
# Kroki:
# 1. Wejść na stronę www.wizzair.com
# 2. Klikamy Zaloguj się
# 3. Klikamy Rejestracja
# 4. Wprowadź Imię
# 5. Wprowadź Nazwisko
# 6. Wybierz Płeć
# 7. Podaj Nr telefonu
# 8. Podaj Błędny email (bez @)
# 9. Wprowadź Hasło
# 10. Wybierz kraj Polska
# 11. Zaakceptuj Politykę prv
# 12. Zaakceptuj Sybskrypcję
# 13. Kliknij zarejestruj
#
# Oczekiwany rezultat:
# User otrzymuje informację, że podany email jest nieprawidłowy

import unittest
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
import test_data

class WizzCheck(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.wizzair.com/pl-pl#/")
#dać time sleep aby www zdazy sie zaladowac  time.sleep(2)
        self.driver.implicitly_wait(20)
    def tearDown(self):
        self.driver.quit()
    def test_register_wrong_email_(self):
        driver = self.driver
# """
#         zaloguj_btns = driver.find_elements_by_class_name('navigation__button')
#         zaloguj_btns[28].click() #najgorsze praktyki
#  2 najgorsze praktyki dostanie się poprzez XPATH
#  3 najgorsze praktyki dostanie się poprzez CSS sleector
#
# """
        # zaloguj_btn = self.driver.find_element_by_class_name('navigation__button navigation__button--simple')
        # zaloguj_btn.click()
#        zaloguj_btn = driver.find_element_by_css_selector("#app > header > div.header__inner > div > nav > ul > li:nth-child(7) > button")
#        zaloguj_btn.click()
        zaloguj_btn = self.driver.find_element_by_xpath("//button[@data-test='navigation-menu-signin']")
        zaloguj_btn.click()

#aby napisać własnego xPath wpisujemy w kodzie strony //<tag>[@]<nazwa zmiennej i wartość> np //button[@data-test='navigation-menu-signin']
        register = driver.find_element_by_xpath('//*[@id="login-modal"]/form/div/p/button')#wlasny xpath //button[text()='Rejestracja']
        register.click()
        name = driver.find_element_by_name('firstName')
        name.send_keys(test_data.valid_name)
        surname = driver.find_element_by_xpath('//input[@data-test="registrationmodal-last-name-input"]')
        surname.send_keys(test_data.valid_surname)
        if test_data.sex == 'male':
            male = driver.find_element_by_xpath('//label[@for="register-gender-male"]')
            driver.execute_script("arguments[0].click()", male)
        else:
            male = driver.find_element_by_xpath('//label[@for="register-gender-female"]')
            driver.execute_script("arguments[0].click()", male)
#webdriver posiada metode wywolujaca skrypt JS driver.execute.script("argument[0].click", find element ...)
        #male.click() - other element receive the click - jakiś element zakrywa kliknięcie
        phone = driver.find_element_by_name('mobilePhone')
        phone.send_keys(test_data.valid_phone)
        passy = driver.find_element_by_xpath('//input[@type="password"][@data-test="booking-register-password"]')
        passy.send_keys(test_data.valid_pass)
        # national = driver.find_element_by_xpath('//input[@data-test="booking-register-country"]')
        # #national.send_keys(test_data.valid_nationality)
        # national.click()
        # #możemy wybrać z listy //div[@class="register-form__country-container__locations"]/label[164]
        # national_choose = driver.find_element_by_xpath('//div[@class="register-form__country-container__locations"]/label[164]')
        # national_choose.location_once_scrolled_into_view #scroluje
        # national_choose.click()
        # wyszukiwanie nazwy kraju po zmiennej w test_data
        national = driver.find_element_by_xpath('//input[@data-test="booking-register-country"]')
        national.click()
        national_choose = driver.find_element_by_xpath('//div[@class="register-form__country-container__locations"]')
        countries = national_choose.find_elements_by_xpath('label')
        for label in countries:
            d=label.find_element_by_tag_name('strong')
            #print(d.text)
            if d.get_attribute("innerText")==test_data.valid_nationality:
                #print(national_choose)
                d.location_once_scrolled_into_view #scroluje
                d.click()
                break

        newsletter = driver.find_element_by_xpath('//label[@for="registration-special-offers-checkbox"][@class="rf-checkbox__label"]')
        newsletter.click()
        pol_prv = driver.find_element_by_xpath('//label[@for="registration-privacy-policy-checkbox"][@class="rf-checkbox__label"]')
        pol_prv.click()
        mail = driver.find_element_by_xpath('//input[@type="email"][@data-test="booking-register-email"]')
        mail.send_keys(test_data.invalid_email)
        rejestracja = driver.find_element_by_xpath('//button[@data-test="booking-register-submit"]')
        rejestracja.click()
        error_notice = driver.find_element_by_xpath("(//span[contains(text(), 'Nieprawidłowy adres e-mail')])[2]")
        #prawidłowy rezultat jest tutaj - sprawdzamy czy jest nieprawidłowy adres email i czy to jest widoczne is displayed
        assert error_notice.is_displayed()
        self.assertEqual(error_notice.text, u'Nieprawidłowy adres e-mail')
        #self.assertIn("Nieprawidłowy adres e-mail".decode("utf-8"), driver.find_element_by_name())
        driver.save_screenshot('hh.png')
        time.sleep(10)


#różnica miedzy xpath a css selector to //input[@data-test="booking-register-country"] a input[data-test="booking-register-country"]

#       imie = driver.find_element_by_name('firstName')
#       imie.send_keys("Jim")


        # select_city = Select(driver.find_element_by_id("..."))
        # act_option = []
        # for option in select_univercity.options:
        #     print option.get_attribute("text")
        # self.assertEqual(11, len(select_univercity.options))


    # def test_cities_(self):
    #     driver = self.driver
    #     driver.get("http://www.wsb.pl")
    #     select_univercity = Select(driver.find_element_by_id("edit-city"))#obiekt instancji select
    #     act_option = []
    #     exp_option = [u'Wybierz miasto',u'Bydgoszcz',u'Chorzów/Katowice',u'Gdańsk',u'Gdynia',u'Opole',u'Poznań',u'Szczecin',u'Toruń',u'Warszawa',u'Wrocław']#u jako unicode
    #     for option in select_univercity.options:
    #         act_option.append(option.get_attribute("text"))
    #     self.assertEqual(exp_option, act_option)
if __name__ == '__main__':
    unittest.main(verbosity=2)
