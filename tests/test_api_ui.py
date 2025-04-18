import os
from http.client import responses

import pytest
import requests
from dotenv import load_dotenv
from selene import browser, have

load_dotenv()
login = os.getenv("LOGIN")
password = os.getenv("PASSWORD")
# данные из .env, которые не пушатся в гит:
# LOGIN = 'Ivanov_test@test.com'
# PASSWORD = 'ivan123456'

base_url = 'https://demowebshop.tricentis.com'
url_card = 'https://demowebshop.tricentis.com/cart'
url_build_your_own_cheap_computer = '/addproducttocart/details/72/1'

endpoint_login = '/login'
body_login = {'Email':login, 'Password':password, 'RememberMe': False}
body_add_product_in_card = {'product_attribute_72_5_18': 53, 'product_attribute_72_6_19': 54,
                           'product_attribute_72_3_20': 57, 'addtocart_72.EnteredQuantity': 1}

@pytest.fixture(scope="function")
def log_in():
    response = requests.post(base_url + endpoint_login, data=body_login, allow_redirects=False)
    cookie = response.cookies.get('NOPCOMMERCE.AUTH')

    browser.open(base_url)
    browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": cookie})
    browser.open(base_url)

    # Это тут не нужно
    # browser.open(base_url)
    # browser.element('.account').should(have.text(login))


def test_add_product_in_card_no_body(log_in):
    response = requests.post(base_url + '/addproducttocart/catalog/72/1/1')
    assert response.status_code == 200

    browser.open(url_card)
    browser.element('.product-name').should(have.text('14.1-inch Laptop'))


def test_add_product_in_card_with_body(log_in):
    response = requests.post(base_url + url_build_your_own_cheap_computer, body_add_product_in_card)
    assert response.status_code == 200
    browser.open(url_card)
    browser.element('.product-name').should(have.text('Build your own cheap computer'))









