from app import app, db
from SerialDataReceiver import SerialDataReceiver
from flask_sqlalchemy import SQLAlchemy
from models.Serial_data import Serial_data
import json


sp = SerialDataReceiver()


def write_to_db():
    with app.app_context():
        while True:
            obj = sp.read()
            serial_data = Serial_data(
                adrress=json.dumps({ "Adress" : obj["Adress"] }),
                data=json.dumps({ "Data" : obj["Data"] })
            )
            try:
                db.session.add(serial_data)
                db.session.commit()
            except SQLAlchemy.exc.OperationalError:
                print(SQLAlchemy.exc.OperationalError)
