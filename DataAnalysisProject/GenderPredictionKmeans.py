import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np
import pyodbc
from sklearn.preprocessing import LabelEncoder
from scipy.stats import iqr
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.cluster import KMeans
from datetime import datetime
from tabulate import tabulate
from kneed import KneeLocator

sql_conn = pyodbc.connect('DRIVER={SQL Server}; SERVER=DESKTOP-DRPFO66\PETER;DATABASE=AdventureWorksDB;Trusted_Connection=yes')                     
query = "SELECT * FROM CustomerFeatures"
df = pd.read_sql(query, sql_conn)

print('got data from sql server')

le = LabelEncoder()

#Transform categorical data into numerical data
df['city2'] = le.fit_transform(df['city'])
df['gender2']=le.fit_transform(df['gender'])
df['MaritalStatus2']=le.fit_transform(df['MaritalStatus'])

print('transformed data into numeric data')

data_test = df[["MaritalStatus2"]]
data = df[["NumberofOrders", "HouseOwnerFlag", "SalesAmt","Age","NumberItems","city2","YearlyIncome","TotalChildren","gender2"]]


#Scaling of the data
#scale2=MinMaxScaler(feature_range=(0, 15))
#scale2.fit(data_test)
#data_test=pd.DataFrame(scale2.transform(data_test),columns = data_test.columns)

scale=StandardScaler()
scale.fit(data)
dff = pd.DataFrame(scale.transform(data),columns = data.columns)

print('scaled data')

#Create cluster labels
clustering1=KMeans(n_clusters=2)
clustering1.fit(dff)
KMeans()
dff['Clusterlabel']=clustering1.labels_

print('have created cluster labels')
#print(dff.head())
#print(data_gender.head())
#join cluster label dataframe to original 
joined= pd.concat([dff['Clusterlabel'], data_test], axis=1).reindex(dff.index)
#print(joined.head())

print('have joined the two dataframes together')

joined['Correct']= np.where(joined['Clusterlabel']==joined['MaritalStatus2'],1,0)

print('have created the boolean column correct')

print(joined['Correct'].sum()/len(joined))
print(joined['Correct'].sum())
print(len(joined))
