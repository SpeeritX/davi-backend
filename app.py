from flask import Flask, request, Response
from dotenv import load_dotenv

from data.flights import Flights

load_dotenv()
app = Flask(__name__)
flights = Flights()

@app.route('/api/oblasts/', methods=['GET'])
def oblasts():
    return flights.oblasts

@app.route('/api/flights/', methods=['GET'])
def filter_by_date():
    args = request.args
    return flights.filter_by_date(args.get("date_1", ""), args.get("date_2", "")).to_json(orient='records')

@app.route('/api/flights_filtered_by_origin_country/', methods=['GET'])
def filter_by_date_and_org_ctr():
    args = request.args
    return flights.filter_by_date_and_origin_country(args.get("date_1", ""), args.get("date_2", ""), args.get("country", "")).to_json(orient='records')

@app.route('/api/flights_by_id/', methods=['GET'])
def filter_by_flight_id():
    args = request.args
    return flights.filter_by_flight_id(args.get("flight_id", "")).to_json(orient='records')

@app.route('/api/flights_by_spi/', methods=['GET'])
#spi value not in dataset
def filter_by_date_and_spi():
    args = request.args
    return flights.filter_by_date_and_spi(args.get("date_1", ""), args.get("date_2", ""), args.get("spi", "")).to_json(orient='records')

# TODO: squawk (value not in dataset)
@app.route('/api/flights_by_maxvel/', methods=['GET'])
def filter_by_date_and_max_velocity_higher():
    args = request.args
    return flights.filter_by_date_and_max_velocity_higher(args.get("date_1", ""), args.get("date_2", ""), args.get("vel", "")).to_json(orient='records')
@app.route('/api/flights_by_maxalt/', methods=['GET'])
def filter_by_date_and_max_altitude_higher():
    args = request.args
    return flights.filter_by_date_and_max_altitude_higher(args.get("date_1", ""), args.get("date_2", ""), args.get("alt", "")).to_json(orient='records')
@app.route('/api/flights_filtered_by_current_country/', methods=['GET'])
def filter_by_date_and_current_ctr():
    args = request.args
    return flights.filter_by_date_and_current_country(args.get("date_1", ""), args.get("date_2", ""), args.get("country", "")).to_json(orient='records')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
