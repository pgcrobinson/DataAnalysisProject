import bs4 as bs
import pandas as pd
import numpy as np
import re
from urllib import request
from urllib.request import Request, urlopen
from string import ascii_letters

url_locations = "https://www.harvester.co.uk/restaurants#/"

request_site = Request(url_locations, headers={"User-Agent": "Mozilla/5.0"})
webpage = urlopen(request_site).read()

soup = bs.BeautifulSoup(webpage,'lxml')

url_list =[]
for url in soup.find_all('a'):
    url_list.append(str(url.get('href')))

#print(url_list)
new_url_list=[]

for s in url_list:
    if re.search('www.harvester', s):
        s+="/mainmenu#/"
        new_url_list.append(s)
    else:
       pass

test_url_list = ['https://www.harvester.co.uk/restaurants/northeast/harvesterryhopesunderland/mainmenu#/','https://www.harvester.co.uk/restaurants/eastofengland/thewhitehartleightonbuzzard/mainmenu#/']

for the_url in new_url_list:
    try:
 
        url = the_url
        request_site = Request(url, headers={"User-Agent": "Mozilla/5.0"})
        webpage = urlopen(request_site).read()

        soup = bs.BeautifulSoup(webpage,'lxml')
        nav = soup.nav

        df = pd.DataFrame(columns=['A'])

        for food in soup.find("div", class_="menu").stripped_strings:
            #food.find_all("div", class_="menu--menu-content")
   
            #print(food)
            df = df.append({'A':food}, ignore_index=True)


        idx_start=df.index[df['A'] == 'Style Starters'][0]
        idx_end = df.index[df['A'] == 'Grills'][0]
        df1 = df.loc[idx_start+5  : idx_end-1]

        df1=pd.DataFrame(df1.values.reshape(-1, 4), columns=['A','B','C','D'])

        df1['Menu_Section']='Starters'
        df1['Restaurant_URL']=url

        df1.to_csv('soup_shaped.csv',mode='a',header=False,index=False)


        idx_start=df.index[df['A'] == 'Grills'][0]
        idx_end = df.index[df['A'] == 'Steaks'][0]
        df2 = df.loc[idx_start+1  : idx_end-3]

        df2=df2[~df2["A"].str.contains("Upgrade")]

        df2=pd.DataFrame(df2.values.reshape(-1, 4), columns=['A','B','C','D'])

        df2['Menu_Section']='Grills'
        df2['Restaurant_URL']=url

        df2.to_csv('soup_shaped.csv', mode='a', header=False,index=False)

        idx_start=df.index[df['A'] == 'Steaks'][0]
        idx_end = df.index[df['A'] == 'CHOOSE YOUR SAUCE'][0]
        df3 = df.loc[idx_start+3  : idx_end-2]

        df3=pd.DataFrame(df3.values.reshape(-1, 3), columns=['A','B','C'])

        df3['D']='No Description'
        df3['Menu_Section']='Steaks'
        df3['Restaurant_URL']=url

        columns_titles = ["A","D","B","C","Menu_Section","Restaurant_URL"]
        df3=df3.reindex(columns=columns_titles)

        df3.to_csv('soup_shaped.csv', mode='a', header=False,index=False)

        idx_start=df.index[df['A'] == 'Flatbreads'][0]
        idx_end = df.index[df['A'] == 'BALANCED'][0]
        df4 = df.loc[idx_start+2  : idx_end-1]

        df4=pd.DataFrame(df4.values.reshape(-1, 3), columns=['A','B','C'])

        df4['D']='No Description'
        df4['Menu_Section']='Flatbreads'
        df4['Restaurant_URL']=url

        columns_titles = ["A","D","B","C","Menu_Section","Restaurant_URL"]
        df4=df4.reindex(columns=columns_titles)

        df4.to_csv('soup_shaped.csv', mode='a', header=False,index=False)
        print('Completed '+ the_url)
    except:
        print('THE URL FOR '+ the_url+ ' DID NOT WORK')