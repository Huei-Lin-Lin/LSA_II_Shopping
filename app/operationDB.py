# import connectDB
# # from typing import List, Dict
# # import mysql.connector

# # 連接 DB
# connectDB.mydb

# # 查詢資料庫菜價
# def queryFoodPrice(str):
#     config = {
#         'user': 'root',
#         'password': 'root',
#         'host': 'mysql',
#         'port': '3306',
#         'database': 'devopsroles',
#         'auth_plugin': 'mysql_native_password'
#     }
#     cursor = connection.cursor()
#     cursor.execute('SELECT * FROM test_Table')
#     results = [{name: color} for (name, color) in cursor]
#     return result

import connectDB

# 連接 DB
connectDB.mydb

# 查詢資料庫菜價
def queryFoodPrice(str):
    cursor = connectDB.cursor # 讓資料自動組織成字典
    sql = 'select * from foodprice WHERE foodName LIKE \'%{str}%\' '.format(str=str) # 定義 SQL 語句
    cursor.execute(sql) # 執行 SQL 語句
    result = cursor.fetchall() # 獲取返回結果
    cursor.close()
    connectDB.mydb.close()
    return result