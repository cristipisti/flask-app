from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Bon dia"

@app.route('/uic')
def uic_func():
    return "Bon dia UIC"

if __name__ == '__main__':
    app.run(debug=True)