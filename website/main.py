from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
DB_NAME = "database.db"


app = Flask(__name__)
app.config['SECRET_KEY'] = 'VHHS'
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
db.init_app(app)



@app.route('/')
def home():
    return render_template("index.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/sign-up')
def signup():
    return render_template("sign-up.html")



if __name__ == '__main__':
    app.run(debug=True)