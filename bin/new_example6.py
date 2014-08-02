  #!/bin/env python
import os
import sys
import re
import linecache
import string
word_list=[]
word_dict={}
valueOfJaccard=[]
union=[]
Jaccard=[]
openFile='../data/e6'
Sentence = raw_input("Please enter the sentence : ")
word_sentence_set=set()
word_in_sentence=[]
inters=[]


def  getDictionary(filename,word_dict,union):
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
                    word_dict[word].append(line_number)
                union[-1]+=1


def wordInSentence(Sentence,word_sentence_set):

    
    for c in string.punctuation:
        Sentence=Sentence.replace(c,"")
    Sentence=Sentence.split()
    for word in Sentence:
        if word!= r'\s+':
            word_in_sentence.append(word)
            word_sentence_set = word_sentence_set|set(word_dict[word])
    word_sentence_set = list(word_sentence_set)
    number_of_sentence = [0 for i in range(len(word_sentence_set))]
    inters=[0 for i in range(len(word_sentence_set))]
    Jaccard=[0 for i in range(len(word_sentence_set))]
    for word in word_in_sentence:
        for index_of_sentence in word_sentence_set:
            if index_of_sentence in word_dict[word]:
                number_of_sentence[word_sentence_set.index(index_of_sentence)]+=1
    inters=number_of_sentence
    return (Jaccard,inters,word_sentence_set,word_in_sentence)


def valueOfJaccard(filename):
    #file=open(filename)
    flag=-1
    for line_index in word_sentence_set:
    #sentence_ori = linecache.getline('file',line_index)
        flag+=1
        for word in word_in_sentence:
            if line_index in word_dict[word]:
                inters[flag]+=1
        Jaccard[flag] = 1.0*inters[flag]/(union[line_index-1]+len(word_in_sentence))

    return (Jaccard)

getDictionary(openFile,word_dict,union)
Jaccard,inters,word_sentence_set,word_in_sentence=wordInSentence(Sentence,word_sentence_set)
Jaccard=valueOfJaccard(openFile)
print 'The similar sentence is:'
for index in range(len(Jaccard)):
    if Jaccard[index]==max(Jaccard):
        print linecache.getline(openFile,word_sentence_set[index])
