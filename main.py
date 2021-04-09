from selenium import webdriver
import geckodriver_autoinstaller
from time import sleep
from getpass import getpass


def autoAdd(email,password,num):
    geckodriver_autoinstaller.install()
    driver = webdriver.Firefox()
    driver.get("https://www.facebook.com/")

    driver.find_element_by_name("email").send_keys(email)
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
    for i in range(num):

        driver.find_element_by_css_selector('div.rwwkvi1h:nth-child(1)').click()
        sleep(2)

email = input("Enter your facebook email: ")
password = getpass(prompt='Enter your facebook password: ', stream=None)
print("How many loop do you want to run ? ")
num = int(input(" : "))

print ("your input is successfully\nenjoy with auto add program XD \nprocess ....")

autoAdd(email,password,num*2)

print ("bye bye !!!")