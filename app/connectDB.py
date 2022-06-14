import mysql.connector

def connect():
    try:
        config = {
            'user': 'root',
            'password': 'root',
            'host': 'mysql',
            'port': '3306',
            'database': 'lsa2',
            'auth_plugin': 'mysql_native_password'
        }
        mydb =  mysql.connector.connect(**config)
        # 生成一個遊標物件 ( 相當於 cmd 開啟 mysql 中的 mysql> )
        print("連線結果", mydb) # 印出連線結果
        # cursor = mydb.cursor(dictionary = True) # 讓資料自動組織成字典
        return mydb
    except:
        print("資料庫連接失敗：")