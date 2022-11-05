from flask import Flask
from tools.load_pandas import load_days, load_minutes
from dotenv import load_dotenv
import datetime

load_dotenv()
app = Flask(__name__)
df_minutes = load_minutes()
df_days = load_days()

@app.route('/api/')
def hello_world():
    origin_countries = df_days['origin country'].unique()
    oblasts = df_minutes.oblast.unique()
    return 'Hello World!<br>oblasts: ' + str(oblasts) + ' ' + str(origin_countries)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
