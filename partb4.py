## Part B Task 4
import re
import pandas as pd
import os
import sys
import nltk
from nltk.stem.porter import *
porterStemmer = PorterStemmer()

keyword=[]
keyword=[0 for i in range(1,len(sys.argv))]

def Preprocessing(filename):
    text=open( filename,'r')
    text=text.read()
    text=re.sub(r'[^A-Za-z\n ]',r'',text)
    text=re.sub(r' +',r' ',text)
    text=re.sub(r'\n',r' ',text)
    text=text.lower()
    return text

documentid=pd.read_csv('partb1.csv')


for i in range(0,len(sys.argv)-1):
    keyword[i]=sys.argv[i+1].lower()
    keyword[i]=porterStemmer.stem(keyword[i])
for i in range(1,125):

    filename= f"{i:03}"+'.txt'
    text=Preprocessing(filename)
    flag=0
    text = nltk.word_tokenize(text)
    
    for j in range(0,len(sys.argv)-1):
        for word in text:
            stemWord = porterStemmer.stem(word)
            if stemWord==keyword[j]:
                flag+=1
                break
            
   
    if flag==len(sys.argv)-1:
        print(documentid[documentid.file_name==filename].DocumentID.iloc[0])
    