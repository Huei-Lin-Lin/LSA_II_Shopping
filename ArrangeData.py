import copy
import json

# 把數字和單位分開
def divide_Num_Unit(array):
    sortArray = [] # 整理後的食材量，使用量和單位分開
    for i in range(len(array)):
        num =  ''.join([x for x in array[i] if x.isdigit()])
        unit = ''.join([i for i in array[i] if not i.isdigit()])
        sortArray.append([num, unit])
    return sortArray

# 把數字和單位合在一起
def combine_Num_Unit(array):
    sortArray = []
    for i in range(len(array)):
        element = str(array[i][0]) + array[i][1]
        sortArray.append(element)
    return sortArray

def UpdateIngredUnitArr(originalQuantity, crawlHeadcount, userNum):
    sortArray = divide_Num_Unit(originalQuantity) # 整理後的食材量，使用量和單位分開
    print(sortArray)
    copyArray = copy.deepcopy(sortArray) # 複製一份 sortArray
    # 人數轉換
    for i in range(len(copyArray)):
        # 原本食譜的數量``
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

def divideDICT(dict):
    keyList = []
    valueList = []
    for key, value in dict.items():
        keyList.append(key)
        valueList.append(value)
    return keyList, valueList

def combineList(list1, list2):
    newDICT = dict(zip(list1,list2))
    return newDICT

def main():
    foodDict = readJSON("./static/data/recipeData.json")
    foodList , unitList = divideDICT(foodDict['ingredent'])

    # 使用者指定的人數
    inputData = readJSON('./static/data/input.json')
    peopleNum = inputData["appInfo"]["sum"]

    # 食譜中的人數
    headcount = foodDict['headcount']
    updateQuantity = UpdateIngredUnitArr(unitList, headcount, peopleNum)
    
    # 把更新後的數量存到 json 
    afterUnit = combineList(foodList, updateQuantity)
    newDICT = dict()
    newDICT['headcount'] = peopleNum
    newDICT['ingredent'] = afterUnit
    writeJSON(newDICT, "./static/data/afterRecipeData.json")
if __name__ == '__main__':
    main()