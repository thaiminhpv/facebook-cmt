from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from main.stringDatabase import *

import time
import json

with open("configMachine.json", encoding="utf-8") as json_file:
    data = json.load(json_file)
    email, password, linkToStrike, message, delay = [data[k] for k in
                                                     ('email', 'password', 'linkToStrike', 'message', 'delay')]
    if message is None:
        message = ":) " * 1000

option = Options()
option.add_argument("--disable-infobars")
option.add_argument("start-maximized")

option.add_argument("--disable-extensions")
# Pass the argument 1 to allow and 2 to block

option.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 1})
option.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

driver = webdriver.Chrome(
    "D:\\MyFiles\\Documents\\Workspace\\PetProject\\bot-Facebook-comment\\BotComment\\source\\chromedriver.exe", options=option)
# login
driver.get(linkToStrike)
driver.find_element_by_name("email").send_keys(email)
driver.find_element_by_name("pass").send_keys(password)
driver.find_element_by_xpath("//input[@data-testid='royal_login_button']").click()
time.sleep(3)
# jump to facebook lite to comment.
driver.get(linkToStrike.replace("www", "m"))

# --------begin----------
length = len(get_combination(message))
counter = 0
for word in get_combination(message):
    counter += 1
    send = " ".join(word)
    print(f'{counter}/{length} - {send}')
    driver.find_element_by_id("composerInput").send_keys(send)
    time.sleep(2)
    driver.find_element_by_xpath("//button[@value='Post']").click()
    time.sleep(delay)

driver.quit()
