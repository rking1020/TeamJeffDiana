from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello Data Analytics'


if __name__ == '__main__':
    app.run(host='0.0.0.0')

        
