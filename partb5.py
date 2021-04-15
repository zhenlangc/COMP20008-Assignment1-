## Part B Task 5
import re
import pandas as pd
import os
import sys
import nltk
from nltk.stem.porter import *
porterStemmer = PorterStemmer()

keyword=[]
for i in range(1,len(sys.argv)):

    keyword.append(porterStemmer.stem(sys.argv[i].lower()))

def Preprocessing(filename):
    text=open( filename,'r')
    text=text.read()
    text=re.sub(r'[^A-Za-z\n ]',r'',text)
    text=re.sub(r' +',r' ',text)
    text=re.sub(r'\n',r' ',text)
    text=text.lower()
    return text

documentid=pd.read_csv('partb1.csv')




filelist=[]
term_counts=[]
dfindex=[]
globaldict={}

matchid=[]
matchfile=[]

#run part 4 to match the text file
for i in range(1,125):

    filename= f"{i:03}"+'.txt'
    text=Preprocessing(filename)
    flag=0
    text = nltk.word_tokenize(text)
    
    for j in range(0,len(keyword)):
        for word in text:
            stemWord = porterStemmer.stem(word)
            if stemWord==keyword[j]:
                flag+=1
                break
            
   
    if flag==len(sys.argv)-1:
        matchid.append(documentid[documentid.file_name==filename].DocumentID.iloc[0])
        matchfile.append(i)
            
# create a dictionary storing every possible word in the text   
for i in matchfile:
    
    filename= f"{i:03}"+'.txt'
    text=Preprocessing(filename)
    text = nltk.word_tokenize(text)
   
    for word in text:
        stemWord = porterStemmer.stem(word)
        if not stemWord in globaldict:
            globaldict[stemWord]=len(globaldict) #record the position of this word which will be the index of the global word list
            
#make up the list of each file        
for i in matchfile:
    filedict = {}
    filename= f"{i:03}"+'.txt'
    text=Preprocessing(filename)
    text = nltk.word_tokenize(text)
   
    
    filelist=[0 for i in range(len(globaldict))]
    for word in text:
        stemWord = porterStemmer.stem(word)
        
        filelist[globaldict[stemWord]]+=1
        
    term_counts.append(filelist)

from sklearn.feature_extraction.text import TfidfTransformer


transformer=TfidfTransformer()
tfidf=transformer.fit_transform(term_counts)
transformer.idf_

tfidf.toarray()


keywordlist=[0 for i in range(len(globaldict))]
for i in range(len(keyword)):
    keywordlist[globaldict[keyword[i]]]=1

import math 
q_unit=[x/(math.sqrt(len(keyword))) for x in keywordlist]
from numpy import dot 
from numpy.linalg import norm
def cosine_sim(v1,v2):
    return dot(v1,v2)/(norm(v1)*norm(v2))
doc_tfidf=tfidf.toarray()
sims=[cosine_sim(q_unit,doc_tfidf[d_id]) for d_id in range(doc_tfidf.shape[0]) ]
df=pd.DataFrame({'documentID':matchid,'score':sims})
df=df.sort_values(by='score',ascending=False)
df=df.set_index('documentID')
print(df)
