from tabnanny import check
import pytest
from helpers.api_helper import log_in

from helpers.api_helper import ApiAddProductInCart
from helpers.ui_helper import UiCheckProductInCard

api_method_add = ApiAddProductInCart()
ui_check = UiCheckProductInCard()

# def test_add_one_product_in_cart(log_in):
#     api_method_add.add_product_to_cart(45,1)
#     ui_check.check_product_in_cart('Smartphone')
#
#
# def test_add_many_products_in_cart(log_in):
#     api_method_add.add_product_to_cart(43,1)
#     ui_check.check_product_in_cart('Fiction')


def test_shop(log_in):
    api_method_add.add_product_to_cart()
    #ui_check.check_product_in_cart('Fiction')


def test_add_note(log_in):
    api_method_add.add_note()


def test_add_product_in_cart_no_auth():
    pass