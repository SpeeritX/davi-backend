from flask import Flask
from tools.load_pandas import load_dataset
from dotenv import load_dotenv
import datetime

load_dotenv()
app = Flask(__name__)
df = load_dataset()

@app.route('/api/')
def hello_world():
    oblasts = df.oblast.unique()
    return 'Hello World!<br>oblasts: ' + str(oblasts)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
