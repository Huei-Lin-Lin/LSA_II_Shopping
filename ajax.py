from flask import Flask, render_template, request, jsonify, json
import crawlerRecipe, VegetableQuotation, ArrangeData
import time 
app = Flask(__name__)


@app.route('/data')
def webapi():
    return render_template('data.html')


@app.route('/data/message', methods=['GET'])
def getDataMessage():
    if request.method == "GET":
        with open('static/data/message.json', 'r') as f:
            data = json.load(f)
            print("text : ", data)
        f.close
        return jsonify(data)  # 直接回傳 data 也可以，都是 json 格式


@app.route('/data/message', methods=['POST'])
def setDataMessage():
    if request.method == "POST":
        data = {
            'appInfo': {
                'name': request.form['app_name'],
                'sum': request.form['app_sum']
            }
        }
        print(type(data))
        with open('static/data/input.json', 'w') as f:
            json.dump(data, f) # 使用 json 物件，寫入 json 文字格式到 input.json 檔案
        f.close
        with open('static/data/input.json', 'r') as f:
            data = json.load(f)
            print("text : ", data)
        f.close
        # 進行爬蟲
        time.sleep(1)
        crawlerRecipe.main()
        time.sleep(1)
        VegetableQuotation.main()
        time.sleep(1)
        ArrangeData.main()
        return jsonify(data)


if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)