# app.py
from flask import Flask , render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

db = SQLAlchemy()
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///flask.db"
db.init_app(app)



@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/login")
def login():
    return "<h1>Login</h1>"


@app.route("/register")
def register():
    return render_template("register.html")

if __name__ == "__main__":
    app.run(debug=True)