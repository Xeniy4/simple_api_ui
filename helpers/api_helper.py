from http.client import responses

import pytest
import requests
from selene import browser

LOGIN = 'Ivanov_test@test.com'
PASSWORD = 'ivan123456'

base_url = 'https://demowebshop.tricentis.com'

url_add_product = 'https://demowebshop.tricentis.com/addproducttocart/details/'

body_login = {'Email':LOGIN, 'Password':PASSWORD, 'RememberMe': False}


@pytest.fixture(scope="function")
def log_in():
    response = requests.post(base_url + '/login', data=body_login, allow_redirects=False)
    cookie = response.cookies.get('NOPCOMMERCE.AUTH')

    browser.open(base_url)
    browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": cookie})
    browser.open(base_url)


def add_product_to_card(product, quantity):
    response = requests.post(
        url=f'{url_add_product} + {product}/{quantity}',
        data={f'addtocart_{product}.EnteredQuantity: {quantity}'}
    )
    return response


