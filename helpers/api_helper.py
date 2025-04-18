from http.client import responses
from symtable import Class

import pytest
import requests
from selene import browser

LOGIN = 'Ivanov_test@test.com'
PASSWORD = 'ivan123456'

base_url = 'https://demowebshop.tricentis.com'
url_add_product = 'https://demowebshop.tricentis.com/addproducttocart/details/'
body_login = {'Email':LOGIN, 'Password':PASSWORD, 'RememberMe': False}


@pytest.fixture()
def log_in():
    response = requests.post(base_url + '/login', data=body_login, allow_redirects=False)
    cookie = response.cookies.get('NOPCOMMERCE.AUTH')

    browser.open(base_url)
    browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": cookie})
    browser.open(base_url)


class ApiAddProductInCart:

    # def add_product_to_cart(self, product, quantity):
    #     response = requests.post(
    #         url=f'{url_add_product}{product}/{quantity}',
    #         data={f'addtocart_{product}.EnteredQuantity:{quantity}'}
    #
    #     )
    #     return response

# https://demowebshop.tricentis.com/addproducttocart/details/45/1


    def add_product_to_cart(self):
        response = requests.post(
            # url='https://demowebshop.tricentis.com/addproducttocart/details/45/1',
            url= 'https://demowebshop.tricentis.com/addproducttocart/catalog/45/1/1',
            data={"addtocart_45.EnteredQuantity": "1"}
        )
        assert response.status_code == 200
        return response



    def add_note(self):
        response = requests.post(base_url + '/addproducttocart/catalog/72/1/1')
        assert response.status_code == 200
        return response