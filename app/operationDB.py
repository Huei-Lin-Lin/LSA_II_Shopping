import connectDB
# from typing import List, Dict
# import mysql.connector

# 連接 DB
connectDB.mydb

# 查詢資料庫菜價
def queryFoodPrice(str):
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'mysql',
        'port': '3306',
        'database': 'devopsroles',
        'auth_plugin': 'mysql_native_password'
    }
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM test_Table')
    results = [{name: color} for (name, color) in cursor]
    return result