# -*- coding: utf-8 -*-
"""SuppotVectorMachine.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1D2zZSCcIjUwlW3hztd_AhTN4OcBgU8Mw

DIKKAT ET !!! AYKIRI VERIELRE COK HASSASTIR OL
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

veriler = pd.read_csv('/content/maaslar.csv')

X = veriler.iloc[:, [1]]
Y = veriler.iloc[:, [2]]
# NUMPY ARRAY DIZI DONUSUMU
x = X.values
y = Y.values

from sklearn.preprocessing import StandardScaler

sc1 = StandardScaler()
x_olcekli = sc1.fit_transform(X)
sc2 = StandardScaler()
y_olcekli = sc2.fit_transform(Y)

from sklearn.svm import SVR

svrReg = SVR(kernel = 'rbf')
svrReg.fit(x_olcekli, y_olcekli)

plt.scatter(x_olcekli, y_olcekli, c = 'r')
plt.plot(x_olcekli, svrReg.predict(x_olcekli), c = 'b')
plt.show()

svrReg.predict([[11]])
