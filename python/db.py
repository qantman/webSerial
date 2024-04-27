from app import app, db
from SerialDataReceiver import SerialDataReceiver
from models.Serial_data import Serial_data
import json

sp = SerialDataReceiver()

def write_to_db():
    while True:
        with app.app_context():
                obj = sp.read()
                serial_data = Serial_data(
                    adrress=json.dumps({ "Adress" : obj["Adress"] }),
                    data=json.dumps({ "Data" : obj["Data"] })
                )
                db.session.add(serial_data)
                db.session.commit()
 
def get_last_value():
    with app.app_context():
        return Serial_data.query.order_by(Serial_data.date.desc()).all()