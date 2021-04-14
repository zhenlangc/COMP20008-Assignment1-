#!/usr/bin/env python
# coding: utf-8

# In[62]:




import os
import pandas as pd
import re
import sys

filername=re.findall(r'\d{3}\.txt',sys.argv[1])

os.getcwd()
os.listdir()
def Proprocessing(filename):
    text=open( filename,'r')
    text=text.read()
    text=re.sub(r'[^A-Za-z\n ]',r'',text)
    text=re.sub(r' +',r' ',text)
    text=re.sub(r'\n',r' ',text)
    text=text.lower()
    print(text)
Proprocessing(filername[0])

