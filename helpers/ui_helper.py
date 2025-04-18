from selene import browser, have

url_cart = 'https://demowebshop.tricentis.com/cart'



class UiCheckProductInCard:
    def check_product_in_cart(self, product):
        browser.open(url_cart)
        browser.element('.product-name').should(have.text(product))

