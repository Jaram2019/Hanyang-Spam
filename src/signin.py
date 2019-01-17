def sign_in():
    try:
        f = open('MyAccount.txt','r+')
        ID,PASSWORD = f.read().split('\n')
        f.close()
        return ID,PASSWORD
    except:
        return sign_up()

def sign_up():
    f = open('MyAccount.txt','w+')
    f.write(input('아이디:')+'\n')
    f.write(input('비밀번호:'))
    f.close()
    
    return sign_in()
