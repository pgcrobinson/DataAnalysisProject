import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np
from scipy.stats import iqr
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from datetime import datetime
from tabulate import tabulate
from kneed import KneeLocator



df = pd.read_csv("marketing_campaign.csv", sep="\t")
#print(df.head())
#print(df.columns.values)

df["TotalAmountSpent"] = df["MntFishProducts"] + df["MntFruits"] + df["MntGoldProds"] + df["MntSweetProducts"] + df["MntMeatProducts"] + df["MntWines"]

df["Age"] = df["Year_Birth"].apply(lambda x : datetime.now().year - x)
#print(df["Age"].describe())

#print(df.Education.unique())

df["Education"] = df["Education"].replace({"Graduation":"Graduate", "PhD":"Postgraduate", "Master":"Postgraduate", "2n Cycle":"Postgraduate", "Basic":"Undergraduate"})
#print(df.Education.value_counts())

#print(df.Education.unique())



#sns.histplot(data=df, x="Age", bins = list(range(10, 150, 10)))
#plt.title("Distribution of Customer's Age")
#plt.savefig("Age.png")


###################################################################################
######################################## Building K means model with three features
###################################################################################

#print(df.columns.values)

df["Income"].fillna(df["Income"].median(), inplace=True)
data = df[["Age", "Income", "TotalAmountSpent"]]
df_log = np.log(data)
std_scaler = StandardScaler()
df_scaled = std_scaler.fit_transform(df_log)
sse = {}
for k in range(1, 11):
    model = KMeans(n_clusters=k, random_state=42)
    model.fit(df_scaled)
    sse[k] = model.inertia_
plt.title('The Elbow Method')
plt.xlabel('k'); plt.ylabel('SSE')
sns.pointplot(x=list(sse.keys()), y=list(sse.values()))
plt.show()

model = KMeans(n_clusters=3, random_state=42)
model.fit(df_scaled)


data = data.assign(ClusterLabel= model.labels_)
result = data.groupby("ClusterLabel").agg({"Age":"mean", "Income":"median", "TotalAmountSpent":"median"}).round()
print(result)


#fig = px.scatter_3d(data_frame=data, x="Income", 
#                    y="TotalAmountSpent", z="Age", color="ClusterLabel", height=550,
#                   title = "Visualizing Cluster Result Using 3 Features")
#fig.show()



#df["Income"].fillna(df["Income"].median(), inplace=True)
#data = df[["Income", "TotalAmountSpent"]]
#df_log = np.log(data)


#std_scaler = StandardScaler()
#df_scaled = std_scaler.fit_transform(df_log)
#errors = []
#for k in range(1, 11):
#    model = KMeans(n_clusters=k, random_state=42)
#    model.fit(df_scaled)
#    errors.append(model.inertia_)
#plt.title('The Elbow Method')
#plt.xlabel('k'); plt.ylabel('SSE')
#sns.pointplot(x=list(range(1, 11)), y=errors)
#plt.savefig("Elbow.png")


#kl = KneeLocator(x = range(1, 11),
#                 y = errors,
#                 curve="convex",
#                 direction="decreasing")
#print('The optimum number of clusters is: ' + str(kl.elbow))

