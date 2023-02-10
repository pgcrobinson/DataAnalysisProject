import numpy as np
import pandas as pd
import pyodbc
from sklearn import preprocessing, neighbors
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

sql_conn = pyodbc.connect('DRIVER={SQL Server}; SERVER=DESKTOP-DRPFO66\PETER;DATABASE=TableauData;Trusted_Connection=yes')                     
query = "SELECT top 10000* FROM PropertyPrices"
df = pd.read_sql(query, sql_conn)

le = LabelEncoder()

df =df.drop(columns=['TransactionID','PPD','Record_Status'])
#Transform categorical data into numerical data

df=df.apply(LabelEncoder().fit_transform)

print(df.head())
#df['city2'] = le.fit_transform(df['city'])
#df['gender2']=le.fit_transform(df['gender'])
#df['MaritalStatus2']=le.fit_transform(df['MaritalStatus'])

X = np.array(df.drop(['Old_New'], 1))
y = np.array(df['Old_New'])

#X =np.array(df[["NumberofOrders", "HouseOwnerFlag", "Age","NumberItems","city2","SalesAmt","YearlyIncome","TotalChildren","gender2"]])
#y = np.array(df[["MaritalStatus2"]])


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15)

clf = neighbors.KNeighborsClassifier()
clf.fit(X_train, y_train)
accuracy = clf.score(X_test, y_test)
print(accuracy)
