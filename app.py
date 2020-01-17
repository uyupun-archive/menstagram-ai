from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return 'Menstagram AI'

@app.route('/api/v1/ramen/judge')
def ramen_judge():
    return jsonify([
        True, True, True, True,
    ])

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 80, debug = True)