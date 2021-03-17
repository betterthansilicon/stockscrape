from flask import Flask
from NASDAQ import objNASDAQ
from NYSE import objNYSE
from RSSE import gameData
from RACE import RACEDATA
import json

app = Flask(__name__)
if __name__ == '__main__':
    app.debug = True
    app.run()

@app.route("/")
def hello_world():
    return 'Hello, World!'

@app.route("/nasdaq")
def nasdaq():
    return json.dumps(objNASDAQ)

@app.route("/nyse")
def nyse():
	return json.dumps(objNYSE)

@app.route("/rsse")
def rsse():
	return json.dumps(gameData)