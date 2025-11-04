from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello Flask i am a home page' 

@app.route('/hello')
def hello():
    return 'Hello Flask i am a hello page'


if __name__ == '__main__':
    app.run(debug=True)