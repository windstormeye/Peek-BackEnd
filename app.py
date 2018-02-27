from flask import make_response, Response, jsonify, request, Flask
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker

import errors, uploadImage, base

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

# user register
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

# user login
@app.route('/peek/v1/user/login', methods=['POST'])
def register():
    if request.method == 'POST' and request.form.get('username') and request.form.get('userMD5'):
        username = request.form.get('username')
        userMD5 = request.form.get('userMD5')
        user = session.query(User).filter_by(username=username).all()
        salt = 'peek2018'
        md5string = username + user[0].passwd + salt
        finalString = base.md5String(md5string)
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

# get uploadImage token
@app.route('/peek/v1/uploadImageToken', methods=['GET'])
def uploadimagetoken():
    if request.args.get('username'):
        username = request.args.get('username')
        token = uploadImage.getUploadToken(username)
        response = {
            'username' : username,
            'token' : token,
        }
        return jsonify(response)
    else:
        return errors.errorOf400()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
