# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 17:31:40 2020

@author: Sujay
"""

import pandas as pd
import ruptures as rpt
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv('ndvi_time_all_points.csv')
'''
dataset = pd.read_csv('ndvi_time_final.csv')
X = dataset.iloc[:,1:-8]'''

X = dataset.iloc[:,2:-7]

arr = []

for j in range(X.shape[1]):
    day = X.loc[X.iloc[:,j] >   0]

    value = day.iloc[:,j].mean()
    if value>0:
        arr.append(value)

#Changepoint detection with the Pelt search method    
signal = np.array(arr)
algo = rpt.Pelt(model="rbf").fit(signal)
result = algo.predict(pen =10)
rpt.display(signal, result)
plt.title('Change Point Detection: Pelt Search Method')
plt.show()

#Changepoint detection with the Binary Segmentation search method
model = "l2"  
algo = rpt.Binseg(model=model).fit(signal)
my_bkps = algo.predict(n_bkps=10)
# show results
rpt.show.display(signal, my_bkps)
plt.title('Change Point Detection: Binary Segmentation Search Method')
plt.show()

#Changepoint detection with window-based search method
model = "l2"  
algo = rpt.Window(width=40, model=model).fit(signal)
my_bkps = algo.predict(n_bkps=10)
rpt.show.display(signal, my_bkps )
plt.title('Change Point Detection: Window-Based Search Method')
plt.show()

#Changepoint detection with dynamic programming search method
model = "l1"  
algo = rpt.Dynp(model=model, min_size=3, jump=5).fit(signal)
my_bkps = algo.predict(n_bkps=10)
rpt.show.display(signal, my_bkps)
plt.title('Change Point Detection: Dynamic Programming Search Method')
plt.show()