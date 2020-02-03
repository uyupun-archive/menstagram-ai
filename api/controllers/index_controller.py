from api import app

@app.route('/')
def index():
    return 'Menstagram AI'