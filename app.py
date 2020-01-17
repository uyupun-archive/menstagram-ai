import os
import logging

from flask import Flask, request, jsonify

app = Flask(__name__)
app.config.from_pyfile('.env')
logging.basicConfig(filename = 'logs/flask.log', format = '[%(asctime)s] %(levelname)s: %(message)s', level = app.config['LOG_LEVEL'])

@app.route('/')
def index():
    return 'Menstagram AI'

@app.route('/api/v1/ramen/judge', methods = ['POST'])
def judge_ramen():
    file = request.files.get('image1')
    file.save(os.path.join(file.filename))

    # TODO: ラーメン判定

    return jsonify([
        True, True, True, True,
    ])

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 80, debug = True)