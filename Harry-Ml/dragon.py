# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 17:44:44 2021

@author: dell
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.model_selection import StratifiedShuffleSplit
from pandas.plotting import scatter_matrix
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import cross_val_score
from joblib import dump,load




housing=pd.read_csv('data.csv')
print(housing.head())#Top 5 rows

housing.hist(bins=50,figsize=(20,15))

#housing.plot(kind='bar')
#plt.show()


#Train test split for learning purpose
def split_train_test(data,test_ratio):
    np.random.seed(42)
    shuffled=np.random.permutation(len(data))#shuffle data  on random permutation
    #print(shuffled)
    test_set_size = int(len(data)*test_ratio)
    test_indices=shuffled[:test_set_size]
    train_indices=shuffled[test_set_size:]
    return data.iloc[train_indices],data.iloc[test_indices]

train_set,test_set=split_train_test(housing,0.2)
print(f"Rows in train set: {len(train_set)}\nRows in test set: {len(test_set)}")

#Train test split for by scikit learn

train_set,test_set=train_test_split(housing,test_size=0.2,random_state=42)
print(f"Rows in train set: {len(train_set)}\nRows in test set: {len(test_set)}")



split = StratifiedShuffleSplit(n_splits=1,test_size=0.2,random_state=42)
for train_index,test_index in split.split(housing,housing['CHAS']):
    strat_train_set=housing.loc[train_index]
    strat_test_set=housing.loc[test_index]
    
    
print(strat_test_set['CHAS'].value_counts())
print(strat_train_set['CHAS'].value_counts())

housing=strat_train_set.copy()#imputer and every subsequent operation on tarining data



#Looking for correlation
corr_matrix=housing.corr()
print(corr_matrix['MEDV'].sort_values(ascending=False))#correlation of MEDV with other columns

attributes=['MEDV','RM','ZN','LSTAT']
scatter_matrix(housing[attributes],figsize=(12,8))
housing.plot(kind="scatter",x="RM",y="MEDV",alpha=0.8)


housing['TAXRM']=housing['TAX']/housing['RM']#tax per room
print(housing.head())

housing.plot(kind="scatter",x="TAXRM",y="MEDV",alpha=0.8)

housing = strat_train_set.drop("MEDV",axis=1)
#removed taxrm new fature while training model otherwise it would harm model
housing_labels = strat_train_set["MEDV"].copy()

#option3
median=housing["RM"].median()
median
housing["RM"].fillna(median)
#original housing dataframe will remain unchanged
#found meadian of training set we have to fit in test set coz that can also contain some missing value
imputer=SimpleImputer(strategy="median")
imputer.fit(housing)
print(imputer.statistics_)

x=imputer.transform(housing)#transform any numerical column missing value with median
housing_tr=pd.DataFrame(x,columns=housing.columns)


#pipeine will also include imputer so apply pipe on originala df which
#you gave to separate imputer code ,no nedd to define imputer seperately
#dont pass medv


my_pipeline=Pipeline([
    ('imputer', SimpleImputer(strategy="median")),
     #add as many as uou want in your pipeline
     ('std_scaler',StandardScaler()),
])

housing_num_tr=my_pipeline.fit_transform(housing)
print(housing_num_tr)


def print_scores(scores):
    print("scores",scores)
    print("mean",scores.mean())
    print("std dev",scores.std())

model = RandomForestRegressor()
model.fit(housing_num_tr,housing_labels)
some_data=housing.iloc[:5]
some_labels=housing.iloc[:5]
prepared_data=my_pipeline.transform(some_data)
model.predict(prepared_data)
housing_predictions = model.predict(housing_num_tr)
lin_mse = mean_squared_error(housing_labels,housing_predictions)
lin_rmse = np.sqrt(lin_mse)


scores = cross_val_score(model,housing_num_tr,housing_labels,scoring="neg_mean_squared_error",cv=10)
rmse_scores=np.sqrt(-scores)

print_scores(rmse_scores)#score of RandomForestClassifier


dump(model,'Dragon.joblib')

#testing model on test data
x_test=strat_test_set.drop("MEDV",axis=1)
y_test=strat_test_set["MEDV"].copy()
x_test_prepared_data=my_pipeline.transform(x_test)
final_prediction=model.predict(x_test_prepared_data)
mse = mean_squared_error(y_test,final_prediction)
rmse = np.sqrt(mse)
rmse
print(list(final_prediction),list(y_test))