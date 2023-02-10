import pandas as pd
from sklearn.preprocessing import LabelEncoder

df = pd.DataFrame(
    {
        "A": ["A0", "A1", "A2", "A1"],
        "B": ["B0", "B1", "B2", "B3"],
        "C": ["C0", "C1", "C2", "C3"],
        "D": ["D0", "D1", "D2", "D3"],
    }
)

#print(df.head())


df1=df.drop(columns=['A'])
df2=df[['A']]
#print(df1.head())
#print(df2.head())

le = LabelEncoder()

df2['A2'] = le.fit_transform(df['A'])
#print(df2.head())

joined= pd.concat([df1, df2], axis=1)

print(joined.head())