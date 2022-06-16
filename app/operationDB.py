import connectDB

# 查詢資料庫菜價
def queryFoodPrice(str):
    mydb = connectDB.connect() # 連接 DB，讓資料自動組織成字典
    cursor = mydb.cursor(dictionary = True)
    sql = 'select * from foodprice WHERE foodName LIKE \'%{str}%\' '.format(str=str) # 定義 SQL 語句
    cursor.execute(sql) # 執行 SQL 語句
    result = cursor.fetchall() # 獲取返回結果
    cursor.close()
    mydb.close()
    return result