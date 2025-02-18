# from selenium import webdriver
# from selenium.webdriver.firefox.service import Service as FirefoxService
# from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.file_detector import LocalFileDetector

# driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

# driver.get("http://www.python.org")
# assert "Python" in driver.title
# elem = driver.find_element(By.NAME, "q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()
print("Start")

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Remote(
   command_executor='http://selenium:4444/wd/hub',
   options=webdriver.FirefoxOptions(),
   keep_alive=False
)
driver.file_detector = LocalFileDetector()

# http://172.17.0.1:3000
driver.get("https://tavos-dev.thalocan.com")
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
driver.quit()