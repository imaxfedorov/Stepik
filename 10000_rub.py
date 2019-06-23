from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

browser = webdriver.Chrome()
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


browser.get("http://suninjuly.github.io/explicit_wait2.html")

push = browser.find_element_by_css_selector('button#book')

WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, 'price'), '10000 RUR'))



push.click()

rval = browser.find_element_by_css_selector('span#input_value').text
val = int(rval)

res = calc(val)

input = browser.find_element_by_css_selector('input#answer')
input.send_keys(res)

button = WebDriverWait(browser, 2).until(EC.element_to_be_clickable((By.ID, 'solve')))
button.click()

finish = browser.switch_to.alert

result = finish.text.split(': ')[-1]
print(result)