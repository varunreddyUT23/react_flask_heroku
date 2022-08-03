from flask import Flask;
from flask_cors import CORS, cross_origin

app = Flask(__name__, static_folder='./my-app/build', static_url_path='/')

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/api')
@cross_origin()
def get_firstName():
    return {
        "firstname": "Varun Reddy"
    }

@app.errorhandler(404)
def not_found(e):
    return app.send_static_file('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=os.environ.get('PORT', 80))

