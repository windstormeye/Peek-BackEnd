from flask import jsonify

def errorOf400():
    error = {
        'code' : 400,
        'errMsg' : '请求参数有误，请检查！',
    }
    return jsonify(error)