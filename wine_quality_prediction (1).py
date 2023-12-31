# -*- coding: utf-8 -*-
"""wine quality prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15KnFmDDE3jIsEz1vHoLi8Hf7M02kBKjT
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression

wine=pd.read_csv("WineQT.csv")
wine

wine.info()

wine.columns

sns.histplot(wine['quality'], color = 'red')
plt.show

sns.distplot(wine['quality'])

co_matrix = wine[['chlorides', 'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol', 'quality']].corr()
sns.heatmap(co_matrix,annot = True, cmap = 'coolwarm')
plt.title('Correlation Matrix')
plt.show

sns.pairplot(wine, x_vars = ['chlorides', 'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol', 'quality'],
          y_vars = 'quality', kind = 'scatter')
plt.show

X=wine.drop('quality',axis=1)
y=wine['quality']

print("Shape of X= ",X.shape)
print("Shape of y= ",y.shape)

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=51)

# Feature Scaling
sc=StandardScaler()
sc.fit(X_train)
X_train=sc.transform(X_train)
X_test=sc.transform(X_test)

lir=LinearRegression()
lir.fit(X_train,y_train)

lir.coef_

lir.intercept_

wine_quality=[7.8,0.760,0.04,2.3,0.092,15.0,54.0,0.99700,3.26,0.65,9.8,2]

wine_quality=np.array([wine_quality])
wine_quality

pred=lir.predict(wine_quality)
pred





