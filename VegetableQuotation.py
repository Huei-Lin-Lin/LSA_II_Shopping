from pickle import NONE
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys  # 讓我們可以按鍵盤上的按鍵
import time 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

driverPath = Service(r"C:/chromedriver_win32/chromedriver.exe")
# driverPath = Service(r"/usr/lib/chromium-browser/chromedriver")

foodList = ['蕃茄', '雞蛋', '鹽', '白糖']
food = "芒果"
index = 0 # 選第幾個搜尋結果，例如芒果有 8 個結果，那就進入第 index 的連結
linkDict = dict() # 各食材搜尋連結
QuotationResult = dict() # 蔬菜估價結果

options = webdriver.ChromeOptions() 
# to supress the error messages/logs
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options, service=driverPath)
driver.get('https://www.twfood.cc/')

for i in range(len(foodList)):
    WebDriverWait(driver, 50, 0.5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "slogan"))
    )
    # 在首頁的搜尋 List 中的食材
    search = driver.find_element(By.ID, "index_search03").find_element(By.ID, "textfield")
    search.clear()
    search.send_keys(foodList[i])
    search.send_keys(Keys.RETURN)
    try:
        print("OK 1")
        # 顯性等待 DyListCover-hot class 加載出来 20 秒，每 0.5 秒檢查一次
        WebDriverWait(driver, 30, 0.5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "slogan"))
        )
        print("OK 2")
        time.sleep(5)

        # linkTitle = driver.find_element(By.CLASS_NAME, "text-left")
        # print("OK 3")
        # links = driver.find_element(By.CLASS_NAME, "search_result").find_elements(By.CLASS_NAME, "text-left")
        # print("OK 4")
        # linkArr = [] # 放目前食材的所有搜尋連結
        # for link in links:
        #     linkArr.append(link.find_element(By.TAG_NAME, "a").get_attribute("href"))
        # print("OK 5")

        link = driver.find_element(By.CLASS_NAME, "text-left").find_element(By.TAG_NAME, "a").get_attribute("href")
        print("OK 3")
        linkDict[foodList[i]] = link
        # linkDict[foodList[i]] = linkArr
        print("回到首頁，搜尋下一個")
        driver.get('https://www.twfood.cc/')
        print("OK 6")
    except:
        print("找不到相關的資料")
        linkDict[foodList[i]] = None
        print("回到首頁，搜尋下一個")
        driver.get('https://www.twfood.cc/')
        continue

    try:
        # FIXME 點連結的方式要改
        # 進入指定蔬菜的連結
        url =  linkDict[foodList[i]][index]
        driver.get(url)
        WebDriverWait(driver, 50, 0.5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "text-left"))
        )
        
        # 抓指定蔬菜的資料
        name = driver.find_element(By.CLASS_NAME, "text-left").text # 菜名
        price = driver.find_element(By.XPATH, "//*[@id=\"vege_chart\"]/div[1]/div/div[1]/table/tbody/tr[5]/th[1]/span").text # 價錢
        unit = driver.find_element(By.XPATH, "//*[@id=\"vege_chart\"]/div[1]/div/div[1]/table/tbody/tr[5]/th[2]").text
        QuotationResult[name] = [price, unit]

        print("回到首頁")
        driver.get('https://www.twfood.cc/')
    except:
        print("進入連結失敗，回到首頁")
        driver.get('https://www.twfood.cc/')

print("各食材搜尋連結", linkDict)
print("蔬菜估價結果", QuotationResult)

# 卡個 5 秒在關掉
time.sleep(5) 
driver.quit()