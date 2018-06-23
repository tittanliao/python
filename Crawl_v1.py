import requests
import json
import pandas as pd
import sqlite3 as sql
from time import sleep

sStockId = '2344'
#format:'http://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=20170901&stockNo=2330'
sURL = 'http://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json'
lMonth = ['20170101', '20170201','20170301','20170401','20170501','20170601','20170701','20170801','20170901','20171001','20171101','20171201']
sCSVFilePath = '../../Data/' + sStockId + '.csv'
dResult = {}

for x in lMonth:
    sGet = sURL + '&date=' + x + '&stockNo=' + sStockId
    err_count = 0
    while err_count < 3:
        try:
            res = requests.get(sGet)
            dResult[x] = res.json()
            #sleep 5 secs
            sleep(5)
            break
        except:
            sleep(5)
            err_count += 1
            continue
    if err_count == 3:
        print('connect fail')
       
header = dResult[list(dResult)[0]]['fields']
data = dResult[list(dResult)[0]]['data']
iIndex = 0
for x in dResult:
    if iIndex != 0:
        data.extend(dResult[x]['data'])
    iIndex += 1

df = pd.DataFrame.from_records(data, columns=header)
df.sort_index(ascending=False).head()

for i, row in df.iterrows():
    strDate = row[0]
    DateArr = strDate.split("/")
    DateArr[0] = str(int(DateArr[0])+1911)
    DateArr[1] = str(int(DateArr[1]))
    DateArr[2] = str(int(DateArr[2]))
    df.loc[i, '日期'] = '/'.join(DateArr)
df.sort_index(ascending=False).head()
df.to_csv(sCSVFilePath, sep=',', encoding='utf-8-sig', index=False)

''' insert sql
#insert sql
conn = sql.connect("../../Data/twse.db")
df.to_sql("twse", conn, if_exists="replace", index=False)
pd.read_sql_query("select * from twse;", conn).sort_index(ascending=False)
'''
