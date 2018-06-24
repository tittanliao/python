
''' test daily
'''
import requests
import pyodbc
import pandas as pd

server = 'aholic.cc'
database = 'stock'
username = 'sa'
password = 'qweqwe1!qweqwe1!'
driver= '{ODBC Driver 13 for SQL Server}'
cnxn = pyodbc.connect('DRIVER='+driver+';PORT=1433;SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)
sql = "SELECT id FROM isin WHERE market_type_detail IN ('股票','ETF')"
df_db = pd.read_sql(sql, cnxn)

sURL = 'http://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json'
x = '20180101'
sGet = sURL + '&date=' + x + '&stockNo=' + str(df_db.loc[0][0])
res = requests.get(sGet)
a = res.json()



'''test sql insert
'''
import pandas as pd
import pyodbc

server = 'aholic.cc'
database = 'stock'
username = 'sa'
password = 'qweqwe1!qweqwe1!'
driver= '{ODBC Driver 13 for SQL Server}'
cnxn = pyodbc.connect('DRIVER='+driver+';PORT=1433;SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)

sql = 'SELECT * FROM isin'
data = pd.read_sql(sql, cnxn)

import datetime

cols = ['id','name','isin_code','create_day','market_type','market_type_detail','industry_type','update_time','update_user']
rows = []
rows.append(['2345', '華邦電', 'TW0002344009','19951018','上市','股票','半導體業','20180617 12:00:00','tittan'])
df1 = pd.DataFrame(rows, columns=cols)
df1.to_sql(sql, cnxn)