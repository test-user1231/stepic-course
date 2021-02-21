from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/math.html"

try:
    browser = webdriver.Firefox()
    browser.get(link)

    y = browser.find_element_by_css_selector("[id=input_value]").text

    x = math.log(abs(12 * math.sin(int(y))), math.e)

    field = browser.find_element_by_css_selector("[id=answer]")
    field.send_keys(str(x))

    check_box = browser.find_element_by_css_selector("[id=robotCheckbox]")
    check_box.click()

    radio = browser.find_element_by_css_selector("[id=robotsRule]")
    radio.click()

    btn = browser.find_element_by_css_selector("button")
    btn.click()

finally:
    time.sleep(9)
    browser.quit()



