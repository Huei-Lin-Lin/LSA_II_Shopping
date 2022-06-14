from tempfile import tempdir
from unittest import result
from selenium import webdriver
from selenium.webdriver.common.keys import Keys  # 讓我們可以按鍵盤上的按鍵
import time 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import json
# 引入其他 python 檔案
import driverPath
import operationDB

# 檢查 element 是否存在
def isElementExist(driver, by, value):
    try:
        element = driver.find_element(by=by, value=value)
    except NoSuchElementException as e:
        return False
    return True

# 得到食材估價結果
def getQuotationResult(url, foodList):
    linkDict = dict() # 各食材搜尋連結
    crawlerKey = []
    crawlerValue = []
    options = webdriver.ChromeOptions() 

    # to supress the error messages/logs
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--no-sandbox')   
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=options, service=driverPath.driverPath)
    # driver = webdriver.Remote(
    #     options=options, 
    #     command_executor=driverPath.path
    # )
    driver.get(url)

    for i in range(len(foodList)):
        # 嘗試搜尋食材
        try:
            WebDriverWait(driver, 50, 0.5).until(
                EC.presence_of_element_located((By.CLASS_NAME, "slogan"))
            )
            # 在首頁的搜尋 List 中的食材
            search = driver.find_element(By.ID, "index_search03").find_element(By.ID, "textfield")
            search.clear()
            search.send_keys(foodList[i])
            search.send_keys(Keys.RETURN)
            haveLink = False # 食材有沒有搜尋連結 
            # 顯性等待 DyListCover-hot class 加載出来 20 秒，每 0.5 秒檢查一次
            WebDriverWait(driver, 50, 0.5).until(
                EC.presence_of_element_located((By.CLASS_NAME, "button_logo"))
            )
            time.sleep(2)
            # 如果有 weekTrend 代表直接跳出食材搜尋結果
            if (isElementExist(driver, By.ID,  "weekTrend")):
                print("直接給食材搜尋結果")
                linkDict[foodList[i]] = driver.current_url # 將抓到的連結存起來
                haveLink = True
                raise Exception('out')
            # 抓 link 
            time.sleep(2)
            link = driver.find_element(By.CLASS_NAME, "text-left").find_element(By.TAG_NAME, "a").get_attribute("href")
            linkDict[foodList[i]] = link # 將抓到的連結存起來
            haveLink = True
            print("將抓到 {name} 的連結存起來".format(name=foodList[i]))
        except: # 如果沒有搜尋結果，就跳回首頁，換搜尋下一個食材
            if(haveLink == False):
                print("找不到 {name} 相關的資料".format(name=foodList[i]))
                linkDict[foodList[i]] = None # 找不到，所以此食材沒有搜尋連結
                # 找不到，所以沒有估價結果
                crawlerKey.append(foodList[i])
                crawlerValue.append(None)
                print("回到首頁，搜尋下一個")
                driver.get(url)
                continue

        # 嘗試進入食材連結
        try: 
            link = linkDict[foodList[i]]
            driver.get(link)
            print("進入 {name} 頁面".format(name=foodList[i]))
            WebDriverWait(driver, 50, 0.5).until(
                EC.presence_of_element_located((By.CLASS_NAME, "text-left"))
            )
             # 抓食材的資料
            time.sleep(2)
            name = driver.find_element(By.CLASS_NAME, "vege_price").find_element(By.CLASS_NAME, "h4").text # 菜名
            price = driver.find_element(By.XPATH, "//*[@id=\"vege_chart\"]/div[1]/div/div[1]/table/tbody/tr[5]/th[1]").text # 價錢
            unit = driver.find_element(By.XPATH, "//*[@id=\"vege_chart\"]/div[1]/div/div[1]/table/tbody/tr[5]/th[2]").text
            crawlerKey.append(name)
            crawlerValue.append([price, unit])
            print("有抓到 {name} 的資料，回到首頁".format(name=name))
            driver.get(url)
        except:
            crawlerKey.append(foodList[i])
            crawlerValue.append(None)
            print("進入 {name} 連結失敗，回到首頁".format(name=foodList[i]))
            driver.get(url)
    # 卡個 5 秒在關掉
    time.sleep(2) 
    driver.quit()
    return crawlerKey, crawlerValue

def queryDB(foodList):
    tempDict = dict() # 蔬菜估價結果
    for i in range(len(foodList)):
        result = operationDB.queryFoodPrice(foodList[i])
        if(result == ()):
            print("資料庫沒有 {food} 的資料".format(food = foodList[i]))
            tempDict[foodList[i]] = None
        else: # 資料庫有資料
            print(result[0]['foodName'])
            print(foodList[i])
            tempDict[foodList[i]] =  [result[0]['price'], result[0]['unit']] # 以第一筆資料為主
    return tempDict

def checkNotQuery(firstResult):
    noResult = [] # 沒有查詢結果
    keyResult = [] # 有結果，key
    valueResult = [] # 有結果，value
    for key, value in firstResult.items():
        if value == None:
            noResult.append(key)
        else:
            keyResult.append(key)
            valueResult.append(value)
    return noResult, keyResult, valueResult


def writeJSON(data, jsonPath):
    with open(jsonPath, 'w') as f:
        json.dump(data, f)
    f.close()

def readJSON(path):
    jsonFile = open(path, 'r')
    f =  jsonFile.read() # 要先使用 read 讀取檔案
    a = json.loads(f) # 再使用 loads
    return a

def divideDICT(dict):
    keyList = []
    valueList = []
    for key, value in dict.items():
        keyList.append(key)
        valueList.append(value)
    return keyList, valueList    

# 把兩個 list 合成一個 DICT
def combineList(list1, list2):
    newDICT = dict(zip(list1,list2))
    return newDICT


def main():
    url = 'https://www.twfood.cc/' # 要爬蟲的網址
    foodDict = readJSON("./static/data/recipeData.json")
    foodList , unitList = divideDICT(foodDict['ingredent'])
    print(foodList)
    # 先查資料庫的價格
    firstResult = queryDB(foodList)
    print("===============")
    print("查完資料庫後的狀況",firstResult)
    noResult, keyList, valueList = checkNotQuery(firstResult)
    print("沒有結果", noResult)
    print("有結果 key", keyList)
    print("有結果 value", valueList)
    print("===============")
    # 再爬蟲查菜價
    crawlerKey, crawlerValue = getQuotationResult(url, noResult)
    # 把查到的結果合再一起，key 對 key，value 對 value
    keyResult = keyList + crawlerKey
    valueResult = valueList + crawlerValue
    # 把 key 跟 value 合成一個字典
    finalResult = combineList(keyResult, valueResult)
    writeJSON(finalResult, "./static/data/quotation.json")
if __name__ == '__main__':
    main()