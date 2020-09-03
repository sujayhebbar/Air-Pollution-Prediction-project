# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 16:11:31 2020

@author: Sujay
"""

# example of evaluating chained multioutput regression with an SVM model
from numpy import mean
from numpy import std
from numpy import absolute
import pandas as pd
from math import sqrt
from sklearn.multioutput import RegressorChain
from sklearn.svm import LinearSVR

dataset = pd.read_csv('DatasetFinal.csv')
#dataset = dataset.dropna(thresh = 13)
#dataset = dataset.drop(columns = 'NO2_CND')

dataset = dataset.drop(columns = ['CO_CND','CO-Delhi1','CO-Delhi2','CO-Delhi3','CO-Delhi4','CO-Delhi5'])
#dataset = dataset.iloc[:,:-5]
# Taking care of missing data
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values='NaN',strategy='mean')
#imputer = imputer.fit(dataset)
dataset_r8 = imputer.fit_transform(dataset)


from sklearn.preprocessing import MinMaxScaler
sc_X = MinMaxScaler();
dataset_r8= sc_X.fit_transform(dataset_r8) 
dataset_r8 = pd.DataFrame(dataset_r8)
X = dataset_r8.iloc[:,:4]
y = dataset_r8.iloc[:,4:]

# define base model
model = LinearSVR(max_iter = 5000)
#model = LinearRegression()
# define the chained multioutput wrapper model
wrapper = RegressorChain(model)
# fit the model on the whole dataset
#wrapper.fit(X, y)
# make a single prediction
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.1, random_state = 1)

# fit model
wrapper.fit(X_train, y_train)

y_pred = wrapper.predict(X_test)
from sklearn.metrics import mean_squared_error
rmse = (mean_squared_error( y_true = y_test, y_pred = y_pred, multioutput = 'raw_values'))
for i in rmse:
    print(sqrt(i))
