# from asyncio.windows_events import NULL
from urllib import parse # 做編碼轉換
# 抓 愛料理 首頁的網頁原始碼
# 用內建套件 request 做網路連線
from cgitb import html
import urllib.request as req
import bs4 # 載入套件，利用套件幫我們做解析

def connect(url):
    # 建立一個 Request 的物件，附加 Request Headers 的資訊
    request = req.Request(url, headers={
        "User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
    }) 
    try:
        # 打開網頁，不要直接用 url，用 request
        with req.urlopen(request) as response:
            data = response.read().decode("utf-8")
        return data
    except:
        return None

def getRecipeData(recipeStr, homeURL):
    recipeArr = [] # 放食譜名稱
    recipeHrefArr = [] # 放食譜連結
    recipeURL = parse.quote(recipeStr)
    url = homeURL + "/search/{recipeURL}/".format(recipeURL=recipeURL)
    
    data = connect(url)
    if(data == None):
        return "查無資料", "查無資料", False
    
    # 解析原始碼，root 代表整份網頁
    root = bs4.BeautifulSoup(data, "html.parser")
    # 找 class_ = "browse-recipe-item" 的 li 標籤
    for recipeArticle in root.find_all("li", class_ = "browse-recipe-item"):
        # 抓每個食譜的連結
        href = recipeArticle.a.get('href')
        recipeHrefArr.append(href)
        # 抓每個食譜的標題名稱
        article = recipeArticle.a.article 
        div1 = article.find("div", class_ = "browse-recipe-content")
        recipeArr.append(div1.h2.string.replace("\n","")) # 去除換行符號
    return recipeHrefArr, recipeArr, True

# 取得食譜中的食材
def getRecipeDetail(url): 
    data = connect(url)
    if(data == None):
        return "查無資料", "查無資料"
    
    # 解析原始碼，root 代表整份網頁
    root = bs4.BeautifulSoup(data, "html.parser")

    # headcount 人數

    # 找食材
    ingredientsArr = []
    ingredientsGroups = root.find("div", class_ = "ingredients-groups")
    for groups in ingredientsGroups.find_all("div", class_ = "group"):
        for ingredient in groups.div.find_all("div", class_ = "ingredient"):
            ingredientName = ingredient.find("div", class_ = "ingredient-name").a.string
            ingredientUnit = ingredient.find("div", class_ = "ingredient-unit").string
            ingredientsArr.append([ingredientName, ingredientUnit])
    print("食材 array：", ingredientsArr)
    # print(ingredientsGroups.findChildren("div", class_="group"))

    

def main():
    recipeStr = input("請輸入想要搜尋的菜名：")
    homeURL = "https://icook.tw" 
    recipeHrefArr, recipeArr, getDataSuccess = getRecipeData(recipeStr, homeURL)
    if(getDataSuccess):
        print("\n食譜連結：", recipeHrefArr,"\n\n食譜標題名稱：", recipeArr)
        index = int(input("\n請輸入你想要哪一個食譜的編號："))
        recipeURL = homeURL + recipeHrefArr[index]
        print(recipeURL)
        getRecipeDetail(recipeURL)
if __name__ == '__main__':
    main()