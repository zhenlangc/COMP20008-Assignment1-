

import os
import pandas as pd
import re
import sys

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

for i in range(1,125):
    filename= f"{i:03}"+'.txt'
    text=Preprocessing(filename)
    flag=1
    
    
    for j in range(0,len(sys.argv)-1):
        
        match=re.findall(r' '+keyword[j]+' ',text) 
        
        if len(match)==0:
            flag=0
   
    if flag==1:
        print(documentid[documentid.file_name==filename].DocumentID.iloc[0])
    
        
        
   





