import pyodbc
import pandas as pd
import urllib
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
import matplotlib as mpl

#df = pd.read_csv("marketing_campaign.csv", sep="\t")



#conn = urllib.parse.quote_plus(
#    'Data Source Name=sqlserverdatasource;'
#    'Driver={SQL Server};'
#    'Server=DESKTOP-DRPFO66\PETER;'
#    'Database=TableauData;'
#    'Trusted_connection=yes;'
#)
 
#try:
    
#    coxn = create_engine('mssql+pyodbc:///?odbc_connect={}'.format(conn))
#    print("Passed")
 
#except:
#    print("failed!")


#connection = coxn.connect()

#df.to_sql("CustomerTableDataScience", coxn)


##################################
sql_conn = pyodbc.connect('DRIVER={SQL Server}; SERVER=DESKTOP-DRPFO66\PETER;DATABASE=TableauData;Trusted_Connection=yes')                     
query = "SELECT top 100* FROM propertyprices"
df = pd.read_sql(query, sql_conn)


print(df.head())

###################################
