from selene import browser, have

url_card = 'https://demowebshop.tricentis.com/cart'

def check_product_in_card(product):
    browser.open(url_card)
    browser.element('.product-name').should(have.text(product))

