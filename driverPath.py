from selenium.webdriver.chrome.service import Service

# docker 測試用的路徑
driverPath = Service(r"http://localhost:4444/wd/hub")
path = "http://localhost:4444/wd/hub"

# docker-compose 整合版路徑
#driverPath = Service(r"http://selenium:4444/wd/hub")
#path = "http://selenium:4444/wd/hub"

# 本機測試用的路徑
# driverPath = Service(r"C:/chromedriver_win32/chromedriver.exe")
# path = "C:/chromedriver_win32/chromedriver.exe"  