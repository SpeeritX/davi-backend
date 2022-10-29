from flask import Flask, request
from dotenv import load_dotenv

from data.flights import Flights

load_dotenv()
app = Flask(__name__)
flights = Flights()


@app.route('/api/oblasts/', methods=['GET'])
def oblasts():
    return flights.oblasts

@app.route('/api/select_time/', methods=['GET'])
def filter_by_time():
    args = request.args
    return flights.filter_by_time(args.get("time_1", ""), args.get("time_2", ""))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
