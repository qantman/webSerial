# webSerial
* This application is implemented using flask and serial.

* Used an ADS 1115 ADC and a TroikaI2Chub multiplexer

# To run the app locally:
  1. `pip install pyserial && pip install flask && pip install flask_sqlalchemy`
  1. `python3 app.py`
  
# Create DB:
*	1.	`python3 >>> from app import app`
*	2.	`python3 >>> from models.Serial_data import db`
*	3.	`python3 >>> app.app_context().push`
*	4.	`python3 >>> db.create_all()`

