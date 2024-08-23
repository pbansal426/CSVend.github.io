from flask import Flask


app = Flask(__name__)




@app.route('/')
def home():
    return "Home Page"

@app.route('/login')
def login():
    return "Login Page"

@app.route('/sign-up')
def signup():
    return "Sign-Up Page"



if __name__ == '__main__':
    app.run(debug=True)