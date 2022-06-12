from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

print("Test Execution Started")
options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument('--no-sandbox')   
options.add_argument('--disable-dev-shm-usage')        
driver = webdriver.Remote(
    command_executor='http://localhost:4444/wd/hub',
    options=options
)

#navigate to browserstack.com
time.sleep(5)
driver.get("https://icook.tw")
WebDriverWait(driver, 50).until(
   EC.presence_of_element_located((By.CLASS_NAME, "global-navbar-title-a"))
)

#click on the Get started for free button
time.sleep(5)
links = driver.find_element(By.CLASS_NAME, "global-navbar-title-a").click()

#close the browser
time.sleep(1) 
driver.quit()
print("Test Execution Successfully Completed!")