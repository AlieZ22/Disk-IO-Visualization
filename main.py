import flask
from flask_cors import CORS
from flask import Flask

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
CORS(app)

@app.route('/')
def index():
    return flask.send_from_directory('visualization','index.html')

@app.route('/imrsim_256MB_seq_write.csv')
def csv1():
    return flask.send_from_directory('traces','imrsim_256MB_seq_write.csv')

@app.route('/imrsim_256MB_rand_rewrite.csv')
def csv2():
    return flask.send_from_directory('traces','imrsim_256MB_rand_rewrite.csv')

if __name__ == '__main__':
    app.run(host='localhost',port=8081,debug=True)