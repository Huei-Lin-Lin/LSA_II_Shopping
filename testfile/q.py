from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

driver = webdriver.Remote(
    command_executor='http://selenium:4444/wd/hub',
    desired_capabilities=DesiredCapabilities.CHROME,
    )

print(driver)