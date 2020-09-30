from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

email = "01688888703"
password = "minhvoi03"
linkToStrike = "https://www.messenger.com/t/3172666576099953"
message = ":)"
delay = 1  # seconds

option = Options()

option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")

# Pass the argument 1 to allow and 2 to block
option.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 1})

driver = webdriver.Chrome(
    "D:\MyFile\Documents\Workspace\Webscrawling\\bot Facebook comment\BotComment\main\chromedriver.exe", options=option)

# login
driver.get(linkToStrike)
driver.find_element_by_name("email").send_keys(email)
driver.find_element_by_name("pass").send_keys(password)
driver.find_element_by_id("loginbutton").click()

for i in range(100):
    driver.find_element_by_xpath("//div[@aria-label='Type a message, @name...']").send_keys(message)
    driver.find_element_by_xpath("//a[@aria-label='Send']").click()
driver.quit()
