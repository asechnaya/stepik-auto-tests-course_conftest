import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_order_button_exstence(browser):
    browser.get(link)
    # addbutton = browser.find_element_by_css_selector(".btn-add-to-basket")
    # assert addbutton is True
    # time.sleep(30)