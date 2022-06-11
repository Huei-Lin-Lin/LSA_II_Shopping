from selenium import webdriver
from selenium.webdriver.common.keys import Keys  # 讓我們可以按鍵盤上的按鍵
import time 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
# 引入其他 python 檔案
import config

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
    QuotationResult = dict() # 蔬菜估價結果
    options = webdriver.ChromeOptions() 

    # to supress the error messages/logs
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options, service=config.driverPath)
    driver.get(url)

    for i in range(len(foodList)):
        WebDriverWait(driver, 50, 0.5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "slogan"))
        )
        # 在首頁的搜尋 List 中的食材
        search = driver.find_element(By.ID, "index_search03").find_element(By.ID, "textfield")
        search.clear()
        search.send_keys(foodList[i])
        search.send_keys(Keys.RETURN)

        # 嘗試搜尋食材
        try:
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
                QuotationResult[foodList[i]] = None # 找不到，所以沒有估價結果
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
            QuotationResult[name] = [price, unit]
            print("有抓到 {name} 的資料，回到首頁".format(name=name))
            driver.get(url)
        except:
            QuotationResult[foodList[i]] = None
            print("進入 {name} 連結失敗，回到首頁".format(name=foodList[i]))
            driver.get(url)
    print("各食材搜尋連結", linkDict)
    print("蔬菜估價結果", QuotationResult)
    # 卡個 5 秒在關掉
    time.sleep(2) 
    driver.quit()

def main():
    url = 'https://www.twfood.cc/'
    foodList = ['火鍋牛肉片', '青椒', '紅椒', '黃椒', '杏鮑菇', '蔥', '蒜頭', '薑泥', '玉米粉']
    getQuotationResult(url, foodList)
if __name__ == '__main__':
    main()