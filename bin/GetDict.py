#!/bin/env python
import os
import sys
import re
import linecache
import string
import pickle
word_list=[]
word_dict={}
union=[]
path = '../data/'
openFile = os.path.join(path,'e6')


def getDictionary(filename,word_dict,union):
    file = open(filename)
    for line in file:
        word_list.append(line)
    line_number=0

    for line in word_list:
        line=str(line)
        line_number += 1
        union.append(0)
        for c in string.punctuation:
            line=line.replace(c,"")
        line_list = line.split()
        for word in line_list:
            if word!= r'\s+':
                if word not in word_dict:
                    word_dict[word] = [line_number]
                else:
                    if line_number not in word_dict[word]:
                        word_dict[word].append(line_number)
                union[-1]+=1


getDictionary(openFile,word_dict,union)
dict = os.path.join(path,'dictionary.txt')
unionf = os.path.join(path,'union.txt')
dictFile = open(dict,'wb')
unionFile = open(unionf,'wb')
pickle.dump(word_dict,dictFile)
pickle.dump(union,unionFile)
dictFile.close()
unionFile.close()
