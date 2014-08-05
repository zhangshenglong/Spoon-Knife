#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:  
@contact:  
@date:  
@version: 0.0.0
@license:  
@copyright:  

"""

import os
import sys
import re
import linecache
import string


def wordInSentence(Sentence,word_dict,word_sentence_set,word_in_sentence):

    
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


def valueOfJaccard(filename,word_dict,word_in_sentence,word_sentence_set,Jaccard,inters,union):
    #file=open(filename)
    flags=-1
    for line_index in word_sentence_set:
    #sentence_ori = linecache.getline('file',line_index)
        flags+=1
        for word in word_in_sentence:
            if line_index in word_dict[word]:
                inters[flags]+=1
        Jaccard[flags] = 1.0*inters[flags]/(union[line_index-1]+len(word_in_sentence))
    return(Jaccard)
