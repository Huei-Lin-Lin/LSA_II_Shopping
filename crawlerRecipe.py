from re import U
from selenium import webdriver
from selenium.webdriver.common.keys import Keys  # 讓我們可以按鍵盤上的按鍵
import time 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from string import digits

# chrome 執行檔的路徑
# PATH = "C:/chromedriver_win32/chromedriver.exe" 
# PATH = "/usr/lib/chromium-browser/chromedriver"
PATH = "/Users/yst/Library/Application Support/Google/Chrome/Default"

# 使用者需要輸入的內容
recipe = "番茄炒蛋"
peopleNum = 3 # 人數

# 變數
linkList = [] # 抓到的食譜連結
ingredArr = [] # 指令食譜的食材
ingredUnitArr = [] # 指令食譜食材的數量

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

for link in links:
    linkList.append(link)
print("連結陣列 :", linkList)

# FIXME
# 選定食譜後，進入頁面
linkEnter = linkList[3]
linkEnter.click()

# 抓食材資料
headcount = driver.find_element_by_class_name("num").text
ingredients = driver.find_elements_by_class_name("ingredient-name")
ingredientsUnit = driver.find_elements_by_class_name("ingredient-unit")

for ingredient in ingredients:
    ingredArr.append(ingredient.text)
for u in ingredientsUnit:
    ingredUnitArr.append(u.text)

print("人數 :", headcount)
print(ingredArr)
print(ingredUnitArr) 
print("================")

# 卡個 5 秒在關掉
time.sleep(5) 
driver.quit()