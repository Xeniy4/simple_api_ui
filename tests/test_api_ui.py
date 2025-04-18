import os
from http.client import responses

import pytest
import requests
from selene import browser, have





base_url = 'https://demowebshop.tricentis.com'
url_card = 'https://demowebshop.tricentis.com/cart'
url_build_your_own_cheap_computer = '/addproducttocart/details/72/1'

body_add_product_in_card = {'product_attribute_72_5_18': 53, 'product_attribute_72_6_19': 54,
                           'product_attribute_72_3_20': 57, 'addtocart_72.EnteredQuantity': 1}



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








