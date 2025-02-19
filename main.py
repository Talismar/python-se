from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.file_detector import LocalFileDetector

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Remote(
   command_executor='http://localhost:4444/wd/hub',
   options=webdriver.FirefoxOptions()
)
driver.file_detector = LocalFileDetector()

try:
    # http://172.17.0.1:3000
   driver.get("https://tavos-dev.thalocan.com/login")
   print(driver.title)
   # assert "Python" in driver.title
   elem = driver.find_element(By.NAME, "email")
   elem.clear()
   elem.send_keys("thalocanadministrator@tavos.com")

   driver.save_screenshot("screenshot.png")
   elem = driver.find_element(By.NAME, "password")
   elem.clear()
   elem.send_keys("Pass@2023")
   elem.send_keys(Keys.RETURN)

   WebDriverWait(driver, 10).until(lambda d: d.title == "Dashboard")
   assert "Dashboard" == driver.title
except BaseException as e:
   print(e)
finally:
   driver.quit()