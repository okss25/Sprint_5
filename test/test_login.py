from Sprint_5 import data, locators

from web_locators.locators import *


class TestLoginTheSite:
    def test_login_to_account_with_button_in_the_main_page(self, driver):
        # переход в "войти в аккаунт"
        driver.find_element(*locators.TestLocators.LOGIN_TO_ACCOUNT_BUTTON).click()
        # вход зарегистрированным пользователем
        driver.find_element(*locators.TestLocators.LOGIN_MAIL_FIELD).send_keys(data.user[1])
        driver.find_element(*locators.TestLocators.LOGIN_PASSWORD_FIELD).send_keys(data.user[2])
        driver.find_element(*locators.TestLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 3).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/"))

        assert driver.current_url == "https://stellarburgers.nomoreparties.site/", (
                "Ожидался URL https://stellarburgers.nomoreparties.site/, но получен {}".format(
                    driver.current_url))


    def test_login_through_personal_account_button(self, driver):
        # нажатие В ЛК
        driver.find_element(*locators.TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
        # вход зарегистрированным пользователем
        driver.find_element(*locators.TestLocators.LOGIN_MAIL_FIELD).send_keys(data.user[1])
        driver.find_element(*locators.TestLocators.LOGIN_PASSWORD_FIELD).send_keys(data.user[2])
        driver.find_element(*locators.TestLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 3).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/"))

        assert driver.current_url == "https://stellarburgers.nomoreparties.site/", (
                "Ожидался URL https://stellarburgers.nomoreparties.site/, но получен {}".format(
                    driver.current_url))


    def test_registration_with_test_login(self, driver):
        # переход в "войти в аккаунт"
        driver.find_element(*locators.TestLocators.LOGIN_TO_ACCOUNT_BUTTON).click()
        # нажатие на кнопку зарегистрироваться
        driver.find_element(*locators.TestLocators.REGISTRATION_BUTTON).click()
        # переход в "войти в аккаунт"
        driver.find_element(*locators.TestLocators.LOGIN_BUTTON_ON_REGISTRATION_PAGE).click()
        # вход зарегистрированным пользователем
        driver.find_element(*locators.TestLocators.LOGIN_MAIL_FIELD).send_keys(data.user[1])
        driver.find_element(*locators.TestLocators.LOGIN_PASSWORD_FIELD).send_keys(data.user[2])
        driver.find_element(*locators.TestLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 3).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/"))

        assert driver.current_url == "https://stellarburgers.nomoreparties.site/", (
            "Ожидался URL https://stellarburgers.nomoreparties.site/, но получен {}".format(
                driver.current_url))

    def test_login_from_recovery_form(self, driver):
        # переход в "войти в аккаунт"
        driver.find_element(*locators.TestLocators.LOGIN_TO_ACCOUNT_BUTTON).click()
        # нажатие на кнопку восстановить пароль
        driver.find_element(*locators.TestLocators.PASSWORD_RECOVERY_BUTTON).click()
        # нажатие на кнопку "войти в аккаунт" со страницы восстановления пароля
        driver.find_element(*locators.TestLocators.LOGIN_BUTTON_ON_PASSWORD_RECOVERY_PAGE).click()
        # вход зарегистрированным пользователем
        driver.find_element(*locators.TestLocators.LOGIN_MAIL_FIELD).send_keys(data.user[1])
        driver.find_element(*locators.TestLocators.LOGIN_PASSWORD_FIELD).send_keys(data.user[2])
        driver.find_element(*locators.TestLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 3).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/"))

        assert driver.current_url == "https://stellarburgers.nomoreparties.site/", (
            "Ожидался URL https://stellarburgers.nomoreparties.site/, но получен {}".format(
                driver.current_url))