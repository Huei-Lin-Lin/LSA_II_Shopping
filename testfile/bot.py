#from time import sleep
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver

#sleep(5)

print("Test Execution Started")
options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Remote(
    command_executor='http://selenium:4444/wd/hub',
    options=options
)

# driver = webdriver.Remote('http://selenium:4444/wd/hub',
#                             desired_capabilities=DesiredCapabilities.CHROME)
#driver.get('https://python.org')
#driver.save_screenshot('screenshot.png')
driver.get("http://www.baidu.com/")
size = driver.find_element_by_name("wd").size
print(size)
#尺寸: {'width': 500, 'height': 22}
news = driver.find_element_by_xpath("//div[@id='u1']/a[1]").text
print(news)
#文字: 新聞
href = driver.find_element_by_xpath("//div[@id='u1']/a[2]").get_attribute('href')
name = driver.find_element_by_xpath("//div[@id='u1']/a[2]").get_attribute('name')
print(href,name)
#屬性值: http://www.hao123.com/ tj_trhao123
location = driver.find_element_by_xpath("//div[@id='u1']/a[3]").location
print(location)
#座標: {'y': 19, 'x': 498}
print(driver.current_url)
#當前連結: https://www.baidu.com/
print(driver.title)
#標題: 百度一下， 你就知道
result = location = driver.find_element_by_id("su").is_displayed()
print(result)