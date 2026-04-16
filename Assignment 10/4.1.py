from flask import Flask, jsonify

app = Flask(__name__)

airports = {
    "LFLL": {
        "name": "Lyon Saint-Exupery Airport",
        "city": "Lyon",
        "country": "FR"
    },
    "KJFK": {
        "name": "John F Kennedy International Airport",
        "city": "New York",
        "country": "US"
    },
    "EGLL": {
        "name": "Heathrow Airport",
        "city": "London",
        "country": "GB"
    }
}

@app.route("/airport/<icao>")
def get_airport(icao):
    icao = icao.upper()

    if icao in airports:
        result = {
            "icao": icao,
            "name": airports[icao]["name"],
            "city": airports[icao]["city"],
            "country": airports[icao]["country"]
        }
        return jsonify(result)
    else:
        return jsonify({"error": "Airport not found"}), 404


if __name__ == "__main__":
    app.run(debug=True, host = '127.0.0.1', port = 5000)