import os
import re
import sys
reload(sys)
sys.setdefaultencoding('utf8')
openFile='../data/e6'
#PATH='e6engl'

def ifFileExists(filename):
    try:
        open(filename)
        return True
    except:
        print "The similar file is missing or is not readable"
        return exit(0)


def findSimilarSentence(filename,sentence):
    file=open(filename)
    lines = file.readlines()
    rowNumber =len(lines)
    count = [ 0 for i in range(rowNumber)]
    aLineASentence = re.split(r'\s+',sentence)
    sentenceLength = len(aLineASentence)
    #print lines 
    similarWordNumber = -1
    for oneLine in lines:
        similarWordNumber = similarWordNumber+1
        noPunctuation = re.split(r'\s+',oneLine)
        WordNumber = len(noPunctuation)
        for indexOne in range(sentenceLength):
            for indexTwo in range(WordNumber):
                if cmp(aLineASentence[indexOne].lower(),noPunctuation[indexTwo].lower())==0:
                    count[similarWordNumber] = count[similarWordNumber]+1
    print 'The similar sentence is:'
    for index  in range(rowNumber):
        if count[index]==max(count):
            print lines[index].encode('gbk')


ifFileExists(openFile)
sentence = raw_input("Please enter the sentence : ")
findSimilarSentence(openFile,sentence)

