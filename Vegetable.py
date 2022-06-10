from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys  # 讓我們可以按鍵盤上的按鍵
import time 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

driverPath = Service(r"C:/chromedriver_win32/chromedriver.exe")
# PATH = "/usr/lib/chromium-browser/chromedriver"

foodList = ['牛蕃茄', '雞蛋', '鹽', '白糖']
food = "芒果"
index = 0 # 選第幾個搜尋結果，例如芒果有 8 個結果，那就進入第 index 的連結
QuotationResult = dict() # 菜價搜尋結果

options = webdriver.ChromeOptions() 
# to supress the error messages/logs
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options, service=driverPath)
driver.get('https://www.twfood.cc/')


# DEBUG
slogan = driver.find_element(By.CLASS_NAME, "slogan")
# print(slogan.text)
# 首頁的搜尋選項
search = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[1]/div[1]/div[3]/div/form/span/input")
search.send_keys(food)
search.send_keys(Keys.RETURN)

# 顯性等待 DyListCover-hot class 加載出来 20 秒，每 0.5 秒檢查一次
WebDriverWait(driver, 20, 0.5).until(
    EC.presence_of_element_located((By.CLASS_NAME, "text-left"))
)

# links = driver.find_element(By.CLASS_NAME, "text-left").find_elements(By.TAG_NAME, "a")
links = driver.find_element(By.CLASS_NAME, "search_result").find_elements(By.CLASS_NAME, "text-left")
linkArr = []
for link in links:
    # print("連結 :", link.find_element(By.TAG_NAME, "a").get_attribute("href"))
    # print("連結 :", link.get_attribute("href"))
    linkArr.append(link.find_element(By.TAG_NAME, "a").get_attribute("href"))
    # linkArr.append(link)
# print("連結 :", linkArr)

# 進入指定蔬菜的連結
# FIXME
try:
    # print(linkArr[index])
    # FIXME 點連結的方式要改
    # 進入指定蔬菜的連結
    # url = driver.find_element(By.PARTIAL_LINK_TEXT, linkArr[index])
    url = linkArr[index]
    driver.get(url)   
    # url.click()
    WebDriverWait(driver, 50, 0.5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "text-left"))
    )
    
    # 抓指定蔬菜的資料
    name = driver.find_element(By.CLASS_NAME, "text-left").text # 菜名
    price = driver.find_element(By.XPATH, "//*[@id=\"vege_chart\"]/div[1]/div/div[1]/table/tbody/tr[5]/th[1]/span").text # 價錢
    unit = driver.find_element(By.XPATH, "//*[@id=\"vege_chart\"]/div[1]/div/div[1]/table/tbody/tr[5]/th[2]").text
    
    QuotationResult[name] = [price, unit]
    print(QuotationResult)
        
    driver.back()
    driver.back()

except:
    print("進入連結失敗")
    driver.back()

print("回到首頁")

# 卡個 5 秒在關掉
time.sleep(5) 
driver.quit()


