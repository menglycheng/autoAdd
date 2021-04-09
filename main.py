from selenium import webdriver
import geckodriver_autoinstaller
from time import sleep

name = "testbot941@gmail.com"
password = "1234567890-="
geckodriver_autoinstaller.install()
driver = webdriver.Firefox()
driver.get("https://www.facebook.com/")

driver.find_element_by_name("email").send_keys(name)
driver.find_element_by_name("pass").send_keys(password)
button = driver.find_element_by_name("login")
button.click()
sleep(3)

# search = browser.find_element_by_xpath('.//[@type="search"]')
search = driver.find_element_by_css_selector('input[type="search" i]')
search.click()

sleep(3)
p = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/ul/li[1]/div/a')
p.click()

sleep(3)
for i in range(10):
    print(i)
    driver.find_element_by_css_selector('div.rwwkvi1h:nth-child(1)').click()
    sleep(2)