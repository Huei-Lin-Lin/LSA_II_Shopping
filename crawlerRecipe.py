from selenium import webdriver
from selenium.webdriver.common.keys import Keys  # 讓我們可以按鍵盤上的按鍵
import time 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
# 引入其他 python 檔案
import driverPath

def getRecipeData(url, recipe):
    # 變數
    linkList = [] # 抓到的食譜連結
    ingredArr = [] # 指令食譜的食材
    ingredUnitArr = [] # 指令食譜食材的數量
    index = 5
    path = driverPath.path

    driver = webdriver.Chrome(path)
    driver.get(url)
    # 搜尋
    search = driver.find_element(By.NAME, "q")
    search.clear()
    search.send_keys(recipe)
    search.send_keys(Keys.RETURN)
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CLASS_NAME, "browse-title-name"))
    )

    # 抓食譜連結
    time.sleep(2)
    links = driver.find_elements(By.CLASS_NAME, "browse-recipe-link")
    for link in links:
        linkList.append(link)

    # 選定食譜後，進入頁面
    linkEnter = linkList[index]
    linkEnter.click()
    
    # 抓食材資料
    headcount = driver.find_element(By.CLASS_NAME, "num").text
    ingredients = driver.find_elements(By.CLASS_NAME, "ingredient-name")
    ingredientsUnit = driver.find_elements(By.CLASS_NAME, "ingredient-unit")
    for ingredient in ingredients:
        ingredArr.append(ingredient.text)
    for u in ingredientsUnit:
        ingredUnitArr.append(u.text)
    # 卡個 5 秒在關掉
    time.sleep(2) 
    driver.quit()
    ingredentDict = combineList(ingredArr,ingredUnitArr)
    recipeData = dict()
    recipeData['headcount'] = headcount
    recipeData['ingredent'] = ingredentDict
    # 把資料寫入 json 檔
    writeJSON(recipeData, "./static/data/backEnd/recipeData.json")
    # print(recipeData)
    return headcount, ingredentDict

def combineList(list1, list2):
    newDICT = dict(zip(list1,list2))
    return newDICT

def writeJSON(data, jsonPath):
    with open(jsonPath, 'w') as f:
        json.dump(data, f)
    f.close()

def readJSON(path):
    jsonFile = open(path, 'r')
    f =  jsonFile.read() # 要先使用 read 讀取檔案
    a = json.loads(f) # 再使用 loads
    return a

def main():
    inputData = readJSON('./static/data/input.json')
    recipe = inputData["appInfo"]["name"]

    url = "https://icook.tw"
    headcount, ingredentDict = getRecipeData(url, recipe)
    print(headcount, ingredentDict)
if __name__ == '__main__':
    main()