from flask import Flask, request
from dotenv import load_dotenv

from data.flights import Flights

load_dotenv()
app = Flask(__name__)
flights = Flights()


@app.route('/api/oblasts/', methods=['GET'])
def oblasts():
    args = request.args
    print("Params...")
    print(args)
    return flights.oblasts


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
