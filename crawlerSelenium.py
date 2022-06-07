from selenium import webdriver
from selenium.webdriver.common.keys import Keys  # 讓我們可以按鍵盤上的按鍵
import time 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "C:/chromedriver_win32/chromedriver.exe"
# PATH = "/usr/lib/chromium-browser/chromedriver"
recipe = "番茄炒蛋"

driver = webdriver.Chrome(PATH)
driver.get("https://icook.tw")

# 搜尋
search = driver.find_element_by_name("q")
search.clear()
search.send_keys(recipe)
search.send_keys(Keys.RETURN)

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "browse-title-name"))
)

# 抓食譜連結
links = driver.find_elements_by_class_name("browse-recipe-link")
linkList = []
for link in links:
    linkList.append(link)
print("連結陣列 :", linkList)

# FIXME
# 選定食譜後，進入頁面
linkEnter = linkList[1]
linkEnter.click()

# 抓食材資料
headcount = driver.find_element_by_class_name("num").text
ingredients = driver.find_elements_by_class_name("ingredient-name")
ingredientsUnit = driver.find_elements_by_class_name("ingredient-unit")
ingredArr = []
ingredUnitArr = []
for ingredient in ingredients:
    ingredArr.append(ingredient.text)
for unit in ingredientsUnit:
    ingredUnitArr.append(unit.text)

print("人數 :", headcount)
print(ingredArr)
print(ingredUnitArr) 

# 卡個 5 秒在關掉
time.sleep(5) 
driver.quit()