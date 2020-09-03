#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 13:42:46 2020

@author: rajathsvasisth
"""

import numpy as np
import pandas as pd

datasetCO = pd.read_csv('CO_points_2018_puhar_Nov.csv')
datasetNO2 = pd.read_csv('NO_points_2018_Nov_punhar.csv')
datasetRain = pd.read_csv('rain_points_2018_Nov.csv')
datasetTemp = pd.read_csv('temp_points_2018_Nov.csv')
datasetWind = pd.read_csv('wind_points_2018_Nov.csv')

datasetCOD = pd.read_csv('CO_points_2018_Nov_Delhi.csv')
datasetNOD = pd.read_csv('NO_points_2018_Nov_Delhi.csv')

datasetCO = datasetCO.iloc[ : , :-1]
datasetNO2 = datasetNO2.iloc[:, :-1]
datasetRain = datasetRain.iloc[ : , :-1]
datasetTemp = datasetTemp.iloc[ : , :-1]
datasetWind = datasetWind.iloc[ : , :-1]
datasetCOD = datasetCOD.iloc[ : , :-1]
datasetNOD = datasetNOD.iloc[ : , :-1]

for i in range(1526):
    st=datasetCO.iloc[i,0]
    lis=[]
    lis=st.split('T')
    lis=lis[0].split('2018')
    st=lis[1]
    st=st+'-'
    lis=list(st)
    st=''
    lis[4]=lis[3]
    lis[3]=lis[2]
    lis[2]='-'
    st=st.join(lis)
    datasetCO.iloc[i,0]=st

for i in range(2918):
    st=datasetNO2.iloc[i,0]
    lis=[]
    lis=st.split('T')
    lis=lis[0].split('2018')
    st=lis[1]
    st=st+'-'
    lis=list(st)
    st=''
    lis[4]=lis[3]
    lis[3]=lis[2]
    lis[2]='-'
    st=st.join(lis)
    datasetNO2.iloc[i,0]=st
    
for i in range(4176):
    st=datasetTemp.iloc[i,0]
    lis=[]
    lis=st.split('_')
    lis=lis[0].split('2018')
    st=lis[1]
    st=st+'-'
    lis=list(st)
    st=''
    lis[4]=lis[3]
    lis[3]=lis[2]
    lis[2]='-'
    st=st.join(lis)
    datasetTemp.iloc[i,0]=st
    
for i in range(33408):
    st=datasetWind.iloc[i,0]
    lis=[]
    lis=st.split('A')
    lis=lis[1].split('_')
    lis=lis[0].split('2018')
    st=lis[1]
    st=st+'-'
    lis=list(st)
    st=''
    lis[4]=lis[3]
    lis[3]=lis[2]
    lis[2]='-'
    st=st.join(lis)
    datasetWind.iloc[i,0]=st

for i in range(19346):
    st=datasetCOD.iloc[i,0]
    lis=[]
    lis=st.split('T')
    lis=lis[0].split('2018')
    st=lis[1]
    st=st+'-'
    lis=list(st)
    st=''
    lis[4]=lis[3]
    lis[3]=lis[2]
    lis[2]='-'
    st=st.join(lis)
    datasetCOD.iloc[i,0]=st
    
for i in range(37349):
    st=datasetNOD.iloc[i,0]
    lis=[]
    lis=st.split('T')
    lis=lis[0].split('2018')
    st=lis[1]
    st=st+'-'
    lis=list(st)
    st=''
    lis[4]=lis[3]
    lis[3]=lis[2]
    lis[2]='-'
    st=st.join(lis)
    datasetNOD.iloc[i,0]=st
    
    
datasetNOD=datasetNOD.iloc[:,[0,7]]
datasetRain=datasetRain.iloc[:,[0,11]]
datasetTemp=datasetTemp.iloc[:,[0,11]] 
datasetWind=datasetWind.iloc[:,[0,11]] 
datasetCOD=datasetCOD.iloc[:,[0,5]]

#Mean calculation for independant CO

prev=''
indexes=[]
for i in range(1526):
    if prev==datasetCO.iloc[i,0] or prev=='':
        prev=datasetCO.iloc[i,0]
    else:
        indexes.append(i-1)
        prev=datasetCO.iloc[i,0]
indexes.append(i)

s=np.array(datasetCO.iloc[:,1])
mean_vals=[]
prev=0
for i in indexes:
    mean_vals.append(np.mean(s[prev:i+1]))
    prev=i+1
date=[]
for i in range(len(indexes)):
    k=indexes[i]
    date.append(datasetCO.iloc[k,0])
    
date=np.array(date)
date=date.reshape(len(date),1)
mean_vals=np.array(mean_vals)
mean_vals=mean_vals.reshape(len(mean_vals),1)

#Mean calculation for independant NO2

prev=''
indexes=[]
for i in range(2918):
    if prev==datasetNO2.iloc[i,0] or prev=='':
        prev=datasetNO2.iloc[i,0]
    else:
        indexes.append(i-1)
        prev=datasetNO2.iloc[i,0]
indexes.append(i)

s=np.array(datasetNO2.iloc[:,1])
mean_vals=[]
prev=0
for i in indexes:
    mean_vals.append(np.mean(s[prev:i+1]))
    prev=i+1
date=[]
for i in range(len(indexes)):
    k=indexes[i]
    date.append(datasetNO2.iloc[k,0])
    
date=np.array(date)
date=date.reshape(len(date),1)
mean_vals=np.array(mean_vals)
mean_vals=mean_vals.reshape(len(mean_vals),1)

#Mean calculation for independant Rain

prev=''
indexes=[]
for i in range(4176):
    if prev==datasetRain.iloc[i,0] or prev=='':
        prev=datasetRain.iloc[i,0]
    else:
        indexes.append(i-1)
        prev=datasetRain.iloc[i,0]
indexes.append(i)

s=np.array(datasetRain.iloc[:,1])
mean_vals=[]
prev=0
for i in indexes:
    mean_vals.append(np.mean(s[prev:i+1]))
    prev=i+1
date=[]
for i in range(len(indexes)):
    k=indexes[i]
    date.append(datasetRain.iloc[k,0])
    
date=np.array(date)
date=date.reshape(len(date),1)
mean_vals=np.array(mean_vals)
mean_vals=mean_vals.reshape(len(mean_vals),1)

#Mean calculation for independant Wind

prev=''
indexes=[]
for i in range(33408):
    if prev==datasetWind.iloc[i,0] or prev=='':
        prev=datasetWind.iloc[i,0]
    else:
        indexes.append(i-1)
        prev=datasetWind.iloc[i,0]
indexes.append(i)

s=np.array(datasetWind.iloc[:,1])
mean_vals=[]
prev=0
for i in indexes:
    mean_vals.append(np.mean(s[prev:i+1]))
    prev=i+1
date=[]
for i in range(len(indexes)):
    k=indexes[i]
    date.append(datasetWind.iloc[k,0])
    
date=np.array(date)
date=date.reshape(len(date),1)
mean_vals=np.array(mean_vals)
mean_vals=mean_vals.reshape(len(mean_vals),1)

#Mean calculation for independant Temp

prev=''
indexes=[]
for i in range(4176):
    if prev==datasetTemp.iloc[i,0] or prev=='':
        prev=datasetTemp.iloc[i,0]
    else:
        indexes.append(i-1)
        prev=datasetTemp.iloc[i,0]
indexes.append(i)

s=np.array(datasetTemp.iloc[:,1])
mean_vals=[]
prev=0
for i in indexes:
    mean_vals.append(np.mean(s[prev:i+1]))
    prev=i+1
date=[]
for i in range(len(indexes)):
    k=indexes[i]
    date.append(datasetTemp.iloc[k,0])
    
date=np.array(date)
date=date.reshape(len(date),1)
mean_vals=np.array(mean_vals)
mean_vals=mean_vals.reshape(len(mean_vals),1)

#Mean calculation for dependant CO

prev=''
indexes=[]
for i in range(19346):
    if prev==datasetCOD.iloc[i,0] or prev=='':
        prev=datasetCOD.iloc[i,0]
    else:
        indexes.append(i-1)
        prev=datasetCOD.iloc[i,0]
indexes.append(i)

s=np.array(datasetCOD.iloc[:,1])
mean_vals=[]
prev=0
for i in indexes:
    mean_vals.append(np.mean(s[prev:i+1]))
    prev=i+1
date=[]
for i in range(len(indexes)):
    k=indexes[i]
    date.append(datasetCOD.iloc[k,0])
    
date=np.array(date)
date=date.reshape(len(date),1)
mean_vals=np.array(mean_vals)
mean_vals=mean_vals.reshape(len(mean_vals),1)

#Mean calculation for dependant NO

prev=''
indexes=[]
for i in range(37349):
    if prev==datasetNOD.iloc[i,0] or prev=='':
        prev=datasetNOD.iloc[i,0]
    else:
        indexes.append(i-1)
        prev=datasetNOD.iloc[i,0]
indexes.append(i)

s=np.array(datasetNOD.iloc[:,1])
mean_vals=[]
prev=0
for i in indexes:
    mean_vals.append(np.mean(s[prev:i+1]))
    prev=i+1
date=[]
for i in range(len(indexes)):
    k=indexes[i]
    date.append(datasetNOD.iloc[k,0])
    
date=np.array(date)
date=date.reshape(len(date),1)
mean_vals=np.array(mean_vals)
mean_vals=mean_vals.reshape(len(mean_vals),1)
