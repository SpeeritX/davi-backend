from flask import Flask, request, Response
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
    return flights.filter_by_time(args.get("time_1", "")).to_json(orient='records')

@app.route('/api/select_date/', methods=['GET'])
def filter_by_date():
    args = request.args
    return flights.filter_by_date(args.get("time_1", ""), args.get("time_2", "")).to_json(orient='records')

@app.route('/api/select_date_and_country_count/', methods=['GET'])
def filter_by_date_and_ctr():
    args = request.args
    return flights.filter_by_date_return_country_count_too(args.get("time_1", ""), args.get("time_2", "")).to_json(orient='records')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
