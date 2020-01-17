import logging.handlers

from flask import Flask, request, jsonify

app = Flask(__name__)

logging.basicConfig(filename = 'logs/flask.log', format = '[%(asctime)s] %(levelname)s: %(message)s', level = 'DEBUG')

@app.route('/')
def index():
    return 'Menstagram AI'

@app.route('/api/v1/ramen/judge', methods = ['POST'])
def ramen_judge():
    # TODO: 画像リクエストの受け取り
    app.logger.info(request.form.get('hoge'))

    # TODO: ラーメン判定

    return jsonify([
        True, True, True, True,
    ])

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 80, debug = True)