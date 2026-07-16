#!/usr/bin/env python
# coding: utf-8

# In[38]:


get_ipython().system('pip install pandas')
get_ipython().system('pip install matplotlib')
get_ipython().system('pip install joblib')


# In[4]:


#IMPORT LIBRARIES 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import joblib
from imblearn.over_sampling import SMOTE


# In[5]:


#LOAD DATASET 

data = pd.read_csv("credit_card_fraud_dataset.csv")

print(data.head())

print(data.shape)

print(data.columns)


# In[6]:


#EXPLORE DATA (EDA)

print(data.info())

print(data.describe())

print(data.isnone().sum())

print(data["IsFraud"].value_counts())


# In[7]:


#VISUALIZATION

data["IsFraud"].value_counts().plot(kind="bar", color=["blue","red"],figsize=(6,4))

plt.title("Fraud vs Genuine Transactions")
plt.xlabel("IsFraud")
plt.ylabel("Count")
plt.show()


# In[8]:


import matplotlib.pyplot as plt

data["IsFraud"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%",
    figsize=(4,4)
)

plt.title("Fraud vs Genuine Transactions")
plt.ylabel("")
plt.show()


# In[9]:


plt.figure(figsize=(6,4))

plt.scatter(data["Amount"], data["MerchantID"])

plt.xlabel("Amount")
plt.ylabel("MerchantID")
plt.title("Amount vs MerchantID")

plt.show()


# In[11]:


plt.figure(figsize=(6,4))

plt.hist(data["Amount"], bins=20)

plt.xlabel("Amount")
plt.ylabel("Frequency")
plt.title("Transaction Amount Distribution")

plt.show()


# In[12]:


plt.figure(figsize=(6,3))
correlation = data.select_dtypes(include="number").corr()

plt.imshow(correlation, cmap="coolwarm")
plt.colorbar()
plt.xticks(range(len(correlation.columns)), correlation.columns, rotation=90)
plt.yticks(range(len(correlation.columns)), correlation.columns)
plt.title("Correlation Heatmap")

plt.show()


# In[13]:


#DATA CLEANING

print("Duplicate Rows:", data.duplicated().sum())

data = data.drop_duplicates()

data = data.dropna()


# In[14]:


#FEATURE ENGINEERING

# Convert TransactionDate only if it exists
if "TransactionDate" in data.columns:
    data["TransactionDate"] = pd.to_datetime(data["TransactionDate"])

    data["Year"] = data["TransactionDate"].dt.year
    data["Month"] = data["TransactionDate"].dt.month
    data["Day"] = data["TransactionDate"].dt.day

    data.drop("TransactionDate", axis=1, inplace=True)

#ENCODE TEXT COLUMN 
le = LabelEncoder()

if "TransactionType" in data.columns:
    data["TransactionType"] = le.fit_transform(data["TransactionType"])

if "Location" in data.columns:
    data["Location"] = le.fit_transform(data["Location"])

print(data.head())


# In[15]:


#FEATURE SELECTION

X = data.drop("IsFraud", axis=1)
y = data["IsFraud"]


# In[16]:


#TRAIN-TEST SPLIT

X_train, X_test, y_train, y_test = train_test_split(
X,
y,
test_size=0.20,
random_state=42
)


# In[17]:


smote=SMOTE(random_state=42)
X_train_smote,y_train_smote=smote.fit_resample(X_train,y_train)
print(y_train_smote.value_counts())
model.fit(X_train_smote,y_train_smote)
grid.fit(X_train_smote,y_train_smote)


# In[18]:


print(X_train.dtypes)


# In[19]:


print(X_train.select_dtypes(include=['object']).columns)


# In[20]:


# Feature Scaling
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

print("Feature Scaling Completed Successfully!")


# In[21]:


#TRAIN MODEL

model = LogisticRegression(max_iter=1000)

model.fit(X_train, y_train)


# In[22]:


#MODEL EVALUTION

prediction = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, prediction))
print(confusion_matrix(y_test, prediction))
print(classification_report(y_test, prediction, zero_division=0))


# In[23]:


train_acc = model.score(X_train, y_train)
test_acc = model.score(X_test, y_test)

print("Training Accuracy:", train_acc)
print("Testing Accuracy:", test_acc)


# In[24]:


#HYPERPARAMETER TUNING

parameters = {

"C":[0.1,1,10],
"solver":["lbfgs"]
}

grid = GridSearchCV(
model,
parameters,
cv=3
)

grid.fit(X_train, y_train)

print(grid.best_params_)


# In[25]:


#SAVE MODEL

joblib.dump(grid.best_estimator_,"Fraud_Model.pkl")

print("Model Saved Successfully")


# In[26]:


#PREDICTION

sample = X_test[0].reshape(1, -1)

result = grid.predict(sample)

if result[0] == 1:
    print("Fraud Transaction")
else:
    print("Genuine Transaction")


# In[27]:


import joblib

joblib.dump(model, "model.pkl")


# In[28]:


from sklearn.ensemble import RandomForestClassifier
import joblib

# Create Model
model = RandomForestClassifier(n_estimators=100, random_state=42)

# Train Model
model.fit(X_train_smote, y_train_smote)

# Save Model
joblib.dump(model, "model.pkl")

print("Model trained and saved successfully!")


# In[30]:


import os

print(os.listdir())


# In[31]:


import os

if os.path.exists("credit_card_fraud_model.pkl"):
    print("✅ Model file exists")
else:
    print("❌ Model file not found")


# In[32]:


import os

print(os.getcwd())


# In[34]:


print(data.columns)


# In[35]:


print(data.dtypes)


# In[36]:


import json

json_string = '{"id": 101, "description": none}'
data = json.loads(json_string) 


