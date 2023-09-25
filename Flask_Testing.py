import flask
from flask import jsonify 
from functools import wraps
import os 

app = flask.Flask(__name__)

def require_api_key(func):
    @wraps(func)
    def decorated_func(*arg, **kwargs):
        provide_api_key = flask.request.headers.get('OPEC-Api-Key')
        if provide_api_key == os.getenv('API_KEY'):
            return func(*arg, **kwargs)
        else:
            return jsonify({'message':'Unauthorized'})
    return decorated_func

@app.route('/')
def hello():
    return 'Hello World'

@app.route('/test')
def DoTest():
    return 'For Test'

@app.route('/api/getjson', methods=['GET'])
@require_api_key
def GetJson():
    data = {
        'name': 'John',
        'age': 30,
        'city': 'New York'
    }
    return jsonify(data)



if __name__ == '__main__':
    app.run(debug=True)

