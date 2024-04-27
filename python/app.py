from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import threading


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlite.db'

db = SQLAlchemy(app)

@app.route("/index")
@app.route("/")
def index():
    from db import get_last_value
    value = get_last_value()
    return render_template('index.html', value=value)


if __name__ == "__main__":    
    app.run(debug=True)
    from db import write_to_db
    threading.Thread(target=write_to_db).start()