import copy
import json
import chinese2Int

# 把數字和單位分開
def divide_Num_Unit(array):
    sortArray = [] # 整理後的食材量，使用量和單位分開
    haveNum = False
    for i in range(len(array)):
        num = ''.join([x for x in array[i] if x.isdigit()])
        if (num!=''):
            haveNum = True
        unit = ''.join([i for i in array[i] if not i.isdigit()])
        # 把 中文數字 轉成數字
        tempNum, unit = chinese2Int.main(unit) # 都是回傳字串
        if(haveNum):
            try:
                if(int(tempNum)):
                    num+=int(tempNum)
            except:
                print(tempNum)
        else:
            num = tempNum
        sortArray.append([num, unit])
        haveNum = False
    return sortArray


# 把數字和單位合在一起
def combine_Num_Unit(array):
    sortArray = []
    for i in range(len(array)):
        element = str(array[i][0]) + " " + array[i][1]
        sortArray.append(element)
    return sortArray

# 依照使用者輸入的人數做食譜人數的轉換
# 例如：原本食譜是 2 人份，但使用者要 6 人份，在這個 function 中會做人數轉換
def UpdateIngredUnitArr(originalQuantity, crawlHeadcount, userNum):
    print("原本的數量", originalQuantity)
    sortArray = divide_Num_Unit(originalQuantity) # 整理後的食材量，使用量和單位分開
    copyArray = copy.deepcopy(sortArray) # 複製一份 sortArray
    # 人數轉換
    for i in range(len(copyArray)):
        # 原本食譜的數量
        num = copyArray[i][0]
        if (num == ''):
            continue
        if(num != '' and crawlHeadcount != '' and userNum != ''):
            # 根據使用者輸入的人數作換算
            newNum = round((float(num)/float(crawlHeadcount)*float(userNum)), 1)
            # 更新食譜數量
            copyArray[i][0] = newNum
    # 更新後的食譜
    updateQuantity = combine_Num_Unit(copyArray)
    print("更新後的數量", updateQuantity)
    return updateQuantity

def writeJSON(data, jsonPath):
    with open(jsonPath, 'w') as f:
        json.dump(data, f)
    f.close()

def readJSON(path):
    jsonFile = open(path, 'r')
    f =  jsonFile.read() # 要先使用 read 讀取檔案
    a = json.loads(f) # 再使用 loads
    return a

# 把字典的 key 和 value 分開變成兩個 List
def divideDICT(dict):
    keyList = []
    valueList = []
    for key, value in dict.items():
        keyList.append(key)
        valueList.append(value)
    return keyList, valueList

# 把剛剛分開的兩個 List ( keyList 和 valueList ) 合成一個字典
def combineList(list1, list2):
    newDICT = dict(zip(list1,list2))
    return newDICT

def main():
    foodDict = readJSON("./static/data/recipeData.json")
    # foodList , unitList = divideDICT(foodDict['ingredent'])
    foodList , unitList = divideDICT(foodDict['料理食材'])

    # 使用者指定的人數
    inputData = readJSON('./static/data/input.json')
    # peopleNum = inputData["appInfo"]["sum"]
    peopleNum = inputData["要查詢的資料"]["準備人數"]

    # 食譜中的人數
    # headcount = foodDict['headcount']
    headcount = foodDict['準備人數']
    updateQuantity = UpdateIngredUnitArr(unitList, headcount, peopleNum)
    
    # 把更新後的數量存到 json 
    afterUnit = combineList(foodList, updateQuantity)
    newDICT = dict()
    # newDICT['headcount'] = peopleNum # 使用者指定的人數
    newDICT['準備人數'] = peopleNum # 使用者指定的人數
    # newDICT['ingredent'] = afterUnit
    newDICT['料理食材'] = afterUnit
    writeJSON(newDICT, "./static/data/afterRecipeData.json")

    print("更新後的字典", newDICT)
if __name__ == '__main__':
    main()