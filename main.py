import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains



PATH = "C:\Development\chromedriver.exe"

driver = webdriver.Chrome(PATH)
driver.get("https://orteil.dashnet.org/cookieclicker/")

cookie = driver.find_element(By.ID, "bigCookie")
cookie_count = driver.find_element(By.ID, "cookies")
# items = [driver.find_element(By.ID, "productPrice"+str(item)) for item in range(1, -1, -1)]
items = []
time.sleep(5)
for i in range(1, -1, -1):
    item = driver.find_element(By.ID, "productPrice"+str(i))
    items.append(item)


# action = ActionChains(driver)
# action.click(cookie)


while True:
    cookie.click()
    count = int(cookie_count.text.split(" ")[0])
    for item in items:
        value = int(item.text)
        if count >= value:
            upgrade_action = ActionChains(driver)
            upgrade_action.move_to_element(item)
            upgrade_action.click()
            upgrade_action.perform()
