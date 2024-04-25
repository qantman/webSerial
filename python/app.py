from flask import Flask
import json
from SerialDataReceiver import SerialDataReceiver


sp = SerialDataReceiver()


app = Flask(__name__)

        

@app.route("/")
def index():
    return json.dumps(sp.read())


if __name__ == "__main__":
    app.run(debug=True)