from turtle import update
from numpy import array
import copy

def UpdateIngredUnitArr(array, crawlHeadcount, userNum):
    sortArray = [] # 整理後的食材量，使用量和單位分開
    # 把數字和單位分開
    for i in range(len(array)):
        num =  ''.join([x for x in array[i] if x.isdigit()])
        unit = ''.join([i for i in array[i] if not i.isdigit()])
        sortArray.append([num, unit])
    
    copyArray = copy.deepcopy(sortArray) # 複製一份 sortArray
    # 人數轉換
    for i in range(len(copyArray)):
        # 原本食譜的數量``
        num = copyArray[i][0]
        if(num != '' and crawlHeadcount != '' and userNum != ''):
            # 根據使用者輸入的人數作換算
            newNum = round((int(num)/int(crawlHeadcount)*userNum), 1)
            # 更新食譜數量
            copyArray[i][0] = newNum
    # DEBUG 用的
    print("最初爬蟲的資料", array)
    print("原本的食譜", sortArray)
    # 要用的是這個
    print("更新後的食譜", copyArray) 

def main():
    array = ['2顆', '3顆', '1匙', '1匙'] # 食譜的數量
    peopleNum = 2 # 使用者指定的人數
    headcount = 3 # 食譜中的人數
    UpdateIngredUnitArr(array, headcount, peopleNum)
if __name__ == '__main__':
    main()