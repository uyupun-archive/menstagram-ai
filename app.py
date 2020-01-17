import logging.handlers

from flask import Flask, jsonify

app = Flask(__name__)

handler = logging.handlers.RotatingFileHandler('logs/flask.log', 'a+', maxBytes = 3000, backupCount = 5)
handler.setFormatter(logging.Formatter('[%(asctime)s] %(levelname)s: %(message)s'))
app.logger.addHandler(handler)

@app.route('/')
def index():
    return 'Menstagram AI'

@app.route('/api/v1/ramen/judge')
def ramen_judge():
    app.logger.debug('debug')
    app.logger.info('info')
    app.logger.warn('warn')
    app.logger.error('error')
    app.logger.critical('critical')
    return jsonify([
        True, True, True, True,
    ])

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 80, debug = True)