# -*- coding: utf-8 -*-
"""multilinearRegression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OSTS53kURF8OctaWn6l88Wlur2FKP2sp
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

veriler = pd.read_csv('/content/veriler.csv')

ulke = veriler.iloc[:,0:1].values

sayisalVeriler = veriler.iloc[:, 1:4]

c = veriler.iloc[:, 4:5].values
c

from sklearn import preprocessing

le = preprocessing.LabelEncoder()

c[:, 0] = le.fit_transform(veriler.iloc[:, -1])

ulke[:, 0] = le.fit_transform(veriler.iloc[:, 0:1])

ohe = preprocessing.OneHotEncoder()

c = ohe.fit_transform(c).toarray()

ulke = ohe.fit_transform(ulke).toarray()

sonuc1 = pd.DataFrame(data=ulke, index=range(len(ulke)), columns=['fr', 'tr', 'us'])

sonuc2 = pd.DataFrame(data=sayisalVeriler, index=range(len(sayisalVeriler)), columns= ['boy', 'kilo', 'yas'])

sCin = pd.DataFrame(data=c[:, 0:1], index = range(len(c[:, 0:1])), columns = ['Cinsiyet'])

s1 = pd.concat([sonuc1, sonuc2], axis=1) # satir satira birlestirmek icin yani yatay boyutta birlestirmek icin axis = 1

s2 = pd.concat([s1, sCin], axis=1)

s2

from sklearn.model_selection import train_test_split

# verinin yuzde 66 si antrenman icin kullanilsin kalan yuzde 33'u test edilsin diye ayrdik
# random_state rastsal ayirma icin kullaniliyor ayni degeri alan her kod ayni ayrimi yapar
x_train, x_test, y_train, y_test = train_test_split(s1, sCin, test_size = 0.33, random_state = 0)

x_train

y_train

x_test

y_test

from sklearn.linear_model import LinearRegression

multile = LinearRegression()

multile.fit(x_train, y_train)

y_predict = multile.predict(x_test)

y_test.values

y_predict

boy = s2.iloc[:, 3:4].values

sol = s2.iloc[:,:3]

sag = s2.iloc[:,4:]

yeniVeriler = pd.concat([sol, sag], axis = 1)

yeniVeriler

x_train, x_test, y_train, y_test = train_test_split(yeniVeriler, boy, test_size = 0.33, random_state = 0)

multile2 = LinearRegression()

multile2.fit(x_train, y_train)

y_predict2 = multile2.predict(x_test)

y_predict2

y_test

"""Multilineer regresyoda ki B0 degerini 1 olarak ```yeniVerilerin``` basina ekledik. Bunuda ```X```'e attik."""

X = np.append(arr = np.ones((22,1)).astype(int), values = yeniVeriler, axis = 1)

X

"""# Backward Elimination Algorithm


> Bu algoritma oneNotaki notalara bakarak nalasilabilir.

> Kisaca OLS raporundan aldigimiz olasik degerlerine bakarak ve Backward Elimination algoritmasina dayanarak 0.05 aldigimiz P degerinden yuksek degerleri sirasiyla kontrol ederek eliyoruz ta ki P < 0.05 olana kadar.


> Burada boy bagimli degisken ve bagimsiz degiskenleri ```yeniVeriler``` tablosundan cekip 0.05 den buyuk olanlari eledik.
"""

import statsmodels.api as sm

X_1 = yeniVeriler.iloc[:, [0, 1, 2, 3, 4, 5]].values

X_1 = np.array(X_1, dtype = float)

model = sm.OLS(boy, X_1).fit()

model.summary()

X_1 = yeniVeriler.iloc[:, [0, 1, 2, 3, 5]].values

X_1 = np.array(X_1, dtype = float)

model = sm.OLS(boy, X_1).fit()

model.summary()

X_1 = yeniVeriler.iloc[:, [0, 1, 2, 3]].values

X_1 = np.array(X_1, dtype = float)

model = sm.OLS(boy, X_1).fit()

model.summary()
