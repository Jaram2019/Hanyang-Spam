import pickle

def sign_in():
    try:
        with open('MyAccount','rb+') as fp:
            (ID,PASSWORD) = pickle.load(fp)
        return ID,PASSWORD
    except:
        return sign_up()

def sign_up():
    with open('MyAccount','wb') as fp:
        pickle.dump((input('아이디:'),input('비밀번호:')), fp)
    return sign_in()

def foece_sign_up(ID,PASSWORD):
    with open('MyAccount','wb') as fp:
        pickle.dump((ID,PASSWORD), fp)
    return sign_in()
