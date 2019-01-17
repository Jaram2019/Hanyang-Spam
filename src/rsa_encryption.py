import base64
import math
import requests
from jsbn import RSAKey

def fnRSAEnc(inData,_public_key):

    base64Str = base64.b64encode(inData.encode('utf-8'))
    length = len(base64Str)
    splitcnt = math.ceil(length/50)
    enc_final = ""

    rsa = RSAKey()
    rsa.setPublic(_public_key,'010001')

    
    for i in range(splitcnt):
        pos = i * 50
        if i == splitcnt-1:
            end_pos = len(base64Str)
        else:
            end_pos = pos + 50

        enc_final += rsa.encrypt(base64Str[pos:end_pos].decode("utf-8"))

    return enc_final



def login(id,password):
    new_session = requests.Session()
    new_req = new_session.get('https://m.hanyang.ac.kr/public_token.json?t=mobile')
    _public_key_nm,_public_key=new_req.text.split("|")

    return dict(
        username=fnRSAEnc(id,_public_key),
        password=fnRSAEnc(password,_public_key),
        identck=_public_key_nm,
        redirectUrl='',
        autologin='N')

