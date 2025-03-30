from Sprint_5 import locators


class TestMovingToPersonalAccount:
    def test_click_on_personal_account(self, driver):
        # вход на сайт
        driver.find_element(*locators.TestLocators.PERSONAL_ACCOUNT_BUTTON).click()

        # введение учётных данных
        driver.find_element(*locators.TestLocators.LOGIN_MAIL_FIELD).send_keys(data.user[1])
        driver.find_element(*locators.TestLocators.LOGIN_PASSWORD_FIELD).send_keys(data.user[2])
        driver.find_element(*locators.TestLocators.LOGIN_BUTTON).click()

        # ожидание перехода на главную страницу
        WebDriverWait(driver, 3).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/"))

        # переход в ЛК
        driver.find_element(*locators.TestLocators.PERSONAL_ACCOUNT_BUTTON).click()

        # ожидание перехода в ЛК
        WebDriverWait(driver, 3).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/account/profile"))

        assert driver.current_url == "https://stellarburgers.nomoreparties.site/account/profile", (
                "Ожидался URL https://stellarburgers.nomoreparties.site/account/profile, но получен {}".format(
                    driver.current_url))