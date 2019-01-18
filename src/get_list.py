import requests
import re
import pickle
from src.rsa_encryption import *
from src.signin import *

def get_list():
    ID,PASSWORD = sign_in()
    return get_list(ID,PASSWORD)

def get_list(ID,PASSWORD):
    list = []
    session = requests.Session()

    formdata = login(ID,PASSWORD)

    req = session.post('https://m.hanyang.ac.kr/loginSubmit.page', data=formdata)
        
    regex = re.compile('현재 입력하신 아이디가 등록되어 있지 않거나, 아이디 또는 비밀번호를 잘못 입력 하셨습니다.')
        
    if regex.findall(req.text):
        print("현재 입력하신 아이디가 등록되어 있지 않거나, 아이디 또는 비밀번호를 잘못 입력 하셨습니다.")
        list.append({"UPMU_GB": "PU00","ID": 0000000,"SENDER_HP_NO": "0000000000","PUSH_READ_DATE": "2099/12/31 00:00:100","PRIORITY": "일반메세지","SEND_DTTM": "2099/12/31 00:00:100","SEND_SEQ": 000,"UUID": "00000000","MESSAGE_DIV": "P","UPMU_GB_NM": "기타","READ_YN": "Y","MESSAGE": "로그인에 실패하셨습니다!!"})
        with open('MyMessage', 'wb') as fp:
            pickle.dump(list, fp)
        return
    
    print("로그인 성공")
    
    session.get('https://m.hanyang.ac.kr/commonAjaxCall.json?apiUrl[]=/COMM/A201300050.json')
    session.headers['Content-Type']= 'application/x-www-form-urlencoded; charset=UTF-8'

    page_index = 1

    while (True):
        req = session.get('https://m.hanyang.ac.kr/commonAjaxCall.json?page='+str(page_index)+'&apiUrl=/COMM/A201300017.json')
        Q = 0
        for i in req.json()['result']['list']:
            list.append(i)
            Q+=1
        if (Q==0):
            break
        else:
            page_index += 1

    with open('MyMessage', 'wb') as fp:
        pickle.dump(list, fp)
    print("메세지 목록을 업데이트했습니다.")
