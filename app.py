from flask import Flask
from tools.mysqlconnect import mysqlconnect
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
cur = mysqlconnect()

@app.route('/api/')
def hello_world():  # put application's code here
    cur.execute("select @@version")
    output = cur.fetchone()
    return 'Hello World!<br>MySQL version: ' + str(output[0])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
