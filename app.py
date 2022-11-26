from flask import Flask, request, Response
from dotenv import load_dotenv
import json

from data.flights import Flights

load_dotenv()
app = Flask(__name__)
flights = Flights()


@app.route('/api/oblasts/', methods=['GET'])
def oblasts():
    return flights.oblasts


@app.route('/api/flights/<string:id>', methods=['GET'])
def filter_by_flight_id(id):
    return flights.filter_flight_by_id(id).to_json(orient='records')


@app.route('/api/flights/', methods=['GET'])
def filter_flights():
    args = request.args
    return flights.filter(args).to_json(orient='records')


@app.route('/api/regions/', methods=['GET'])
def regions():
    args = request.args
    return flights.region_counted(args).to_json()


@app.route('/api/matrix/absolute/', methods=['GET'])
def matrix_absolute():
    args = request.args
    return flights.matrix_absolute(args).reset_index().rename(
        columns={'state': 'x', 'state2': 'y'}).to_json(orient='table', index=False)


@app.route('/api/matrix/expected/', methods=['GET'])
def matrix_expected():
    args = request.args
    return flights.matrix_expected(args).reset_index().rename(
        columns={'state': 'x', 'state2': 'y'}).to_json(orient='table', index=False)


@app.route('/api/flights_count/', methods=['GET'])
def count_flights():
    args = request.args
    return flights.count(args).to_json(orient='split', index=False)


@app.route('/api/parallel/', methods=['GET'])
def parallel_flights():
    args = request.args
    return flights.parallel(args).to_json(orient='split', index=False)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
