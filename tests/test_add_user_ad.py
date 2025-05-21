import random
import string

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from conftest import save_random_email, driver, generate_random_email
from locators import REGISTRATION_BUTTON, NON_ACCOUNT_BUTTON, REGISTRATION_PASSWORD_INPUT, \
    REGISTRATION_SUBMIT_PASSWORD_INPUT, USER_IMG, REGISTRATION_EMAIL_INPUT, SUBMIT_BUTTON, \
    LOG_OUT_BUTTON, LOG_IN_BUTTON, CREATE_AD_BUTTON, AUTHORIZATION_ALARM_TEXT, \
    AUTHORIZATION_ALARM_FORM, CREATE_AD_NAME_INPUT, CREATE_AD_DESCRIPTION, CREATE_PRICE_INPUT, \
    GOOD_AND_CITY_CATEGORY_DROPDOWN, \
    CATEGORY_BOOKS, CATEGORY_CITY_SPB, USED_RADIO_BUTTON, POST_BUTTON, MY_AD_CARD


class TestAddUserAd:

    def test_create_ad_non_authorization_user(self, driver, generate_random_email):
        driver.get("https://qa-desk.stand.praktikum-services.ru/")

        driver.find_element(By.XPATH, CREATE_AD_BUTTON).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, AUTHORIZATION_ALARM_TEXT)))

        assert len(driver.find_elements(By.XPATH, AUTHORIZATION_ALARM_FORM)) == 1
        assert driver.find_element(By.XPATH,
                                   AUTHORIZATION_ALARM_TEXT).text == 'Чтобы разместить объявление, авторизуйтесь'

    def test_create_ad_authorization_user(self, driver, save_random_email):
        driver.get("https://qa-desk.stand.praktikum-services.ru/")

        random_price = random.randrange(100, 1000)

        driver.find_element(By.XPATH, REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, NON_ACCOUNT_BUTTON)))

        driver.find_element(By.XPATH, NON_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, REGISTRATION_EMAIL_INPUT)))

        driver.find_element(By.XPATH, REGISTRATION_EMAIL_INPUT).send_keys(save_random_email)
        driver.find_element(By.XPATH, REGISTRATION_PASSWORD_INPUT).send_keys("1234")
        driver.find_element(By.XPATH, REGISTRATION_SUBMIT_PASSWORD_INPUT).send_keys("1234")

        driver.find_element(By.XPATH, SUBMIT_BUTTON).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, LOG_OUT_BUTTON)))

        driver.find_element(By.XPATH, LOG_OUT_BUTTON).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, REGISTRATION_BUTTON)))

        driver.find_element(By.XPATH, REGISTRATION_BUTTON).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, LOG_IN_BUTTON)))

        driver.find_element(By.XPATH, REGISTRATION_EMAIL_INPUT).send_keys(save_random_email)
        driver.find_element(By.XPATH, REGISTRATION_PASSWORD_INPUT).send_keys("1234")

        driver.find_element(By.XPATH, LOG_IN_BUTTON).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.presence_of_element_located((By.XPATH, CREATE_AD_BUTTON)))
        driver.find_element(By.XPATH, CREATE_AD_BUTTON).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, CREATE_AD_NAME_INPUT)))

        driver.find_element(By.XPATH, CREATE_AD_NAME_INPUT).send_keys(
            ''.join(random.choices(string.ascii_lowercase, k=10)))
        driver.find_element(By.XPATH, CREATE_AD_DESCRIPTION).send_keys(
            (''.join(random.choices(string.ascii_lowercase, k=20))))
        driver.find_element(By.XPATH, CREATE_PRICE_INPUT).send_keys(str(random_price))

        category_good_and_city = driver.find_elements(By.XPATH, GOOD_AND_CITY_CATEGORY_DROPDOWN)
        category_good_and_city[0].click()
        driver.find_element(By.XPATH, CATEGORY_BOOKS).click()

        category_good_and_city[1].click()
        driver.find_element(By.XPATH, CATEGORY_CITY_SPB).click()

        driver.find_element(By.XPATH, USED_RADIO_BUTTON).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, POST_BUTTON)))

        driver.find_element(By.XPATH, POST_BUTTON).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable((By.XPATH, USER_IMG)))
        driver.find_element(By.XPATH, USER_IMG).click()

        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, MY_AD_CARD)))

        assert len(driver.find_elements(By.XPATH, MY_AD_CARD)) == 1
