from typing import List, Dict
from flask import Flask
import mysql.connector
import json

app = Flask(__name__)


def test_table() -> List[Dict]:
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'mysql',
        'port': '3306',
        'database': 'devopsroles',
        'auth_plugin': 'mysql_native_password'
    }
    connection = mysql.connector.connect(**config)
    print(connection)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM test_Table')
    results = [{name: color} for (name, color) in cursor]
    cursor.close()
    connection.close()

    return results


@app.route('/')
def index() -> str:
    return json.dumps({'text: test_table': test_table()})


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)