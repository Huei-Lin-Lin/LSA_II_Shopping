# import connectDB
import mysql.connector

mydb = mysql.connector.connect(
  host="mysql",       # 数据库主机地址
  user="dbadmin",    # 数据库用户名
  passwd="12345678"   # 数据库密码
)
 
print(mydb)

# # 連接 DB
# connectDB.mydb

# def getMysqlConnection():
#     return mysql.connector.connect(user='root', host='mysql', port='3306', password='12345678', database='mydev')

# # 查詢資料庫菜價
# def queryFoodPrice(str):
#     cursor = connectDB.cursor # 讓資料自動組織成字典
#     sql = 'select * from foodprice WHERE foodName LIKE \'%{str}%\' '.format(str=str) # 定義 SQL 語句
#     cursor.execute(sql) # 執行 SQL 語句
#     result = cursor.fetchall() # 獲取返回結果
#     return result
