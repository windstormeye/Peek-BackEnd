from flask import Flask
from flask import request
from flask import make_response,Response

app = Flask(__name__)


@app.route('/peek/v1/user/login')
def login():
    return '2333'

@app.route('/peek/v1/user/register', methods=['post'])
def register():
    if request.method == 'POST' and request.form.get('username') and request.form.get('passwd'):
        return "4666"



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
