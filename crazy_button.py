from selenium import webdriver
from time import sleep
import math
link = "http://suninjuly.github.io/redirect_accept.html"

browser = webdriver.Chrome()
browser.get(link)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

troll = browser.find_element_by_css_selector('button.trollface')
sleep(0.5)
troll.click()

new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

rval = browser.find_element_by_css_selector('span#input_value').text
val = int(rval)

res = calc(val)

input = browser.find_element_by_css_selector('input#answer')
input.send_keys(res)

browser.find_element_by_css_selector('button.btn-primary').click()

finish = browser.switch_to.alert

result = finish.text.split(': ')[-1]
print(result)


