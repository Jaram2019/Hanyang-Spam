import pickle

try:
    with open ('MyMessage', 'rb') as fp:
        list = pickle.load(fp)
except:
    from src.get_list import *
    get_list()
    with open ('MyMessage', 'rb') as fp:
        list = pickle.load(fp)
