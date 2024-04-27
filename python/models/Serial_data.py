from app import db
from datetime import datetime


class Serial_data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    adrress = db.Column(db.String(100))
    data = db.Column(db.String(100))
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Serial_data %r>' % self.id