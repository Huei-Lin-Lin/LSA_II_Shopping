from flask import Flask, render_template, request, jsonify, json
import crawlerRecipe, VegetableQuotation, ArrangeData, connectDB
from typing import List, Dict
import time

app = Flask(__name__)

def test_table() -> List[Dict]:
    mydb = connectDB.connect() # 連接 DB，讓資料自動組織成字典
    cursor = mydb.cursor(dictionary = True)
    cursor.execute('SELECT * FROM foodprice')
    results = cursor.fetchall() # 獲取返回結果
    cursor.close()
    mydb.close()
    return results

@app.route('/')
def webapi():
    return render_template('data.html')

@app.route('/data')
def index() -> str:
    return json.dumps({'text: test_table': test_table()})

@app.route('/message', methods=['GET'])
def getDataMessage():
    if request.method == "GET":
        with open('./static/data/input.json', 'r') as f:
            data1 = json.load(f)
        f.close
        with open('./static/data/quotation.json', 'r') as f:
            data2 = json.load(f)
        f.close
        with open('./static/data/afterRecipeData.json', 'r') as f:
            data3 = json.load(f)
        f.close
        data1.update(data3)
        data1.update(data2)
        print("GET-text : ", data1)
        return jsonify(data1)  # 直接回傳 data 也可以，都是 json 格式


@app.route('/message', methods=['POST'])
def setDataMessage():
    if request.method == "POST":
        data = {
            '要查詢的資料': {
                '料理名稱': request.form['app_name'],
                '準備人數': request.form['app_sum']
            }
        }
        print(type(data))
        with open('static/data/input.json', 'w') as f:
            json.dump(data, f) # 使用 json 物件，寫入 json 文字格式到 input.json 檔案
        f.close
        with open('./static/data/input.json', 'r') as f:
            data1 = json.load(f)
        f.close
        print(data1)
        # 進行爬蟲 (需先改 operationDB 的輸出，才能正確執行)
        time.sleep(1)
        crawlerRecipe.main()
        time.sleep(1)
        VegetableQuotation.main()
        time.sleep(1)
        ArrangeData.main()
        
        with open('./static/data/quotation.json', 'r') as f:
            data2 = json.load(f)
        f.close
        with open('./static/data/afterRecipeData.json', 'r') as f:
            data3 = json.load(f)
        f.close
        data1.update(data3)
        data1.update(data2)
        print("POST-text : ", data1)
        return jsonify(data1)


if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)