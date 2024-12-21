# -*- coding: utf-8 -*-
"""Bank customer Churn Predication.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1qrjSQ8FZ5Lq4Q3OJmGz7GgVyCQ0YTE0i
"""

import numpy as np # linear algebra
import pandas as pd
import seaborn as sns
import sklearn as sk
import matplotlib.pyplot as plt

df = pd.read_csv('Churn_Modelling.csv')

df.head()

df.tail()

df.shape

df.info()

df.isnull().sum()

df.describe()

df.drop(columns=['RowNumber','CustomerId','Surname'],inplace=True,axis=1)

df.head()

df['Geography'].value_counts()

df['Gender'].value_counts()

df = pd.get_dummies(df,drop_first=True)

df.head()

df['Geography_Germany'].replace({False:0,True:1},inplace=True)
df['Geography_Spain'].replace({False:0,True:1},inplace=True)
df['Gender_Male'].replace({False:0,True:1},inplace=True)

df.head()

df.info()

df['Exited'].value_counts()

sns.countplot(data=df,x=df['Exited'])

X = df.drop(['Exited'],axis=1)

y = df['Exited']

X.head()

y.head()

"""Handling Imbalanced Data with SMOTE(Synthetic Minority Oversampling TEchnique)"""

from imblearn.over_sampling import SMOTE

X_new, y_new = SMOTE().fit_resample(X,y)

X.shape, y.shape, X_new.shape, y_new.shape

y.value_counts()

y_new.value_counts()

# splitting the data into train and test set

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X_new,y_new,test_size=0.2,random_state=42)

X_train.shape,X_test.shape,y_train.shape,y_test.shape

y_train.value_counts()

y_test.value_counts()

# Feature Scaling
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

X_train

"""1. Logistic Regression Model"""

from sklearn.linear_model import LogisticRegression

lr_model = LogisticRegression()

lr_model.fit(X_train, y_train)

y_pred_lr = lr_model.predict(X_test)

from sklearn.metrics import accuracy_score

accuracy_score(y_test,y_pred_lr)

from sklearn.metrics import precision_score, recall_score, f1_score

as_lr = accuracy_score(y_test,y_pred_lr)
ps_lr = precision_score(y_test,y_pred_lr)
rs_lr = recall_score(y_test,y_pred_lr)
f1_lr = f1_score(y_test,y_pred_lr)

print('Accuracy Score using Logistic Regression:',as_lr)

print('Precision Score using Logistic Regression:',ps_lr)

print('Recall Score using Logistic Regression:',rs_lr)

print('F1 Score using Logistic Regression:',f1_lr)

"""2. Support Vector Classifier (SVC) Model"""

from sklearn import svm

svc_model = svm.SVC()
svc_model.fit(X_train, y_train)

y_pred_svc = svc_model.predict(X_test)

as_svc = accuracy_score(y_test,y_pred_svc)
ps_svc = precision_score(y_test,y_pred_svc)
rs_svc = recall_score(y_test,y_pred_svc)
f1_svc = f1_score(y_test,y_pred_svc)

print('Accuracy Score using SVC:',as_svc)

print('Precision Score using SVC:',ps_svc)

print('Recall Score using SVC:',rs_svc)

print('F1 Score using SVC:',f1_svc)

"""3. KNeighbors Classifier Mode"""

from sklearn.neighbors import KNeighborsClassifier

model_knn = KNeighborsClassifier()
model_knn.fit(X_train, y_train)
y_pred_knn = model_knn.predict(X_test)

as_knn = accuracy_score(y_test,y_pred_knn)
ps_knn = precision_score(y_test,y_pred_knn)
rs_knn = recall_score(y_test,y_pred_knn)
f1_knn = f1_score(y_test,y_pred_knn)

print('Accuracy Score using KNN:',as_knn)

print('Precision Score using KNN:',ps_knn)

print('Recall Score using KNN:',rs_knn)

print('F1 Score using KNN:',f1_knn)

"""4. Decision Tree Classifier Model"""

from sklearn.tree import DecisionTreeClassifier

model_tree = DecisionTreeClassifier()

model_tree.fit(X_train,y_train)

y_pred_tree = model_tree.predict(X_test)

as_tree = accuracy_score(y_test,y_pred_tree)
ps_tree = precision_score(y_test,y_pred_tree)
rs_tree = recall_score(y_test,y_pred_tree)
f1_tree = f1_score(y_test,y_pred_tree)

print('Accuracy Score using Decision Tree:',as_tree)

print('Precision Score using Decision Tree:',ps_tree)

print('Recall Score using Decision Tree:',rs_tree)

print('F1 Score using Decision Tree:',f1_tree)

"""5. Random Forest Classifier Model"""

from sklearn.ensemble import RandomForestClassifier

model_rf = RandomForestClassifier()

model_rf.fit(X_train, y_train)

y_pred_rf = model_rf.predict(X_test)

as_rf = accuracy_score(y_test,y_pred_rf)
ps_rf = precision_score(y_test,y_pred_rf)
rs_rf = recall_score(y_test,y_pred_rf)
f1_rf = f1_score(y_test,y_pred_rf)

print('Accuracy Score using Random Forest:',as_rf)

print('Precision Score using Random Forest:',ps_rf)

print('Recall Score using Random Forest:',rs_rf)

print('F1 Score using Random Forest:',f1_rf)

"""6. Gradient Boosting Classifier Model"""

from sklearn.ensemble import GradientBoostingClassifier

model_gb = GradientBoostingClassifier()

model_gb.fit(X_train,y_train)

y_pred_gb = model_gb.predict(X_test)

as_gb = accuracy_score(y_test,y_pred_gb)
ps_gb = precision_score(y_test,y_pred_gb)
rs_gb = recall_score(y_test,y_pred_gb)
f1_gb = f1_score(y_test,y_pred_gb)

print('Accuracy Score using Gradient Boosting:',as_gb)

print('Precision Score using Gradient Boosting:',ps_gb)

print('Recall Score using Gradient Boosting:',rs_gb)

print('F1 Score using Gradient Boosting:',f1_gb)

"""7. XGBoost Classifier Model"""

from xgboost import XGBClassifier

model_xgb = XGBClassifier()

model_xgb.fit(X_train,y_train)

y_pred_xgb = model_xgb.predict(X_test)

as_xgb = accuracy_score(y_test,y_pred_xgb)
ps_xgb = precision_score(y_test,y_pred_xgb)
rs_xgb = recall_score(y_test,y_pred_xgb)
f1_xgb = f1_score(y_test,y_pred_xgb)

print('Accuracy Score using XGBoost:',as_xgb)

print('Precision Score using XGBoost:',ps_xgb)

print('Recall Score using XGBoost:',rs_xgb)

print('F1 Score using XGBoost:',f1_xgb)

"""Visualise all the Models"""

model_df = pd.DataFrame(
    {'Models':
         ['Logistic Regression','Support Vector Classifier',
          'KNN', 'Decision Tree','Random Forest',
          'Gradient Boosting','XGBoost'],
     'Accuracy Score':
         [as_lr,as_svc,
          as_knn,as_tree,as_rf,
          as_gb, as_xgb],
     'Precision Score':
         [ps_lr,ps_svc,
          ps_knn,ps_tree,ps_rf,
          ps_gb, ps_xgb],
     'Recall Score':
         [rs_lr,rs_svc,
          rs_knn,rs_tree,rs_rf,
          rs_gb, rs_xgb],
     'F1 Score':
         [f1_lr,f1_svc,
          f1_knn,f1_tree,f1_rf,
          f1_gb, f1_xgb],

    })

model_df

# Visualising F1 Score for each model
plt.figure(figsize=(6,6))
model_plot = sns.barplot(data=model_df,y=model_df['Models'],x=model_df['F1 Score'],hue=model_df['Models'])

import joblib

joblib.dump(model_rf,'churn_predict_model')
