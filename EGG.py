import requests
import sys
import re
from src.rsa_encryption import *
from src.signin import *
from bs4 import BeautifulSoup

ID,PASSWORD = sign_in()
session = requests.Session()

Flag = True

while(Flag):
    formdata = login(ID,PASSWORD)

    req = session.post('https://m.hanyang.ac.kr/loginSubmit.page', data=formdata)
    
    regex = re.compile('현재 입력하신 아이디가 등록되어 있지 않거나, 아이디 또는 비밀번호를 잘못 입력 하셨습니다.')
    
    if regex.findall(req.text):
        print("아이디 비밀번호 오류!")
        ID,PASSWORD = sign_up()
    else:
        Flag = False


session.get('https://m.hanyang.ac.kr/commonAjaxCall.json?apiUrl[]=/COMM/A201300050.json')
session.headers['Content-Type']= 'application/x-www-form-urlencoded; charset=UTF-8'
req = session.get('https://m.hanyang.ac.kr/commonAjaxCall.json?page=1&apiUrl=/COMM/A201300017.json')



for i in req.json()['result']['list']:
    print(i['MESSAGE'])

