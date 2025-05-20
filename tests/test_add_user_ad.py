import random
import string

from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from conftest import save_random_email, driver, generate_random_email
from locators import registration_button, non_account_button, registration_password_input, \
    registration_submitPassword_input, user_img, registration_email_input, submit_button, \
    log_out_button, log_in_button, create_ad_button, authorization_alarm_text, \
    authorization_alarm_form, create_ad_name_input, create_ad_description, create_price_input, \
    good_and_city_category_dropdown, \
    category_books, category_city_spb, used_radio_button, post_button, my_ad_card


class TestAddUserAd:

    def test_create_ad_non_authorization_user(self, driver, generate_random_email):
        driver.get("https://qa-desk.stand.praktikum-services.ru/")

        driver.find_element(By.XPATH, create_ad_button).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, authorization_alarm_text)))

        assert len(driver.find_elements(By.XPATH, authorization_alarm_form)) == 1
        assert driver.find_element(By.XPATH,
                                   authorization_alarm_text).text == 'Чтобы разместить объявление, авторизуйтесь'

        driver.quit()

    def test_create_ad_authorization_user(self, driver, save_random_email):
        driver.get("https://qa-desk.stand.praktikum-services.ru/")

        random_price = random.randrange(100, 1000)

        driver.find_element(By.XPATH, registration_button).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, non_account_button)))

        driver.find_element(By.XPATH, non_account_button).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, registration_email_input)))

        driver.find_element(By.XPATH, registration_email_input).send_keys(save_random_email)
        driver.find_element(By.XPATH, registration_password_input).send_keys("1234")
        driver.find_element(By.XPATH, registration_submitPassword_input).send_keys("1234")

        driver.find_element(By.XPATH, submit_button).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, log_out_button)))

        driver.find_element(By.XPATH, log_out_button).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, registration_button)))

        driver.find_element(By.XPATH, registration_button).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, log_in_button)))

        driver.find_element(By.XPATH, registration_email_input).send_keys(save_random_email)
        driver.find_element(By.XPATH, registration_password_input).send_keys("1234")

        driver.find_element(By.XPATH, log_in_button).click()

        try:
            WebDriverWait(driver, 5).until(
                expected_conditions.presence_of_element_located((By.XPATH, create_ad_button)))
            driver.find_element(By.XPATH, create_ad_button).click()
        except StaleElementReferenceException:
            WebDriverWait(driver, 10).until(
                expected_conditions.presence_of_element_located((By.XPATH, create_ad_button)))
            driver.find_element(By.XPATH, create_ad_button).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, create_ad_name_input)))

        driver.find_element(By.XPATH, create_ad_name_input).send_keys(
            ''.join(random.choices(string.ascii_lowercase, k=10)))
        driver.find_element(By.XPATH, create_ad_description).send_keys(
            (''.join(random.choices(string.ascii_lowercase, k=20))))
        driver.find_element(By.XPATH, create_price_input).send_keys(str(random_price))

        category_good_and_city = driver.find_elements(By.XPATH, good_and_city_category_dropdown)
        category_good_and_city[0].click()
        driver.find_element(By.XPATH, category_books).click()

        category_good_and_city[1].click()
        driver.find_element(By.XPATH, category_city_spb).click()

        driver.find_element(By.XPATH, used_radio_button).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, post_button)))

        driver.find_element(By.XPATH, post_button).click()

        try:
            WebDriverWait(driver, 5).until(
                expected_conditions.element_to_be_clickable((By.XPATH, user_img)))
            driver.find_element(By.XPATH, user_img).click()
        except StaleElementReferenceException:
            WebDriverWait(driver, 10).until(
                expected_conditions.element_to_be_clickable((By.XPATH, user_img)))
            driver.find_element(By.XPATH, user_img).click()

        try:
            WebDriverWait(driver, 5).until(
                expected_conditions.visibility_of_element_located((By.XPATH, my_ad_card)))
        except StaleElementReferenceException:
            WebDriverWait(driver, 10).until(
                expected_conditions.visibility_of_element_located((By.XPATH, my_ad_card)))

        assert len(driver.find_elements(By.XPATH, my_ad_card)) == 1

        driver.quit()
