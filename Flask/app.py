from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer

app = Flask(__name__)

db = SQLAlchemy()
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///flask.db"
db.init_app(app)

class User(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String(50), unique=True)
    email: Mapped[str] = mapped_column(String(120))
    password: Mapped[str] = mapped_column(String(200))

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

# first type = run this command in python shell
# >>> from app import app, db
# >>> app.app_context().push()
# >>> db.create_all()

# second type = run this command in python shell
# >>> from app import app, db, User
# >>> u = User(username="vishal", email="lvishal108@gmail.com", password="Python@8788")
# >>> db.session.add(u)
# >>> db.session.commit()
# >>> User.query.all()
