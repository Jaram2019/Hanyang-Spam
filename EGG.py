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
        print("현재 입력하신 아이디가 등록되어 있지 않거나, 아이디 또는 비밀번호를 잘못 입력 하셨습니다.")
        ID,PASSWORD = sign_up()
    else:
        Flag = False


session.get('https://m.hanyang.ac.kr/commonAjaxCall.json?apiUrl[]=/COMM/A201300050.json')
session.headers['Content-Type']= 'application/x-www-form-urlencoded; charset=UTF-8'


list = []
page_index = 1
while (page_index>0):
    req = session.get('https://m.hanyang.ac.kr/commonAjaxCall.json?page='+str(page_index)+'&apiUrl=/COMM/A201300017.json')
    Q = 0
    for i in req.json()['result']['list']:
        print("Loding")
        print(i['MESSAGE'])
        print()
        Q+=1
    if (Q==0):
        page_index = 0
    else:
        page_index += 1
    
