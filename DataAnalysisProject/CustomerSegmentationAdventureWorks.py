import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np
import pyodbc
from sklearn.preprocessing import LabelEncoder
from scipy.stats import iqr
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from datetime import datetime
from tabulate import tabulate
from kneed import KneeLocator

sql_conn = pyodbc.connect('DRIVER={SQL Server}; SERVER=DESKTOP-DRPFO66\PETER;DATABASE=AdventureWorksDB;Trusted_Connection=yes')                     
query = "SELECT * FROM CustomerFeatures"
df = pd.read_sql(query, sql_conn)

#df=df[["gender", "city"]]

le = LabelEncoder()
le = LabelEncoder()
#encoded_series = df[df.columns[:]].apply(le.fit_transform)
df['city2'] = le.fit_transform(df['city'])
df['gender2']=le.fit_transform(df['gender'])

#print(df)
#print(df.columns.values)



data = df[["NumberofOrders", "YearlyIncome", "SalesAmt","Age","NumberItems","city2","gender2","gender","city"]]
data1 = df[["NumberofOrders", "YearlyIncome", "SalesAmt","Age","NumberItems","city2","gender2"]]
#sns.pairplot(data, hue="gender2")
#plt.show()#data=df[["NumberofOrders", "YearlyIncome", "SalesAmt","Age","NumberItems",'gender2',"city2"]]
#print(data.groupby(['gender2'])[["NumberofOrders", "YearlyIncome", "SalesAmt","Age","NumberItems","city2"]].mean())

#print(data.head())
scale=StandardScaler()
scale.fit(data1)
dff = pd.DataFrame(scale.transform(data1),columns = data1.columns)
#print(dff.head())



clustering1=KMeans(n_clusters=4)
clustering1.fit(dff)
KMeans()
dff['Clusterlabel']=clustering1.labels_
#print(dff.head())
#print(data.head())

joined= pd.concat([dff, data], axis=1).reindex(dff.index)
#print(joined.head())
#data.to_clipboard()

joined.to_csv('clusterdata_scaled_joined.csv')


#centerdf=pd.DataFrame(clustering1.cluster_centers_)
#centerdf.columns=['x','y']

#plt.scatter(x=centerdf['x'],y=centerdf['y'],s=100,c='black',marker='*')
#sns.scatterplot(data=data, x='YearlyIncome', y='SalesAmt', hue='IncomeAndSalesCluster',palette='tab10')
#plt.show()

#print(pd.crosstab(data['IncomeAndSalesCluster'],data['gender']))

#print(dff['Clusterlabel'].value_counts())
##print(data.columns)
#print(data.groupby('Clusterlabel')[['Age','SalesAmt','NumberofOrders','NumberItems']].mean())
#print(data.groupby(['Clusterlabel','gender'])[['gender']].count())



#distortions = []
#K = range(1,10)
#for k in K:
#    kmeanModel = KMeans(n_clusters=k)
#    kmeanModel.fit(dff)
#    distortions.append(kmeanModel.inertia_)

#plt.figure(figsize=(16,8))
#plt.plot(K, distortions, 'bx-')
#plt.xlabel('k')
#plt.ylabel('Distortion')
#plt.title('The Elbow Method showing the optimal k')
#plt.show()


