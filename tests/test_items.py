from selenium.webdriver.common.by import By
import time


def test_button_add_to_cart_exists(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)
    # Для визуальной проверки добавляем задержку
    time.sleep(3)
    button = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert button.is_displayed(), "Button add to cart is not displayed"