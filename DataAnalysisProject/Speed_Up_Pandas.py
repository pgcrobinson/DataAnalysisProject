import pandas as pd
import numpy as np
import time


def get_data(size=10000):
    df = pd.DataFrame()
    df['age'] =np.random.randint(0,100,size)
    df['time_in_bed'] = np.random.randint(0,9,size)
    df['pct_sleeping']=np.random.rand(size)
    df['favourite_food']=np.random.choice(['pizza','taco','ice-cream'],size)
    df['hate_food']=np.random.choice(['brocoli','candy corn','eggs'],size)
    return df


#print(get_data())

################LEVEL 1 - LOOP ##################

def reward_calc(row):
    if row['age']>=90:
        return row['favourite_food']
    if (row['time_in_bed']>5) & (row['pct_sleeping']>0.5):
        return row['favourite_food']
    return row['hate_food']


df=get_data() 
start_time_level_1 = time.time()

for index, row in df.iterrows():
    df.loc[index,'reward']=reward_calc(row)

end_time_level_1=time.time()
level_1_time = end_time_level_1-start_time_level_1
print('This is the level 1 time: '+ str(level_1_time))


######################## LEVEL 2 - APPLY ###########
start_time_level_2 = time.time()
#df=get_data()
df['reward']=df.apply(reward_calc, axis=1)
end_time_level_2=time.time()
level_2_time = end_time_level_2-start_time_level_2
print('This is the level 2 time: '+ str(level_2_time))

######################## LEVEL 3 - Vectorised ###########
start_time_level_3 = time.time()
#df=get_data()
df['reward']=df['hate_food']
df.loc[((df['pct_sleeping']>0.5) & (df['time_in_bed']>5)) | (df['age']>90),'reward']=df['favourite_food']
end_time_level_3=time.time()
level_3_time = end_time_level_3-start_time_level_3
print('This is the level 3 time: '+ str(level_3_time))


