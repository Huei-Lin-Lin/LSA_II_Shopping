from selenium.webdriver.chrome.service import Service

# docker-compose 整合版路徑
driverPath = Service(r"http://selenium:4444/wd/hub")
path = "http://selenium:4444/wd/hub"