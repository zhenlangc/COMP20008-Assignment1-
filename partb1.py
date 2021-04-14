## Part B Task 1

import os
import pandas as pd
import re
import sys

os.getcwd()
os.listdir()
file_name=[]
file_name=[0 for i in range(124)]
DocumentID=[]
DocumentID=[0 for i in range(124)]
for i in range(1,125):
    
    text=open( f"{i:03}"+'.txt','r')
    text=text.read()
    ID=re.findall(r'[A-Z]{4}-\d\d\d[A-Za-z]{0,2}',text)
    
    if len(ID[0])==10:
        if ID[0][-1].isupper()==True:
            
            ID=ID[0][0:9]
        else:
            ID=ID[0][0:8]
        
        
    else:
        ID=ID[0]
    DocumentID[i-1]=ID
    file_name[i-1]=f"{i:03}"+'.txt'
df=pd.DataFrame(file_name,columns=['file_name'])
df['DocumentID']=DocumentID
df.to_csv(sys.argv[1])

