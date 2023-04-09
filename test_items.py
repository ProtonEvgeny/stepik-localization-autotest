from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def check_exists_by_css(browser, css):
    try:
        browser.find_element(By.CSS_SELECTOR, css)
    except NoSuchElementException:
        return False
    return True


class TestLocalization:

    def test_availability_cart_button(self, browser):
        browser.get(link)
        actual_cart_button = check_exists_by_css(browser, '.btn-add-to-basket')
        expected_cart_button = True
        assert actual_cart_button == expected_cart_button, \
            f'Expected exists cart button: "{str(expected_cart_button)}", ' \
            f'but actual exists cart button: "{str(actual_cart_button)}"'
