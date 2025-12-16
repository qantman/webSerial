# WEBSERIAL
WebSeries is a utility that allows you to receive voltage values ​​from the ADS1115 ADC, located on the TroikaI2Chub multiplexer, and display the value on a page via HTTP.
This application is implemented using flask and serial.
Used an ADS 1115 ADC and a TroikaI2Chub multiplexer.

# To run the app locally: 
1. Install `Python3`.
2. Install req.
```bash
pip install pyserial flask flask_sqlalchemy
```
3. Goto in **./python** dir.
`cd python`
3. Create db in sql.
```bash
python -i -c "
  from app import app
  from models.Serial_data import db
  app.app_context().push
  db.create_all()
"
```
4. `python3 app.py`  
