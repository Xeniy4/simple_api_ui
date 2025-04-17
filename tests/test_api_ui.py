import os
from http.client import responses

import requests
from dotenv import load_dotenv
from selene import browser, have

load_dotenv()
login = os.getenv("LOGIN")
password = os.getenv("PASSWORD")
# данные из .env, которые не пушатся в гит
# LOGIN = 'Ivanov_test@test.com'
# PASSWORD = 'ivan123456'

base_url = 'https://demowebshop.tricentis.com'
endpoint_login = '/login'

body_login = {'Email':login, 'Password':password, 'RememberMe': False}


def test_log_in():
    response = requests.post(base_url + endpoint_login, data=body_login, allow_redirects=False)
    cookie = response.cookies.get('NOPCOMMERCE.AUTH')

    browser.open(base_url)
    browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": cookie})
    browser.open(base_url)

    browser.open(base_url)
    browser.element('.account').should(have.text(login))


