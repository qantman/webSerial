from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import threading



app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlite.db'


db = SQLAlchemy(app)


@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html')


if __name__ == "__main__":
    from db import write_to_db
    threading.Thread(target=write_to_db).start()
    
    app.run(debug=True)