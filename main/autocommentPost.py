from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


def getNextLetter(message):
    return message[0]


email = "01688888703"
password = "minhvoi03"
linkToStrike = "https://www.facebook.com/thaiminhpv/posts/1165430377151066"
message = "va"
delay = 3  # seconds

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

driver.find_element_by_xpath("//input[@data-testid='royal_login_button']").click()
time.sleep(3)
# jump to facebook lite to comment.
driver.get(linkToStrike.replace("www", "m"))

for i in range(10):
    driver.find_element_by_id("composerInput").send_keys(getNextLetter(message))
    driver.find_element_by_xpath("//button[@value='Post']").click()
    time.sleep(delaj)


driver.quit()
