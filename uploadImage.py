from qiniu import Auth

import time, base


access_key = 'AVCX8fRcsmNfOQRhNOrkXGlgdrggPEZxMqgWG0m5'
secret_key = '0zel8u7-j-33QRP5ZggRISIiyKwweaT5-r95DAuA'

# 鉴权对象
q = Auth(access_key, secret_key)

# 上传的空间
bucket_name = 'peek'

def getUploadToken(filename):
    t = int(time.time())
    deadline = t + 300
    # 上传到七牛后保存的文件名
    key = '%s%s' % (filename, str(t))
    # 设置上传策略，不设置key七牛直接把filename Hash后作为key
    policy = {
        'deadline': deadline
    }
    token = q.upload_token(bucket_name, key, 300, policy)
    return token

