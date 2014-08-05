import os
import sys
import linecache
import string
import pickle
from CalculateSimilar import *

path = '../data/'
openFile = os.path.join(path,'e6')
if not os.path.isfile(os.path.join(path,'dictionary.txt')):
    os.system("python GetDict.py")

dic = open(os.path.join(path,'dictionary.txt'),'rb')
word_dict = pickle.load(dic)
uni = open(os.path.join(path,'union.txt'),'rb')
union = pickle.load(uni)
flag = True
while flag:
    Jaccard = []
    word_sentence_set = set()
    word_in_sentence = []
    inters = []
    Sentence = raw_input("Please enter the sentence : ")
    Jaccard,inters,word_sentence_set,word_in_sentence = wordInSentence(Sentence,word_dict,word_sentence_set,word_in_sentence)
    Jaccard = valueOfJaccard(openFile,word_dict,word_in_sentence,word_sentence_set,Jaccard,inters,union)

    print 'The similar sentence is:'
    for index in range(len(Jaccard)):
        if Jaccard[index] == max(Jaccard):
            print linecache.getline(openFile,word_sentence_set[index])
    ifQuit = raw_input("Please enter the Key:Y(quit),other(continue)")
    if ifQuit == 'Y':
        flag = 0
    else:
        pass
