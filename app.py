from flask import make_response, Response, jsonify, request, Flask
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker

import hashlib

import errors

engine = create_engine('mysql+mysqldb://root:woaiwoziji123@localhost:3306/peek?charset=utf8')
Base = declarative_base()
Base.metadata.create_all(engine)
Session = sessionmaker(bind = engine)
session = Session()


class User(Base):
    __tablename__ = 'p_user'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=True)
    username = Column(String(length=11), nullable=True, primary_key=True)
    nickname = Column(String(length=15), nullable=True)
    passwd = Column(String(length=16))
    createTime = Column(String)


app = Flask(__name__)

# ¿¿¿¿
@app.route('/peek/v1/user/register', methods=['POST'])
def login():
    if request.method == 'POST' and request.form.get('username') and request.form.get('passwd'):
        session = Session()
        username = request.form.get('username')
        passwd = request.form.get('passwd')
        newUser = User(username = username, passwd = passwd)
        session.add(newUser)
        session.commit()
        session.close()
        response = {
            'status' : 'success',
            'username' : username,
        }
        return jsonify(response)


# ¿¿¿¿
@app.route('/peek/v1/user/login', methods=['POST'])
def register():
    if request.method == 'POST' and request.form.get('username') and request.form.get('userMD5'):
        session = Session()

@app.route('/peek/v1/user/register')
def login():
    return '2333'

# ÓÃ»§µÇÂ¼
@app.route('/peek/v1/user/login', methods=['POST'])
def register():
    if request.method == 'POST' and request.form.get('username') and request.form.get('userMD5'):

        username = request.form.get('username')
        userMD5 = request.form.get('userMD5')
        user = session.query(User).filter_by(username=username).all()
        salt = 'peek2018'
        md5string = username + user[0].passwd + salt
        finalString = md5String(md5string)
        if userMD5 == finalString:
            responder = {
                'status' : 'success',
                'id' : user[0].id,
                'username' : user[0].username,
                'nickname' : user[0].nickname,
                'createTime' : user[0].createTime
            }
            return jsonify(responder)
        else:
            return errors.errorOf400()
        session.close()
    else:
        return errors.errorOf400()

def md5String(string):
    md5 = hashlib.md5()
    md5.update(string.encode("utf-8"))
    return md5.hexdigest()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
