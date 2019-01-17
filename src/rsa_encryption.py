import base64
import math
from Crypto.PublicKey import RSA

global _public_key = ""
global _public_key_nm = ""
global _curtimecheck = 0
global _token_req_cnt = 0

def fnRSAEnc(inData):
    if(_public_key == ""):
        print("서버에 암호화를 위한 데이터요청중입니다. 잠시만 기다려주세요.")
    
    base64Str = base64.b64encode(inData.encode('utf-8'))

    length = len(base64Str)
    splitcnt = math.ceil(length/50)
    enc_final = ""

    key_pair = RSA.generate("010001")
    _public_key = key_pair.publickey()

    for i in range(splitcnt):
        pos = i * 50
        if i == splitcnt-1:
            end_pos = len(base64Str)
        else:
            end_pos = pos + 50

        enc_final += _public_key.encrypt(base64Str[pos+1:end_pos])

    return enc_final